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


print("------Menu------")
print("Ingrese simbolo de operacion a querer realizar: + - * / ")
o=input()
print("Operacion seleccionada: " + o)
if o=="+":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    a=Fraction(n,d)
    a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    b=Fraction(n,d)
    b.print()
    
    r=a.addition(b)
    r.print()


elif o=="-":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    a=Fraction(n,d)
    a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    b=Fraction(n,d)
    b.print()

    r=a.subtraccion(b)
    r.print()

elif o=="*":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    a=Fraction(n,d)
    a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    b=Fraction(n,d)
    b.print()

    r=a.multiply(b)
    r.print()

elif o=="/":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    a=Fraction(n,d)
    a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    b=Fraction(n,d)
    b.print()

    r=a.division(b)
    r.print()

else:
    print("Favor Ingresar una opcion valida")
