from uncertainties import ufloat
import uncertainties

l_1 = [ufloat(x, 1) for x in range(10)]
l_2 = [ufloat(x, 1) for x in range(11,20)]
l_3 = [ufloat(x, 1) for x in range(21,30)]

print(type(l_1[0]))

def sci(number, decimals=4):
    if type(number) == uncertainties.core.Variable:
        return number.format('L')
    else:
        
