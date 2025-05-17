hojas_de_vida = []

def registrar_hoja_de_vida():
    print(" Registro de hoja de vida")
    nombre = input(" Ingrese su nombre completo -> ")
    documento = input(" Ingrese su documento -> ")
    correo = input(" Ingrese su correo electronico -> ")
    telefono = input(" Ingrese su telefono -> ")

    hoja ={
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
        "telefono": telefono
    }

    hojas_de_vida.append(hoja)

def consultar_hojas_de_vida():
    print(" Consultando hojas de vida")
    if not hojas_de_vida:
        print(" NO hay hojas de vida registradas")
        return
    
    for i, j in enumerate(hojas_de_vida, 1):
        print(f" {i}. {j["nombre"]} - {j["documento"]} - {j["correo"]} - {j["telefono"]}")

def actualizar_hoja_de_vida():
    print("Actualizando hoja de vida")
    if not hojas_de_vida:
        print(" No hay hojas de vida registradas")
        return
    for i, j in enumerate(hojas_de_vida, 1):
        print(f" {i}. {j["nombre"]} - {j["documento"]} - {j["correo"]} - {j["telefono"]}")

    try:
        eligiendo_hoja_de_vida = int(input(" Escribe el numero de la hoja de vida que quiere actualizar -> "))
        if eligiendo_hoja_de_vida < 1 or eligiendo_hoja_de_vida > len(hojas_de_vida):
            print( "Selección invalida")
            return
    except ValueError:
        print("Opción no válida")
        return
    
    hoja = hojas_de_vida[eligiendo_hoja_de_vida - 1]

    print("Campos disponibles para actualizar :")

    for clave in hoja.keys():
        print(f" - {clave}")

    campo = input(" Escriba el campo que quiere actualizar -> ").strip()
    if campo not in hoja:
        print( "Campo no encontrado")
        return
    
    dato_actualizar = input(f" Escriba el nuevo valor para '{campo}': ")
    hoja[campo] = dato_actualizar
    print(f" Campo {campo} actualizado exitosmente.")

def buscar_por_nombre():
    nombre = input(" Ingrese el nombre de la persona que desea buscar -> ").lower().strip()
    encontrados = []

    for hoja in hojas_de_vida:
        if hoja["nombre"].lower() == nombre:
            encontrados.append(hoja)

    if encontrados:
        print(" Resultados encontrados")
        for hoja in encontrados:
            print(f" Nombre : {hoja["nombre"]}")
            print(f" Documento : {hoja["documento"]}")
            print(f" Correo : {hoja["correo"]}")
            print(f" Telefono : {hoja["telefono"]}")
            print("*"*30)
    else:
        print(" No se encontraron resultados con su criterio de busquedad")

def buscar_por_documento():
    documento = input(" Ingrese el documento de la persona que desea buscar -> ").strip()
    encontrados = None

    for hoja in hojas_de_vida:
        if hoja["documento"].lower() == documento:
            encontrados = hoja
            break

    if encontrados:
        print("Hoja de vida encontrado")
        print(f" Nombre : {encontrados["nombre"]}")
        print(f" Documento : {encontrados["documento"]}")
        print(f" Correo : {encontrados["correo"]}")
        print(f" Telefono : {encontrados["telefono"]}")
        print("*"*30)
    else:
        print(" No se encontraron resultados con su criterio de busquedad")


registrar_hoja_de_vida()
buscar_por_nombre()
buscar_por_documento()