class Diff:

    def Chain(self, formula):
        bracketSlice = formula[formula.find('(') + 1 : formula.find(')')]
        if formula.find('(') == 0:
            strPower = (formula[formula.find(')^') + 2 : ])
            strCoeff = strPower + '*' + Diff(bracketSlice)
            return '{0}({1})^{2}'.format(Multiply(strCoeff), bracketSlice, int(strPower) -1)

    def Quotient(self, formula):
        formula = formula.split('\\')

        #sets up strings for multplication
        vu = '{0}*{1}'.format(formula[1], self.Diff(formula[0]))
        uv = '{0}*{1}'.format(formula[0], self.Diff(formula[1]))

        if formula[1].find('x') == -1: #squares the denominator if it is only an integer
            return '{0}-{1}\{2}'.format(self.Multiply(vu), self.Multiply(uv), int(formula[1]) **2)
        return '{0}-{1}\({2})^2'.format(self.Multiply(vu), self.Multiply(uv), formula[1])
        
    def Product(self, formula):
        if '*' in formula:
            formula = formula.replace('*', ')(')
        formula = formula.lstrip('(').rstrip(')').split(')(')
        
        #formats the two parts of the product rule
        vu = '{0}*{1}'.format(formula[1], self.DiffHandler(formula[0]))
        uv = '{0}*{1}'.format(formula[0], self.DiffHandler(formula[1]))
        
        return '{0}+{1}'.format(self.Multiply(vu), self.Multiply(uv))

    def Addition(self, formula):
        #splits up the input by the operands of the input
        if '-' in formula:
            formula = formula.replace('-', '+-')
 
        if '+' in formula:
            formula = formula.split('+')
            
            for i in range(len(formula)):
                formula[i] = self.DiffHandler(formula[i])

            formula = '+'.join(formula)
            return formula
            
    def GeneralForm(self, formula):
        if 'x' not in formula: #handles constants
            return '0'

        elif formula.find('^') == -1: #for no power
            return str(self.Coefficient(formula))

        else: #handles general form
            return '{0}x^{1}'.format(self.Coefficient(formula) * self.Power(formula), self.Power(formula) -1)
        
    def Multiply(self, expression):
        expression = expression.replace(' ', '')

        if '+' in expression or expression.find('-') > 0:
            expression = expression.split('*')
            expression = '(' + expression[0] + ')(' + expression[1] + ')'
            return expression
        else:
            expression = expression.split('*')
            if (Power(expression[0]) + Power(expression[1])) == 0:
                return str(self.Coefficient(expression[0]) * self.Coefficient(expression[1]))
        
            elif self.Coefficient(expression[0]) * self.Coefficient(expression[1]) == 0:
                return 'x{0}'.format(self.Power(expression[0]) + self.Power(expression[1]))
            return '{0}x^{1}'.format(self.Coefficient(expression[0]) * self.Coefficient(expression[1]), self.Power(expression[0]) + self.Power(expression[1]))

    def Coefficient(self, expression):
        if expression.find('x') == 0:
            return 1
        elif 'x' not in expression:
            return int(expression)
        elif expression.find('/') != -1 and expression.find('/') < expression.find('x'):
            return int(expression[:expression.find('/')]) / int(expression[expression.find('/') + 1 : expression.find('x')])
        
        return int(expression[0:expression.find('x')])

    def Power(self, expression):
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

        return 1

    def DiffHandler(self, formula):
        if '\\' in self.formula:
            self.formula = self.Quotient(formula)
        elif '*' or ')(' in formula:
            self.formula = self.Product(formula)
        elif '+' or '-' in formula:
            self.formula = self.Addition(formula)
        else:
            self.formula = self.GeneralForm(formula)
        print self.formula