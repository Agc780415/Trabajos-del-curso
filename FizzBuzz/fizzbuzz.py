print "instrucciones: Escribe un numero del 1 al 100." \
      " si tu numero es divisible por 3 veras fizz" \
      "y si lo es por 5 buzz, ya si se divide por los 2 veras fizzbuzz."
seguir = True
while seguir:
    numero= raw_input ("Escribe un numero del 1 al 100, ")
    respuesta = int (numero)

    div3 = respuesta % 3
    div5 = respuesta % 5
    if div3 == 0:
        if div5 == 0:
            print "fizzbuzz"
        else:
            print "fizz"
    else:
        if div5 == 0:
            print "buzz"
        else:
            print "tu numero no es divisible por: 3 ni 5"
    otra = raw_input("desea hacer otra division responda (s o n), ")
    if otra == "s":
        seguir = True
    else:
        seguir = False
        print "hasta la proxima division"



