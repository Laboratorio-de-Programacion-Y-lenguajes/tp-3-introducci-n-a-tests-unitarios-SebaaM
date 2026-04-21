"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0

def test_mean_lista_un_elemento():
    """El promedio de una lista con un solo elemento debe ser ese mismo elemento."""
    assert mean([5]) == 5.0

def test_mean_lista_negativos():
    """El promedio de una lista con números negativos debe ser negativo."""
    assert mean([-1, -2, -3]) == -2.0

def test_mean_lista_decimales():
    """El promedio de una lista con números decimales debe ser decimal."""
    assert mean([1.5, 2.5, 3.5]) == 2.5

def test_mean_lista_vacia():
    with pytest.raises(ValueError):
        mean([])


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])
