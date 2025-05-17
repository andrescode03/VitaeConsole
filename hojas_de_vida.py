hojas_de_vida = []

def registrar_hoja_de_vida():
    # TODO: Mostrar encabezado del registro de hoja de vida
    print(" Registro de hoja de vida")

    # TODO: Solicitar datos básicos al usuario
    nombre = input(" Ingrese su nombre completo -> ")
    documento = input(" Ingrese su documento -> ")
    correo = input(" Ingrese su correo electronico -> ")
    telefono = input(" Ingrese su telefono -> ")

    # TODO: Crear diccionario con los datos ingresados
    hoja = {
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
        "telefono": telefono
    }

    # TODO: Agregar la hoja de vida a la lista
    hojas_de_vida.append(hoja)

def consultar_hojas_de_vida():
    # TODO: Mostrar encabezado de consulta
    print(" Consultando hojas de vida")

    # TODO: Verificar si hay hojas registradas
    if not hojas_de_vida:
        print(" NO hay hojas de vida registradas")
        return
    
    # TODO: Recorrer e imprimir cada hoja de vida
    for i, j in enumerate(hojas_de_vida, 1):
        print(f" {i}. {j['nombre']} - {j['documento']} - {j['correo']} - {j['telefono']}")

def actualizar_hoja_de_vida():
    # TODO: Mostrar encabezado de actualización
    print("Actualizando hoja de vida")

    # TODO: Verificar si hay hojas registradas
    if not hojas_de_vida:
        print(" No hay hojas de vida registradas")
        return

    # TODO: Mostrar la lista de hojas de vida para elegir
    for i, j in enumerate(hojas_de_vida, 1):
        print(f" {i}. {j['nombre']} - {j['documento']} - {j['correo']} - {j['telefono']}")

    # TODO: Solicitar selección de hoja a actualizar
    try:
        eligiendo_hoja_de_vida = int(input(" Escribe el numero de la hoja de vida que quiere actualizar -> "))
        if eligiendo_hoja_de_vida < 1 or eligiendo_hoja_de_vida > len(hojas_de_vida):
            print(" Selección invalida")
            return
    except ValueError:
        print("Opción no válida")
        return
    
    hoja = hojas_de_vida[eligiendo_hoja_de_vida - 1]

    # TODO: Mostrar campos disponibles para actualizar
    print("Campos disponibles para actualizar :")
    for clave in hoja.keys():
        print(f" - {clave}")

    # TODO: Solicitar campo a actualizar y su nuevo valor
    campo = input(" Escriba el campo que quiere actualizar -> ").strip()
    if campo not in hoja:
        print(" Campo no encontrado")
        return

    dato_actualizar = input(f" Escriba el nuevo valor para '{campo}': ")
    hoja[campo] = dato_actualizar

    # TODO: Confirmar que se actualizó el campo
    print(f" Campo {campo} actualizado exitosamente.")

def buscar_por_nombre():
    # TODO: Solicitar el nombre a buscar
    nombre = input(" Ingrese el nombre de la persona que desea buscar -> ").lower().strip()
    encontrados = []

    # TODO: Buscar coincidencias exactas por nombre
    for hoja in hojas_de_vida:
        if hoja["nombre"].lower() == nombre:
            encontrados.append(hoja)

    # TODO: Mostrar resultados encontrados o mensaje si no hay coincidencias
    if encontrados:
        print(" Resultados encontrados")
        for hoja in encontrados:
            print(f" Nombre : {hoja['nombre']}")
            print(f" Documento : {hoja['documento']}")
            print(f" Correo : {hoja['correo']}")
            print(f" Telefono : {hoja['telefono']}")
            print("*"*30)
    else:
        print(" No se encontraron resultados con su criterio de busquedad")

def buscar_por_documento():
    # TODO: Solicitar el documento a buscar
    documento = input(" Ingrese el documento de la persona que desea buscar -> ").strip()
    encontrados = None

    # TODO: Buscar coincidencia exacta por documento
    for hoja in hojas_de_vida:
        if hoja["documento"].lower() == documento:
            encontrados = hoja
            break

    # TODO: Mostrar resultado encontrado o mensaje si no hay coincidencia
    if encontrados:
        print("Hoja de vida encontrada")
        print(f" Nombre : {encontrados['nombre']}")
        print(f" Documento : {encontrados['documento']}")
        print(f" Correo : {encontrados['correo']}")
        print(f" Telefono : {encontrados['telefono']}")
        print("*"*30)
    else:
        print(" No se encontraron resultados con su criterio de busquedad")

# TODO: Ejecución de funciones principales para pruebas
registrar_hoja_de_vida()
buscar_por_nombre()
buscar_por_documento()
