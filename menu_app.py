def agregar_compra(lista_compras, numero):
    try:
        numero_entero = int(numero)
        lista_compras.append(numero_entero)
        print(f"Compra agregada correctamente: {numero_entero}")
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")

def mostrar_compras(lista_compras):
    print("Lista de compras:", lista_compras)

def mostrar_total_gastado(lista_compras):
    total_gastado = sum(lista_compras)
    print(f"Total gastado: {total_gastado}")

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            compra = input("Ingrese el monto de la compra: ")
            agregar_compra(compras, compra)
            total_gastado = sum(compras)

        elif opcion == "2":
            mostrar_compras(compras)

        elif opcion == "3":
            mostrar_total_gastado(compras)

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()