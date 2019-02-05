from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy import odr
import numpy as np
import uncertainties as uc
from jinja2 import Template
import jinja2
import os
import codecs

ucvar = [uc.core.AffineScalarFunc, uc.core.Variable]

def sci(num, decimals=4):
    if type(num) in ucvar:
        return num.format('L')
    elif type(num) in [float, int]:
        float_str = str("{0:."+str(decimals)+"g}").format(num)
        if "e" in float_str:
            base, exponent = float_str.split("e")
            return "{0} \\times 10^{{{1}}}".format(base, int(exponent))
        else:
            return float_str
    else:
        return str(num)

def num(ulist):
    if type(ulist[0]) in ucvar:
        if type(ulist) == np.ndarray:
            return np.array([x.n for x in ulist])
        else:
            return [x.n for x in ulist]
    else:
        raise BaseException('input must be a list of ufloats or an uarray')
 
def sig(ulist):
    if type(ulist[0]) in ucvar:
        if type(ulist) == np.ndarray:
            return np.array([x.s for x in ulist])
        else:
            return [x.s for x in ulist]
    else:
        raise BaseException('input must be a list of ufloats or an uarray')


def fit(data_x, data_y, sigma_x=None, sigma_y=None, func=None, beta=[1., 0.], *args, **kwargs):
    if func == None:
        func = lambda p,x: p[0]*x+p[1]

    if type(data_x[0]) in ucvar:
        values_x = [d.n for d in data_x]
        sigma_x = [d.s if d.s!=0 else 1e-5 for d in data_x]
    else: #type(data_x[0]) in [float, int]:
        values_x = data_x

    if type(data_y[0]) in ucvar:
        values_y = [d.n for d in data_y]
        sigma_y = [d.s if d.s!=0 else 1e-5 for d in data_y]
    else: #type(data_y[0]) in [float, int]:
        values_y = data_y

    data = odr.RealData(values_x, values_y, sx=sigma_x, sy=sigma_y)
    model = odr.Model(func)
    odrfit = odr.ODR(data, model, beta0=beta)
    out = odrfit.run()
    return [ufloat(n, s) for n, s in zip(out.beta, out.sd_beta)] 

def table(name, data):
    max_len = max([len(x) for x in data.values()])
    tab_str = 'l'+''.join(['|l']*(len(data)-1))
    start = '''
            \\begin{table}[H]
                \\caption{%s}
                \\centering
                \\begin{tabular}{%s}
            ''' % (str(name), tab_str)
    name_str = '\t\t'+''.join(['$ %s $ & ' % (n) for n in data.keys()])[:-2]+'\\\\\n'
    hline = '\\hline \n'
    end = '''
                \\end{tabular}
            \\end{table}
          '''
    data_str = []
    for i in range(max_len):
        data_str += '\t\t\t'+''.join(['$'+sci(x[i])+'$ & ' for x in data.values()])[:-2]+'\\\\\n'
    data_str = ''.join(data_str)
    return start+name_str+hline+data_str+end


def uplot(data_x, data_y, *args, fmt=' ', **kwargs):
    sigma_x = None
    sigma_y = None
    if type(data_x[0]) in ucvar:
        values_x = [d.n for d in data_x]
        sigma_x = [d.s if d.s!=0 else 1e-5 for d in data_x]
    elif type(data_x[0]) in [float, int]:
        values_x = data_x

    if type(data_y[0]) in ucvar:
        values_y = [d.n for d in data_y]
        sigma_y = [d.s if d.s!=0 else 1e-5 for d in data_y]
    elif type(data_y[0]) in [float, int]:
        values_y = data_y
    plt.errorbar(values_x, values_y, xerr=sigma_x, yerr=sigma_y, *args, fmt=fmt, **kwargs)


def render(template_path, output_path, variables):
    latex_jinja_env = jinja2.Environment(
        block_start_string = '\BLOCK{',
        block_end_string = '}',
        variable_start_string = '\VAR{',
        variable_end_string = '}',
        comment_start_string = '\#{',
        comment_end_string = '}',
        line_statement_prefix = '%%',
        line_comment_prefix = '%#',
        trim_blocks = True,
        autoescape = False,
        loader = jinja2.FileSystemLoader(os.path.abspath('.'))
    )

    template = latex_jinja_env.get_template(template_path)
    with codecs.open(output_path, 'w', encoding='utf-8') as out:
        out.write(template.render(variables))    

