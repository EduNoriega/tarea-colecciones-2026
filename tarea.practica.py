# Universidad Estatal Amazonica - UEA
# Estudiante: Eduardo Luis Noriega Peñafiel
# Codigo: 2626-UEA-L-UFB-026-C - Paralelo: C
# Tarea Practica Semana 15: Colecciones de datos

# PROBLEMA DE LA VIDA REAL: Guardar frutas sin repetir usando un conjunto

# 1. CREACION DE LA COLECCION (conjunto no permite duplicados)
frutas = {"manzana", "pera", "banana", "uva", "mango", "kiwi"}

# 2. MOSTRAR INFORMACION DE FORMA CLARA - incluye recorrer elementos
def mostrar_frutas():
    print("\n--- Frutas registradas sin repetir ---")
    if not frutas:
        print("No hay frutas registradas")
    else:
        for i, fruta in enumerate(frutas, start=1):
            print(f"{i}. {fruta}")
        print(f"Total: {len(frutas)} frutas diferentes")

# 3. INSERTAR / AGREGAR DATOS
def agregar_fruta():
    nombre = input("Ingresa el nombre de la fruta nueva: ").lower()
    if nombre in frutas:
        print(f"'{nombre}' ya existe, no se permite repetir")
    else:
        frutas.add(nombre)
        print(f"'{nombre}' agregada correctamente")

# 4. OPERACION BASICA: BUSCAR
def buscar_fruta():
    nombre = input("Nombre de la fruta a buscar: ").lower()
    if nombre in frutas:
        print(f"SI tenemos {nombre}")
    else:
        print(f"NO tenemos {nombre}")

# 5. OPERACION BASICA: ELIMINAR
def eliminar_fruta():
    mostrar_frutas()
    nombre = input("Nombre de la fruta a eliminar: ").lower()
    if nombre in frutas:
        frutas.remove(nombre)
        print(f"'{nombre}' eliminada")
    else:
        print(f"'{nombre}' no existe")

# PROGRAMA PRINCIPAL
while True:
    print("\n1. Agregar | 2. Mostrar | 3. Buscar | 4. Eliminar | 5. Salir")
    opcion = input("Elige una opcion (1-5): ")

    if opcion == "1":
        agregar_fruta()
    elif opcion == "2":
        mostrar_frutas()
    elif opcion == "3":
        buscar_fruta()
    elif opcion == "4":
        eliminar_fruta()
    elif opcion == "5":
        print("Programa finalizado - 2626-UEA-L-UFB-026-C")
        break
    else:
        print("Opcion no valida")