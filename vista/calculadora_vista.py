"""Vista: se encarga de mostrar la informacion al usuario."""


class CalculadoraVista:
    """Muestra los resultados de la calculadora en consola."""

    def mostrar_titulo(self):
        """Imprime el titulo de la aplicacion."""
        print("=== Calculadora MVC - Examen T3 ===")

    def mostrar_resultado(self, operacion, a, b, resultado):
        """Imprime el resultado de una operacion."""
        print(f"{a} {operacion} {b} = {resultado}")

    def mostrar_error(self, mensaje):
        """Imprime un mensaje de error."""
        print(f"Error: {mensaje}")
