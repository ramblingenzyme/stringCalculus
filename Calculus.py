#Calculus library
#TheEnzyme


def Diff(formula):

    if '\\' in formula: #applies quotient rule
        formula = formula.split('\\')

        #sets up strings for multplication
        vu = '{0}*{1}'.format(formula[1], Diff(formula[0]))
        uv = '{0}*{1}'.format(formula[0], Diff(formula[1]))

        if formula[1].find('x') == -1:
            return '{0}-{1}\{2}'.format(Multiply(vu), Multiply(uv), int(formula[1]) **2)
        return '{0}-{1}\({2})^2'.format(Multiply(vu), Multiply(uv), formula[1])
    
    elif ')(' in formula: #applies the product rule
        formula = formula.lstrip('(').rstrip(')').split(')(')

        vu = '{0}*{1}'.format(formula[1], Diff(formula[0]))
        uv = '{0}*{1}'.format(formula[0], Diff(formula[1]))
        print vu, uv
        return '{0}+{1}'.format(Multiply(vu), Multiply(uv))

    elif ')^' in formula: 
        bracketSlice = formula[formula.find('(') + 1 : formula.find(')')]
        if formula.find('(') == 0:
            strPower = (formula[formula.find(')^') + 2 : ])
            strCoeff = strPower + '*' + Diff(bracketSlice)
            print strCoeff
            return '{0}({1})^{2}'.format(Multiply(strCoeff), bracketSlice, int(strPower) -1)

        elif formula.find('(') > 0:
            if Diff(formula[:formula.find('(')]) != '0':
                retPower = (formula[formula.find(')^') + 2 : ])
                retCoeff = '{0}*{1}'.format(Diff(formula[:formula.find('(')]), retPower)
                return '{0}({1})({2})^{3}'.format(Multiply(retCoeff), Diff(bracketSlice), bracketSlice, int(retPower) - 1)

    elif '+' in formula or '-' in formula: #handles more than one operand
        output = list()
        divider = '-'

        #splits up the input by the operands of the input
        if '+' in formula:
            divider = '+'
        formula = formula.replace(' ', '').split(divider.strip())
        print formula
        for i in range(len(formula)):
            if Power(formula[i]) == 1:
                output.append(str(Coefficient(formula[i])))

            elif Coefficient(formula[i]) == 0 or Diff(formula[i]) == '0':
                pass
            else:
                output.append(Diff(formula[i]))
            print output
 
        return divider.join(output)

    elif 'x' not in formula: #handles constants
        return '0'

    elif formula.find('^') == -1: #for no power
        return str(Coefficient(formula))

    else: #handles general form
        return '{0}x^{1}'.format(Coefficient(formula) * Power(formula), Power(formula) -1)

def Multiply(formula): #only can handle two strings being multiplied together.
    formula = formula.replace(' ', '')

    if '+' in formula or formula.find('-') > 0:
        formula = formula.replace('-','+-').split('*')
        output = list()

        for i in range(len(formula)):
            if '+' in formula[i]:
                formula[i] = formula[i].split('+')

        for i in range(len(formula[0])):
            for x in range(len(formula[1])):
                output.append(Multiply('{0}*{1}'.format(formula[0][i], formula[1][x])))
        output = '+'.join(output)

        if '-' in output:
            return output.replace('+-', '-')
        return output
        
    else:
        formula = formula.split('*')
        if (Power(formula[0]) + Power(formula[1])) == 0:
            return str(Coefficient(formula[0]) * Coefficient(formula[1]))
        
        elif Coefficient(formula[0]) * Coefficient(formula[1]) == 0:
            return 'x{0}'.format(Power(formula[0]) + Power(formula[1]))
        return '{0}x^{1}'.format(Coefficient(formula[0]) * Coefficient(formula[1]), Power(formula[0]) + Power(formula[1]))

def Coefficient(expression):
    if expression.find('x') == 0:
        return 1
    elif 'x' not in expression:
        return int(expression)
    
    elif expression.find('/') != -1 and expression.find('/') < expression.find('x'):
        return int(expression[:expression.find('/')]) / int(expression[expression.find('/') + 1 : expression.find('x')])
        
    return int(expression[0:expression.find('x')])

def Power(expression):
    if expression.find('x^') != -1:
        power = expression[expression.find('^') +1: ]
        if 'x' in power:
            return int(power[:power.find('x')])
        else:
            return int(power)

    elif expression.find('x') == -1:
        return 0

    elif expression[0] == '^':
        return expression[1:]
    else:
        return 1 

#Broken code written at stupid times with idiot ball. Also broken
##def Simplification(formula):
##    number = []
##    for a in range(len(formula[0])):
##	for b in range(len(formula[1])):
##	    if Power(formula[0][a]) == Power(formula[0][b]):
##		formula[0][a] = str(Coefficient(formula[0][a]) + Coefficient(formula[1][b])) + 'x^' + str(Power(formula[0][a]))
##		number.append(formula[0][a])
##		print formula
##    print number
