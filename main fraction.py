from fraction import Fraction

print("\t\t\t Menu")
print("Ingrese simbolo de operacion a querer realizar: + - * / ")
o=input()
print("Operacion seleccionada: " + o)
if o=="+":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 1")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 2")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()
    b=Fraction(n,d)
    b.print()
    
    r=a.addition(b)
    r.print()


elif o=="-":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 1")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()
    a=Fraction(n,d)
    a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 2")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()
    b=Fraction(n,d)
    b.print()

    r=a.subtraccion(b)
    r.print()

elif o=="*":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 1")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()
    a=Fraction(n,d)
    a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 2")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()
    b=Fraction(n,d)
    b.print()

    r=a.multiply(b)
    r.print()

elif o=="/":
    print("Ingrese numerador 1:")
    n=int(input())
    print("ingrese denominador 1")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 1")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()
    a=Fraction(n,d)
    a.print()

    print("Ingrese numerador 2:")
    n=int(input())
    print("Ingrese denominador 2:")
    d=int(input())
    while d==0:
        if d==0:
            print("Numerador debe ser diferente de 0")
            print("ingrese denominador 2")
            d=int(input())
            a=Fraction(n,d)
            a.print()
        else:
            a=Fraction(n,d)
            a.print()
    b=Fraction(n,d)
    b.print()

    r=a.division(b)
    r.print()

else:
    print("Favor Ingresar una opcion valida")