print "programa para guardar el menu del restaurante"
seguir = True
menu = {}
while seguir:

    plato = raw_input("Escribe aqui el nombre del plato: ")
    precio = raw_input("Escribe aqui el precio del plato: ")
    menu [plato] = precio
    nuevo_plato = raw_input("desea escribir otro plato, responda con ( s o n ): ")
    if nuevo_plato == "s" :
        seguir = True
    else:
        seguir = False
        print "Fin del menu Hasta la proxima."
respuesta = raw_input ("responde (s o n) para imprimir el menu: ")
if respuesta == "s" :
    print menu
    with open("menu.txt", "w+") as menu_file:  # open the file for writing and overwrite the previous file (w+)
        for dish in menu:
            menu_file.write(
                "%s, %s EUR\n" % (dish, menu[dish]))  # write this text into the file and add a new line at the end (\n)
else:
    print "No se imprime el menu, Hasta la proxima."






