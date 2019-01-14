class Vehiculo:
    def __init__(self, matricula, marca, modelo, km, fecha_servicio):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.fecha_servicio = fecha_servicio

def todos_los_vehiculos(vehiculos):
    for index, vehiculo in enumerate(vehiculos):
        print "Matricula -: " + vehiculo.matricula
        print "Marca -----: " + vehiculo.marca
        print "Modelo ----: " + vehiculo.modelo
        print "kms -------: " + vehiculo.km
        print "F-servicio-: " + vehiculo.fecha_servicio
        print ""  # empty line

def agegar_nuevo_vehiculo(vehiculos):
    matricula = raw_input("por favor escriba la matricula: ")
    marca = raw_input("Por favor escriba la marca: ")
    modelo = raw_input("Por favor escriba el modelo: ")
    km = raw_input("Por favor escriba los km: ")
    fecha_servicio = raw_input("Por favor escriba la fecha de servicio: ")

    new = Vehiculo(matricula=matricula, marca=marca, modelo=modelo, km=km, fecha_servicio=fecha_servicio )
    vehiculos.append(new)


def quitar_vehiculo(vehiculos):
    print "Seleccione la matricula del vehiculo a eliminar: "

    for index, vehiculo in enumerate(vehiculos):
        print vehiculo.matricula

    print ""  # empty line
    seleccion_usuario = raw_input("escriba la matricula que desee eliminar: ")
    vehiculo = buscar_matricula(vehiculos, seleccion_usuario)
    vehiculos.remove(vehiculo)
    print ""  # empty line
    print "El vehiculo esta eliminado."

def buscar_matricula(vehiculos, matricula):
    for index, vehiculo in enumerate(vehiculos):
        if matricula == vehiculo.matricula:
            break
    return vehiculo


def editar(vehiculos):
    print "Seleccione la matricula del vehiculo a editar: "

    for index, vehiculo in enumerate(vehiculos):
        print vehiculo.matricula

    print ""  # empty line
    seleccion_usuario = raw_input("escriba la matricula del vehiculo a modificar: ")
    vehiculo = buscar_matricula(vehiculos, seleccion_usuario)
    edicion_km = raw_input("cambie aqui los kms: ")
    edicion_servicio =raw_input("cambie aqui la fecha de servicio: ")
    vehiculo.km = edicion_km
    vehiculo.fecha_servicio = edicion_servicio



def main():
    print "Programa de control de servicio general, kilometros y modelo de vehiculos"

    coche1 = Vehiculo(matricula="001", marca="Fiat", modelo="Punto", km="0012423", fecha_servicio="04/01/2019")

    vehiculos = [coche1]


    while True:
        print ""  # empty line
        print "Indique una de las opciones:"
        print "a) Mostrar lista de vehiculos"
        print "b) Agregar vehiculo"
        print "c) Quitar vehiculo"
        print "d) Editar kms o fecha de servicio"
        print "e) Salir del programa"
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""  # empty line

        if selection.lower() == "a":
            todos_los_vehiculos(vehiculos)
        elif selection.lower() == "b":
            agegar_nuevo_vehiculo(vehiculos)
        elif selection.lower() == "c":
            quitar_vehiculo(vehiculos)
        elif selection.lower() == "d":
            editar(vehiculos)
        elif selection.lower() == "e":
            print "Gracias y hasta nunca"
            break
        else:
            print "La seleccion no es correcta, Pruebe de nuevo"
            continue





if __name__ == "__main__":
    main()
