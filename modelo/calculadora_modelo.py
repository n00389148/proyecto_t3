"""Modelo: contiene la logica de negocio de la calculadora."""


class CalculadoraModelo:
    """Realiza las operaciones matematicas basicas."""

    def sumar(self, a, b):
        """Retorna la suma de dos numeros."""
        return a + b

    def restar(self, a, b):
        """Retorna la resta de dos numeros."""
        return a - b

    def multiplicar(self, a, b):
        """Retorna el producto de dos numeros."""
        return a * b

    def dividir(self, a, b):
        """Retorna la division de dos numeros."""
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b
