"""
Visualización del polinomio de Lagrange con matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt


def lagrange_simple(x_points, y_points, x):
    """Interpolación de Lagrange para un solo valor."""
    n = len(x_points)
    resultado = 0.0
    for j in range(n):
        lj = 1.0
        for i in range(n):
            if i != j:
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
    """
    Grafica los puntos originales y el polinomio de Lagrange.
    
    Parámetros:
    -----------
    x_data : list or np.array
        Coordenadas x de los puntos de datos.
    y_data : list or np.array
        Coordenadas y de los puntos de datos.
    x_min : float
        Inicio del rango de x para graficar.
    x_max : float
        Fin del rango de x para graficar.
    num_points : int
        Número de puntos para evaluar el polinomio.
    punto_estimado : tuple or None
        (x, y) del punto estimado a marcar en la gráfica.
    titulo : str
        Título de la gráfica.
    xlabel : str
        Etiqueta del eje x.
    ylabel : str
        Etiqueta del eje y.
    """
    # Generar puntos para la curva
    x_plot = np.linspace(x_min, x_max, num_points)
    y_plot = lagrange_multiple(x_data, y_data, x_plot)
    
    # Crear figura
    plt.figure(figsize=(10, 6))
    
    # Puntos originales
    plt.plot(x_data, y_data, 'o', 
             label='Puntos medidos', 
             markersize=10, 
             color='blue', 
             zorder=5)
    
    # Polinomio de Lagrange
    plt.plot(x_plot, y_plot, '-', 
             label='Polinomio de Lagrange', 
             color='red', 
             linewidth=2)
    
    # Punto estimado (opcional)
    if punto_estimado is not None:
        x_est, y_est = punto_estimado
        plt.axvline(x=x_est, color='green', linestyle='--', alpha=0.5)
        plt.axhline(y=y_est, color='green', linestyle='--', alpha=0.5)
        plt.plot(x_est, y_est, 's', 
                 color='green', 
                 markersize=12,
                 label=f'Estimación: ({x_est}, {y_est:.2f})',
                 zorder=6)
    
    # Configuración
    plt.title(titulo, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()


# ============================================================
# EJEMPLO DE USO
# ============================================================
if __name__ == "__main__":
    # Datos del banco de pruebas
    rpm_data = np.array([1500, 2500, 3500, 4500])
    torque_data = np.array([180, 220, 210, 170])
    
    # Punto a estimar
    rpm_objetivo = 3000
    torque_estimado = lagrange_simple(rpm_data, torque_data, rpm_objetivo)
    
    print("=" * 50)
    print("GRÁFICA DE INTERPOLACIÓN DE LAGRANGE")
    print("=" * 50)
    print(f"Datos: {list(zip(rpm_data, torque_data))}")
    print(f"Torque estimado a {rpm_objetivo} RPM: {torque_estimado:.2f} Nm")
    print("=" * 50)
    
    # Graficar
    plot_lagrange(
        x_data=rpm_data,
        y_data=torque_data,
        x_min=1400,
        x_max=4600,
        punto_estimado=(rpm_objetivo, torque_estimado),
        titulo='Curva de Torque del Motor — Interpolación de Lagrange',
        xlabel='RPM',
        ylabel='Torque (Nm)'
    )
