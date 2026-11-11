"""Controlador: conecta el modelo con la vista."""
from modelo.calculadora_modelo import CalculadoraModelo
from vista.calculadora_vista import CalculadoraVista


class CalculadoraControlador:
    """Recibe las peticiones, usa el modelo y actualiza la vista."""

    def __init__(self, modelo=None, vista=None):
        self.modelo = modelo or CalculadoraModelo()
        self.vista = vista or CalculadoraVista()

    def calcular(self, operacion, a, b):
        """Ejecuta una operacion y envia el resultado a la vista."""
        operaciones = {
            "+": self.modelo.sumar,
            "-": self.modelo.restar,
            "*": self.modelo.multiplicar,
            "/": self.modelo.dividir,
        }
        if operacion not in operaciones:
            self.vista.mostrar_error(f"Operacion '{operacion}' no valida")
            return None
        try:
            resultado = operaciones[operacion](a, b)
        except ValueError as error:
            self.vista.mostrar_error(str(error))
            return None
        self.vista.mostrar_resultado(operacion, a, b, resultado)
        return resultado

    def ejecutar(self):
        """Ejecuta una demostracion de la calculadora."""
        self.vista.mostrar_titulo()
        self.calcular("+", 10, 5)
        self.calcular("-", 10, 5)
        self.calcular("*", 10, 5)
        self.calcular("/", 10, 5)
        self.calcular("/", 10, 0)
