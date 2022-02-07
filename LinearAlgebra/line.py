from decimal import Decimal, getcontext
from vector import Vector

getcontext().prec = 30

class Line(object):
    
    NO_NONZERO_ELEMENTS_ERROR = 'No nonzero elements found!'

    def __init__(self, normalVector = None, constantTerm = None):
        self.dimension = 2 # lines are 2D

        # initialise the normal vector (default: [0, 0])
        if not normalVector:
            allZeroes = ['0'] * self.dimension
            normalVector = Vector(allZeroes)
        self.normalVector = normalVector

        # initialise the constant term (default: 0)
        if not constantTerm:
            constantTerm = Decimal('0')
        self.constantTerm = Decimal(constantTerm)

        self.setBasePoint()

    # set the line's base
    def setBasePoint(self):
        try:
            n = self.normalVector
            c = self.constantTerm
            basepointCoords = ['0'] * self.dimension

            initIndex = Line.firstNonzeroIndex(n)
            initCoefficient = n[initIndex]

            basepointCoords[initIndex] = c / initCoefficient
            self.basepoint = Vector(basepointCoords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELEMENTS_ERROR:
                self.basepoint = None
            else:
                raise e

    # output the standard form of the line
    def __str__(self):

        numDecimalPlaces = 3

        def writeCoefficient(coefficient, isInitialTerm = False):
            coefficient = round(coefficient, numDecimalPlaces)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not isInitialTerm:
                output += '+'
            if not isInitialTerm:
                output += ' '
            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))
            
            return output

        n = self.normalVector

        try:
            initIndex = Line.firstNonzeroIndex(n)
            terms = [writeCoefficient(n[i], isInitialTerm = (i == initIndex)) + 'x_{}'.format(i + 1) for i in range(self.dimension) if round(n[i], numDecimalPlaces) != 0]
            output = ' '.join(terms)
        except Exception as e:
            if str(e) == self.NO_NONZERO_ELEMENTS_ERROR:
                output = '0'
            else:
                raise e
        
        constant = round(self.constantTerm, numDecimalPlaces)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    # helper function to find the first nonzero index
    @staticmethod
    def firstNonzeroIndex(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).isNearZero():
                return k
        raise Exception(Line.NO_NONZERO_ELEMENTS_ERROR)

# to find values close to 0. Avoids rounding errors
class MyDecimal(Decimal):
    def isNearZero(self, tolerance = 1e-10):
        return abs(self) < tolerance