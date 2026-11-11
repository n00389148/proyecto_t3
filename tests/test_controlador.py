"""Pruebas unitarias del Controlador."""
from controlador.calculadora_controlador import CalculadoraControlador


def test_calcular_suma(capsys):
    controlador = CalculadoraControlador()
    assert controlador.calcular("+", 2, 3) == 5
    assert "2 + 3 = 5" in capsys.readouterr().out


def test_calcular_division_entre_cero(capsys):
    controlador = CalculadoraControlador()
    assert controlador.calcular("/", 10, 0) is None
    assert "No se puede dividir entre cero" in capsys.readouterr().out


def test_operacion_no_valida(capsys):
    controlador = CalculadoraControlador()
    assert controlador.calcular("%", 10, 3) is None
    assert "no valida" in capsys.readouterr().out
