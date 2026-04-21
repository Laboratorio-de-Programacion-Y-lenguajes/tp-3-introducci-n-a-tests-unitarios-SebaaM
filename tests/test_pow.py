"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8

def test_pow_exponente_cero():
    """Cualquier número elevado a 0 debe dar 1."""
    assert pow_(5, 0) == 1
    assert pow_(-3, 0) == 1
    assert pow_(0, 0) == 1

def test_pow_exponente_uno():
    """Cualquier número elevado a 1 debe dar el mismo número."""
    assert pow_(5, 1) == 5
    assert pow_(-3, 1) == -3
    
def test_pow_base_negativa_exponente_par():
    """Base negativa con exponente par debe dar un resultado positivo."""
    assert pow_(-2, 4) == 16

def test_pow_exponente_decimal():
    """Exponente decimal, ej: 9 ** 0.5 debe dar 3.0."""
    assert pow_(9, 0.5) == 3.0




# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
