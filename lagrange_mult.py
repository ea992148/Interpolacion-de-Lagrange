"""
Interpolación de Lagrange para MÚLTIPLES valores de x.
"""

import numpy as np


def lagrange_simple(x_points, y_points, x):
    """
    Calcula el valor interpolado en x usando el método de Lagrange.
    (Función auxiliar para un solo valor)
    """
    n = len(x_points)
    
    if len(y_points) != n:
        raise ValueError("Las listas x_points e y_points deben tener la misma longitud.")
    
    resultado = 0.0
    
    for j in range(n):
        lj = 1.0
        for i in range(n):
            if i != j:
                if x_points[j] == x_points[i]:
                    raise ValueError(f"Puntos x duplicados: x[{j}] = x[{i}] = {x_points[j]}")
                lj *= (x - x_points[i]) / (x_points[j] - x_points[i])
        resultado += y_points[j] * lj
    
    return resultado


def lagrange_multiple(x_points, y_points, x_values):
    """
    Calcula los valores interpolados para varios valores de x.
    
    Parámetros:
    -----------
    x_points : list or np.array
        Coordenadas x de los puntos conocidos.
    y_points : list or np.array
        Coordenadas y de los puntos conocidos.
    x_values : list or np.array
        Valores de x donde se quiere interpolar.
    
    Retorna:
    --------
    np.array : Valores interpolados en cada x_values.
    """
    x_values = np.atleast_1d(x_values)
    resultados = np.zeros_like(x_values, dtype=float)
    
    for k, x in enumerate(x_values):
        resultados[k] = lagrange_simple(x_points, y_points, x)
    
    return resultados


# ============================================================
# EJEMPLO DE USO
# ============================================================
if __name__ == "__main__":
    # Datos del banco de pruebas
    rpm_data = np.array([1500, 2500, 3500, 4500])
    torque_data = np.array([180, 220, 210, 170])
    
    # Estimar torque en varios puntos
    rpm_range = np.arange(1500, 4501, 250)
    torques = lagrange_multiple(rpm_data, torque_data, rpm_range)
    
    print("=" * 50)
    print("INTERPOLACIÓN MÚLTIPLE DE LAGRANGE")
    print("=" * 50)
    print(f"\n{'RPM':>6} | {'Torque (Nm)':>12}")
    print("-" * 25)
    for rpm, tq in zip(rpm_range, torques):
        print(f"{rpm:>6} | {tq:>12.2f}")
    print("=" * 50)
