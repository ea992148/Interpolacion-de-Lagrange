"""
Interpolación de Lagrange — Versión completa
Incluye: interpolación simple, múltiple y gráfica.
"""

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# FUNCIONES
# ============================================================

def lagrange_simple(x_points, y_points, x):
    """Interpolación de Lagrange para un solo valor."""
    n = len(x_points)
    if len(y_points) != n:
        raise ValueError("Las listas deben tener la misma longitud.")
    
    resultado = 0.0
    for j in range(n):
        lj = 1.0
        for i in range(n):
            if i != j:
                if x_points[j] == x_points[i]:
                    raise ValueError(f"Puntos duplicados en x = {x_points[j]}")
                lj *= (x - x_points[i]) / (x_points[j] - x_points[i])
        resultado += y_points[j] * lj
    return resultado


def lagrange_multiple(x_points, y_points, x_values):
    """Interpolación de Lagrange para múltiples valores."""
    x_values = np.atleast_1d(x_values)
    return np.array([lagrange_simple(x_points, y_points, x) for x in x_values])


def plot_lagrange(x_data, y_data, x_min, x_max, num_points=200,
                  punto_estimado=None, titulo='Interpolación de Lagrange',
                  xlabel='x', ylabel='y'):
    """Grafica los puntos y el polinomio de Lagrange."""
    x_plot = np.linspace(x_min, x_max, num_points)
    y_plot = lagrange_multiple(x_data, y_data, x_plot)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, 'o', label='Puntos medidos',
             markersize=10, color='blue', zorder=5)
    plt.plot(x_plot, y_plot, '-', label='Polinomio de Lagrange',
             color='red', linewidth=2)
    
    if punto_estimado is not None:
        x_est, y_est = punto_estimado
        plt.axvline(x=x_est, color='green', linestyle='--', alpha=0.5)
        plt.axhline(y=y_est, color='green', linestyle='--', alpha=0.5)
        plt.plot(x_est, y_est, 's', color='green', markersize=12,
                 label=f'Estimación: ({x_est}, {y_est:.2f})', zorder=6)
    
    plt.title(titulo, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":
    # Datos
    rpm_data = np.array([1500, 2500, 3500, 4500])
    torque_data = np.array([180, 220, 210, 170])
    
    # 1. Interpolación simple
    print("=" * 55)
    print("1. INTERPOLACIÓN SIMPLE")
    print("=" * 55)
    rpm_obj = 3000
    tq = lagrange_simple(rpm_data, torque_data, rpm_obj)
    print(f"Torque a {rpm_obj} RPM: {tq:.2f} Nm")
    
    # 2. Interpolación múltiple
    print("\n" + "=" * 55)
    print("2. INTERPOLACIÓN MÚLTIPLE")
    print("=" * 55)
    rpm_range = np.arange(1500, 4501, 500)
    torques = lagrange_multiple(rpm_data, torque_data, rpm_range)
    print(f"\n{'RPM':>6} | {'Torque (Nm)':>12}")
    print("-" * 25)
    for r, t in zip(rpm_range, torques):
        print(f"{r:>6} | {t:>12.2f}")
    
    # 3. Gráfica
    print("\n" + "=" * 55)
    print("3. GRÁFICA")
    print("=" * 55)
    print("Generando gráfica...")
    plot_lagrange(
        x_data=rpm_data,
        y_data=torque_data,
        x_min=1400,
        x_max=4600,
        punto_estimado=(rpm_obj, tq),
        titulo='Curva de Torque del Motor — Interpolación de Lagrange',
        xlabel='RPM',
        ylabel='Torque (Nm)'
    )
