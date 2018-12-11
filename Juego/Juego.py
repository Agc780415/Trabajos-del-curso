print "adivina un numero del 1 al 100"
numero_secreto = int("35")
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
        print "felicidades numero correcto"
    else:
        print"Numero incorrecto, Prueba de nuevo tontin"
