"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12

def test_mul_por_cero():
    """Multiplicar por cero debe dar cero."""
    assert mul(5, 0) == 0
    assert mul(0, 5) == 0
    assert mul(0, 0) == 0

def test_mul_negativos():
    """Multiplicar dos números negativos debe dar un resultado positivo."""
    assert mul(-2, -3) == 6

def test_mul_positivo_negativo():
    """Multiplicar un número positivo por uno negativo debe dar un resultado negativo."""
    assert mul(4, -5) == -20
    assert mul(-4, 5) == -20

def test_mul_por_uno():
    """Multiplicar por 1 debe dar el mismo número."""
    assert mul(5, 1) == 5
    assert mul(1, 5) == 5

def test_mul_decimales():
    """Multiplicar dos números decimales debe dar un resultado decimal."""
    assert mul(1.5, 2.5) == 3.75

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (5, 0, 0),
    (0, 5, 0),
    (0, 0, 0),
    (-2, -3, 6),
    (4, -5, -20),
    (-4, 5, -20),
    (5, 1, 5),
    (1, 5, 5),
    (1.5, 2.5, 3.75)
])
def test_mul_parametrizado(a, b, expected):
    assert mul(a, b) == expected

# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
