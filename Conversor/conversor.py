
print "Hola este es un programa para convertir kilometros a millas"
seguir = True
while seguir:
    km = raw_input ("Escribe aqui kilometros,solo numeros, ")
    km = km.replace("," , ".")
    milla = float(km) * 0.621371
    print milla
    otra = raw_input ("desea hacer otra convercion responda (s o n), ")
    if otra == "s":
        seguir = True
    else:
        seguir = False
        print "hasta la proxima conversion"

