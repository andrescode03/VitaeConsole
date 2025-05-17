# Lista principal donde se almacenarán las hojas de vida como diccionarios
hojas_de_vida = []

# Función para registrar una nueva hoja de vida
def registrar_hoja_de_vida():
    print(" Registro de hoja de vida")

    # Solicita al usuario los datos básicos
    nombre = input(" Ingrese su nombre completo -> ")
    documento = input(" Ingrese su documento -> ")
    correo = input(" Ingrese su correo electronico -> ")
    telefono = input(" Ingrese su telefono -> ")

    # Crea un diccionario con los datos y lo agrega a la lista
    hoja = {
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
        "telefono": telefono
    }

    hojas_de_vida.append(hoja)
    print(" Hoja de vida registrada exitosamente.\n")

# Función para mostrar todas las hojas de vida registradas
def consultar_hojas_de_vida():
    print(" Consultando hojas de vida")

    # Verifica si hay registros
    if not hojas_de_vida:
        print(" NO hay hojas de vida registradas\n")
        return
    
    # Recorre e imprime cada hoja con su índice
    for i, j in enumerate(hojas_de_vida, 1):
        print(f" {i}. {j['nombre']} - {j['documento']} - {j['correo']} - {j['telefono']}")
    print()

# Función para actualizar los datos de una hoja de vida
def actualizar_hoja_de_vida():
    print("Actualizando hoja de vida")

    # Verifica si hay registros
    if not hojas_de_vida:
        print(" No hay hojas de vida registradas\n")
        return

    # Muestra la lista con índices para elegir
    for i, j in enumerate(hojas_de_vida, 1):
        print(f" {i}. {j['nombre']} - {j['documento']} - {j['correo']} - {j['telefono']}")

    # Solicita el número de hoja a actualizar y valida entrada
    try:
        eligiendo_hoja_de_vida = int(input(" Escribe el numero de la hoja de vida que quiere actualizar -> "))
        if eligiendo_hoja_de_vida < 1 or eligiendo_hoja_de_vida > len(hojas_de_vida):
            print(" Selección invalida\n")
            return
    except ValueError:
        print(" Opción no válida\n")
        return
    
    hoja = hojas_de_vida[eligiendo_hoja_de_vida - 1]

    # Muestra los campos que se pueden modificar
    print("Campos disponibles para actualizar:")
    for clave in hoja.keys():
        print(f" - {clave}")

    # Solicita el campo a modificar y su nuevo valor
    campo = input(" Escriba el campo que quiere actualizar -> ").strip()
    if campo not in hoja:
        print(" Campo no encontrado\n")
        return

    dato_actualizar = input(f" Escriba el nuevo valor para '{campo}': ")
    hoja[campo] = dato_actualizar
    print(f" Campo {campo} actualizado exitosamente.\n")

# Función para buscar hojas de vida por nombre exacto
def buscar_por_nombre():
    nombre = input(" Ingrese el nombre de la persona que desea buscar -> ").lower().strip()
    encontrados = []

    # Recorre y almacena coincidencias exactas
    for hoja in hojas_de_vida:
        if hoja["nombre"].lower() == nombre:
            encontrados.append(hoja)

    # Imprime resultados o notifica si no hay
    if encontrados:
        print(" Resultados encontrados")
        for hoja in encontrados:
            print(f" Nombre : {hoja['nombre']}")
            print(f" Documento : {hoja['documento']}")
            print(f" Correo : {hoja['correo']}")
            print(f" Telefono : {hoja['telefono']}")
            print("*" * 30)
        print()
    else:
        print(" No se encontraron resultados con su criterio de busquedad\n")

# Función para buscar por número de documento
def buscar_por_documento():
    documento = input(" Ingrese el documento de la persona que desea buscar -> ").strip()
    encontrados = None

    # Busca la primera coincidencia exacta
    for hoja in hojas_de_vida:
        if hoja["documento"].lower() == documento:
            encontrados = hoja
            break

    # Muestra los datos si se encuentra o notifica si no
    if encontrados:
        print("Hoja de vida encontrada")
        print(f" Nombre : {encontrados['nombre']}")
        print(f" Documento : {encontrados['documento']}")
        print(f" Correo : {encontrados['correo']}")
        print(f" Telefono : {encontrados['telefono']}")
        print("*" * 30 + "\n")
    else:
        print(" No se encontraron resultados con su criterio de busquedad\n")

# Función para eliminar una hoja de vida
def eliminar_hoja_de_vida():
    print("Eliminando hoja de vida")

    # Verifica si hay registros
    if not hojas_de_vida:
        print(" No hay hojas de vida registradas\n")
        return

    # Muestra la lista con índices
    for i, j in enumerate(hojas_de_vida, 1):
        print(f" {i}. {j['nombre']} - {j['documento']} - {j['correo']} - {j['telefono']}")

    # Solicita la hoja a eliminar y valida entrada
    try:
        seleccion = int(input(" Escribe el número de la hoja de vida que deseas eliminar -> "))
        if seleccion < 1 or seleccion > len(hojas_de_vida):
            print(" Selección inválida\n")
            return
    except ValueError:
        print(" Entrada no válida\n")
        return

    hoja_eliminada = hojas_de_vida.pop(seleccion - 1)
    print(f" Hoja de vida de {hoja_eliminada['nombre']} eliminada exitosamente.\n")

# Función principal que muestra el menú interactivo
def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Registrar hoja de vida")
        print("2. Consultar hojas de vida")
        print("3. Actualizar hoja de vida")
        print("4. Buscar por nombre")
        print("5. Buscar por documento")
        print("6. Eliminar hoja de vida")
        print("7. Salir")

        # Captura la opción elegida por el usuario
        opcion = input("Seleccione una opción -> ")

        # Ejecuta la función correspondiente
        if opcion == '1':
            registrar_hoja_de_vida()
        elif opcion == '2':
            consultar_hojas_de_vida()
        elif opcion == '3':
            actualizar_hoja_de_vida()
        elif opcion == '4':
            buscar_por_nombre()
        elif opcion == '5':
            buscar_por_documento()
        elif opcion == '6':
            eliminar_hoja_de_vida()
        elif opcion == '7':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# Inicia el sistema mostrando el menú
menu()

