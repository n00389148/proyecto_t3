"""Pruebas unitarias del Modelo."""
import pytest

from modelo.calculadora_modelo import CalculadoraModelo


@pytest.fixture
def modelo():
    return CalculadoraModelo()


def test_sumar(modelo):
    assert modelo.sumar(2, 3) == 5


def test_restar(modelo):
    assert modelo.restar(10, 4) == 6


def test_multiplicar(modelo):
    assert modelo.multiplicar(3, 4) == 12


def test_dividir(modelo):
    assert modelo.dividir(10, 2) == 5


def test_dividir_entre_cero(modelo):
    with pytest.raises(ValueError):
        modelo.dividir(10, 0)
