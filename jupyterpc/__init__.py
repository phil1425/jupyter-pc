from uncertainties import ufloat
import uncertainties

def sci(number, decimals=4):
    if type(number) == uncertainties.core.Variable:
        return number.format('L')
    elif type(number) in [float, int]:
        float_str = "{0:."+decimals+"g}".format(number)
        if "e" in float_str:
            base, exponent = float_str.split("e")
            return r"{0} \times 10^{{{1}}}".format(base, int(exponent))
        else:
            return float_str
    else:
        return str(number)

def ulist(list_val, sigma):
	if type(sigma) in [int, float]:
		return [ufloat(x, sigma) for x in list_val]
	if type(sigma) == list:
		if list_val.length == sigma.length:
			return [ufloat(v, s) for v, s in zip(list_val, sigma)]
		else:
			print('list and sigma must be the same length')
			print('sigma', sigma.length)
			print('values', list_val.length)

def table(name, data):
    max_len = max([len(x) for x in data.values()])
    tab_str = 'l'+''.join(['|l']*(len(data)-1))
    start = '''
            \\begin{table}
                \\caption{%s}
                \\centering
                \\begin{tabular}{%s}
            ''' % (str(name), tab_str)
    name_str = '\t\t'+''.join(['%s & ' % (n) for n in data.keys()])[:-2]+'\\\\\n'
    end = '''
                \\end{tabular}
            \\end{table}
          '''
    data_str = []
    for i in range(max_len-1):
        data_str += '\t\t\t'+''.join(['$'+sci(x[i])+'$ & ' for x in data.values()])[:-2]+'\\\\\n'
    data_str = ''.join(data_str)
    return start+name_str+data_str+end
