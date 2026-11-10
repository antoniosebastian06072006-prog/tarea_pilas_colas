from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero.")


def leer_pasajero():
    numero = leer_entero("  Número de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Danna", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "lupe", "0934567890", 16, "2026-11-20", "PERU", "07B"),
        Pasajero(1001, "nicolas", "0901234567", 41, "2026-11-22", "ESPAÑA", "01A")
    ]


def cargar_pruebas(estructura, metodo_entrada):
    cargados = 0
    for pasajero in datos_prueba():
        if metodo_entrada(pasajero):
            cargados = cargados + 1
    print(f"  Se cargaron {cargados} pasajeros de prueba.")


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 - PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  Pasajero apilado correctamente.")
        elif op == "2":
            pila.listar()
        elif op == "3":
            pasajero = pila.desapilar()
            if pasajero is not None:
                print("  Salió:", pasajero)
                tope = pila.ver_tope()
                if tope is not None:
                    print("  Nuevo tope:", tope)
        elif op == "4":
            pasajero = pila.ver_tope()
            if pasajero is None:
                print("  La pila está vacía.")
            else:
                print("  Tope:", pasajero)
        elif op == "5":
            numero = leer_entero("  Número que desea buscar: ")
            posicion = pila.buscar(numero)
            if posicion == -1:
                print("  No existe ese pasajero.")
            else:
                print(f"  Encontrado en [{posicion}]: {pila.datos[posicion]}")
        elif op == "6":
            numero = leer_entero("  Número del pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  No existe ese pasajero.")
        elif op == "7":
            numero = leer_entero("  Número que desea eliminar: ")
            if pila.eliminar_por_numero(numero):
                print("  Pasajero eliminado.")
            else:
                print("  No existe ese pasajero.")
        elif op == "8":
            copia = pila.copiar()
            print("  Copia de la pila:")
            copia.listar()
        elif op == "9":
            print("  Longitud:", pila.longitud())
            print("  ¿Está vacía?", "Sí" if pila.esta_vacia() else "No")
        elif op == "C":
            cargar_pruebas(pila, pila.apilar)
        elif op == "0":
            break
        else:
            print("  Opción no válida.")


def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 - COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  Pasajero encolado correctamente.")
        elif op == "2":
            cola.listar()
        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero is not None:
                print("  Salió:", pasajero)
                frente = cola.ver_frente()
                if frente is not None:
                    print("  Nuevo frente:", frente)
        elif op == "4":
            pasajero = cola.ver_frente()
            if pasajero is None:
                print("  La cola está vacía.")
            else:
                print("  Frente:", pasajero)
        elif op == "5":
            numero = leer_entero("  Número que desea buscar: ")
            posicion = cola.buscar(numero)
            if posicion == -1:
                print("  No existe ese pasajero.")
            else:
                print(f"  Encontrado en [{posicion}]: {cola.datos[posicion]}")
        elif op == "6":
            numero = leer_entero("  Número del pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(numero, destino, asiento):
                print("  Pasajero modificado correctamente.")
            else:
                print("  No existe ese pasajero.")
        elif op == "7":
            numero = leer_entero("  Número que desea eliminar: ")
            if cola.eliminar_por_numero(numero):
                print("  Pasajero eliminado.")
            else:
                print("  No existe ese pasajero.")
        elif op == "8":
            copia = cola.copiar()
            print("  Copia de la cola:")
            copia.listar()
        elif op == "9":
            print("  Longitud:", cola.longitud())
            print("  ¿Está vacía?", "Sí" if cola.esta_vacia() else "No")
        elif op == "C":
            cargar_pruebas(cola, cola.encolar)
        elif op == "0":
            break
        else:
            print("  Opción no válida.")


def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS - PASAJEROS =====")
        print("1. Menú 1 - Pila")
        print("2. Menú 2 - Cola")
        print("3. Salir")
        op = input("Opción: ").strip()

        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
