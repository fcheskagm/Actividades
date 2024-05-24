''' Clase Cuenta que tendra de atributo titular(obligatorio), cantidad(decimal y opcional), constuir metodos para la clase, 1 constructor donde los datos pueden estar vacios, 2 los set y get de cada atributo, 
no se deben modificar los atributos manualmente solo retirando e ingresando, 3 mostrar datos de la cuenta, 4 se ingresa cantidad a la cuenta si es negativa no pasa nada, si se retira una cantidad a la cuenta 
mayor quedaria en numero negativos'''

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular_nuevo):
        self.titular = titular_nuevo

    def get_titular(self):
        return self.titular

    def set_cantidad(self, cantidad_nueva):
        if cantidad_nueva >= 0:
            self.cantidad = cantidad_nueva

    def get_cantidad(self):
        return self.cantidad

    def mostrar_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad += cantidad
        else:
            self.cantidad = self.cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad
        
mi_cuenta = Cuenta("Juan Pérez", 100.0)
mi_cuenta.mostrar_datos()

mi_cuenta.ingresar(50.0)
mi_cuenta.mostrar_datos()

mi_cuenta.retirar(300.0)
mi_cuenta.mostrar_datos() 