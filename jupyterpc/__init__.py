from uncertainties import ufloat
import uncertainties

l_1 = [ufloat(x, 1) for x in range(10)]
l_2 = [x**2 for x in l_1]
l_3 = [ufloat(x, 1) for x in range(21,30)]

def sci(number, decimals=4):
    if type(number) == uncertainties.core.Variable:
        return number.format('L')
    elif type(number) ==float:
        float_str = "{0:.2g}".format(number)
        if "e" in float_str:
            base, exponent = float_str.split("e")
            return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
        else:
            return float_str
    else:
        return str(number)

def table(name, data):
    max_len = max([len(x) for x in data.values()])
    tab_str = 'l'+''.join(['|l']*(len(data)-1))
    start = '''
            \\begin{table}
                \\caption{%s}
                \\centering
                \\begin{tabular}{%s}
            ''' % (str(name), tab_str)
    name_str = '\t'+''.join(['%s & ' % (n) for n in data.keys()])[:-2]+'\\\\\n'
    end = '''
                \\end{tabular}
            \\end{table}
          '''
    data_str = []
    for i in range(max_len-1):
        data_str += '\t\t'+''.join([sci(x[i])+' & ' for x in data.values()])[:-2]+'\\\\\n'
    data_str = ''.join(data_str)
    return start+name_str+data_str+end
print(table('test', {'col1':[1,2,3,4], 'col2':[5,6,7,8]}))
print(table('test', {'col1':[10,200,3000,4e4], 'col2':[0.5,0.06,0.07,0.008]}))
print(table('test', {'col1':[143978912,27281940,3276,42143], 'col2':[0.0000005234,0.602134,72143e-100]}))
