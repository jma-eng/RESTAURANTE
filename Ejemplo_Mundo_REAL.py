# Sistema de Restaurante
# Caso del mundo real: Cliente escoge su pedido y paga (efectivo o tarjeta)
# Programación Orientada a Objetos (POO)

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []

    def agregar_plato(self, plato):
        self.menu.append(plato)

    def mostrar_menu(self):
        print(f"\n--- Menú del {self.nombre} ---")
        for i, plato in enumerate(self.menu, start=1):
            print(f"{i}. {plato.nombre} - ${plato.precio}")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def pagar_efectivo(self, total):
        while True:
            monto = float(input("\nIngrese el monto entregado: $"))
            if monto >= total:
                cambio = monto - total
                print(f"Pago realizado con éxito.")
                print(f"Cambio a devolver: ${cambio}")
                break
            else:
                print("Monto insuficiente. Intente nuevamente.")

    def pagar_tarjeta(self, total):
        fondos = float(input("\nIngrese el saldo disponible en su tarjeta: $"))
        if fondos >= total:
            print(f"Pago aprobado por ${total}.")
            print("Compra finalizada. ¡Gracias por su visita!")
        else:
            print("❌ No tiene fondos suficientes. No se puede realizar el pedido.")


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.platos = []

    def agregar_plato(self, plato):
        self.platos.append(plato)
        print(f"✔ {plato.nombre} agregado al pedido")

    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)

    def mostrar_resumen(self):
        print(f"\n--- Resumen del pedido de {self.cliente.nombre} ---")
        for plato in self.platos:
            print(f"- {plato.nombre}: ${plato.precio}")
        print(f"Total a pagar: ${self.calcular_total()}")


# -------- PROGRAMA PRINCIPAL --------

# Crear restaurante
restaurante = Restaurante("Restaurante Python")

# Agregar platos al menú
restaurante.agregar_plato(Plato("Hamburguesa", 8.50))
restaurante.agregar_plato(Plato("Pizza", 10.00))
restaurante.agregar_plato(Plato("Ensalada", 6.00))
restaurante.agregar_plato(Plato("Jugo Natural", 3.00))

# Datos del cliente
nombre = input("Ingrese su nombre: ")
cliente = Cliente(nombre)
pedido = Pedido(cliente)

# Selección de platos
while True:
    restaurante.mostrar_menu()
    opcion = input("\nSeleccione el número del plato: ")

    if opcion.isdigit() and 1 <= int(opcion) <= len(restaurante.menu):
        plato = restaurante.menu[int(opcion) - 1]
        pedido.agregar_plato(plato)
    else:
        print("❌ Opción inválida")
        continue

    continuar = input("\n¿Desea agregar más platos? (s/n): ").lower()
    if continuar != "s":
        break

# Mostrar resumen del pedido
pedido.mostrar_resumen()

# Selección del método de pago
print("\nMétodo de pago:")
print("1. Efectivo")
print("2. Tarjeta")

opcion_pago = input("Seleccione una opción: ")
total = pedido.calcular_total()

if opcion_pago == "1":
    cliente.pagar_efectivo(total)
    print("Compra finalizada. ¡Gracias por su compra!")
elif opcion_pago == "2":
    cliente.pagar_tarjeta(total)
else:
    print("❌ Opción de pago no válida")
