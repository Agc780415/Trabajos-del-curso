# imports random module
import random

def dame_numero():
    numero = random.randint( 1 , 100)
    return numero
def main():
    print "adivina un numero del 1 al 100"
    numero_secreto = dame_numero()
    print numero_secreto
    seguir = True
    while seguir:
        numero_usuario = raw_input("pon tu numero aqui: ")
        numero_valido = True
        if int(numero_usuario) > 100:
            numero_valido = False
            print "No sabes contar... numero mayor que 100"
        elif int(numero_usuario) < 1:
            numero_valido = False
            print "No sabes contar... numero menor que 1"
        if numero_valido:
            if int(numero_usuario) == numero_secreto:
                seguir = False
                print "felicidades numero correcto"
            else:
                print"Numero incorrecto, Prueba de nuevo tontin"
                otra = raw_input("desea intentarlo otra vez, responda (s o n), ")
                if otra == "s":
                    seguir = True
                else:
                    seguir = False
                    print "hasta la proxima"

if __name__ == "__main__": main()



