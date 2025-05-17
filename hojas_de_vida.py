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
    if not hojas_de_vida

