class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for producto in self.productos.values():
            print(f"{producto.nombre} | Precio: ${producto.precio} | Stock: {producto.stock}")

    def obtener_producto(self, nombre):
        return self.productos.get(nombre)


class Venta:
    def __init__(self):
        self.items = {}

    def agregar_producto(self, producto, cantidad):
        if producto.reducir_stock(cantidad):
            self.items[producto.nombre] = {
                "precio": producto.precio,
                "cantidad": cantidad
            }
            return True
        print("Stock insuficiente.")
        return False

    def calcular_total(self):
        total = 0
        for item in self.items.values():
            total += item["precio"] * item["cantidad"]
        return total


class Pago:
    def __init__(self, monto):
        self.monto = monto

    def procesar_pago(self):
        print(f"\nPago realizado correctamente por ${self.monto}")


def main():
    inventario = Inventario()

    inventario.agregar_producto(Producto("Arroz", 1.50, 50))
    inventario.agregar_producto(Producto("Azúcar", 1.20, 40))
    inventario.agregar_producto(Producto("Aceite", 3.80, 30))

    inventario.mostrar_productos()

    venta = Venta()

    while True:
        nombre = input("\nIngrese el nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break

        producto = inventario.obtener_producto(nombre)
        if not producto:
            print("Producto no encontrado.")
            continue

        cantidad = int(input("Ingrese la cantidad: "))
        venta.agregar_producto(producto, cantidad)

    total = venta.calcular_total()
    print(f"\nTotal a pagar: ${total}")

    pago = Pago(total)
    pago.procesar_pago()


if __name__ == "__main__":
    main()
