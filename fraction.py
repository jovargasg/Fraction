class Fraction():
    ##atributos##
    numerator=0
    denominator=1
    ##fin atributos##

    ##metodos##
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator

    def print(self):
        print(self.numerator,"/",self.denominator)
    
    def multiply(self,b):
        result_numerator=self.numerator*b.numerator
        result_denominator=self.denominator*b.denominator
        r=Fraction(result_numerator,result_denominator)
        return r
    
    def addition(self,b):
        result_numerator=(self.numerator*b.denominator)+(self.denominator*b.numerator)
        result_denominator=self.denominator*b.denominator
        r=Fraction(result_numerator,result_denominator)
        return r

    def division(self,b):
        result_numerator=self.numerator*b.denominator
        result_denominator=self.denominator*b.numerator
        r=Fraction(result_numerator,result_denominator)
        return r

    def subtraccion(self,b):
        result_numerator=(self.numerator*b.denominator)-(self.denominator*b.numerator)
        result_denominator=self.denominator*b.denominator
        r=Fraction(result_numerator,result_denominator)
        return r
    ##fin metodos##