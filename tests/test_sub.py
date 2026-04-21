"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3
    
def test_sub_resta_mayor():
    """Restar un número mayor al primero debe dar un resultado negativo."""
    assert sub(2, 5) == -3

def test_sub_cero():
    """Restar cero debe dar el mismo número."""
    assert sub(5, 0) == 5
    assert sub(0, 5) == -5
    

def test_sub_resta_negativos():
    """Restar dos números negativos."""
    assert sub(-5, -2) == -3
    assert sub(-2, -5) == 3
    # Restar un número negativo a otro negativo, ej: -5 - (-2) debe dar -3 
    

def test_sub_resta_decimales():
    """Restar dos números decimales (float)."""
    assert sub(5.5, 2.2) == 3.3
    assert sub(2.2, 5.5) == -3.3
    assert sub(5.5, 5.5) == 0
    assert sub(5.5, 2.2) == pytest.approx(3.3)
    assert sub(2.2, 5.5) == pytest.approx(-3.3)


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
