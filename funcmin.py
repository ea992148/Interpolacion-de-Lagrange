"""
Interpolación de Lagrange para UN solo valor de x.
"""

def lagrange_simple(x_points, y_points, x):
    """
    Calcula el valor interpolado en x usando el método de Lagrange.
    
    Parámetros:
    -----------
    x_points : list
        Coordenadas x de los puntos conocidos.
    y_points : list
        Coordenadas y de los puntos conocidos.
    x : float
        Valor de x donde se quiere interpolar.
    
    Retorna:
    --------
    float : Valor interpolado en x.
    """
    n = len(x_points)
    
    # Verificar que las listas tengan el mismo tamaño
    if len(y_points) != n:
        raise ValueError("Las listas x_points e y_points deben tener la misma longitud.")
    
    resultado = 0.0
    
    for j in range(n):
        # Calcular el polinomio base l_j(x)
        lj = 1.0
        for i in range(n):
            if i != j:
                # Evitar división por cero
                if x_points[j] == x_points[i]:
                    raise ValueError(f"Puntos x duplicados: x[{j}] = x[{i}] = {x_points[j]}")
                lj *= (x - x_points[i]) / (x_points[j] - x_points[i])
        
        # Sumar y_j * l_j(x)
        resultado += y_points[j] * lj
    
    return resultado


# ============================================================
# EJEMPLO DE USO
# ============================================================
if __name__ == "__main__":
    # Datos del PDF: Torque vs RPM
    rpm = [1000, 1500, 2000]
    torque = [80, 95, 110]
    
    # Estimar torque a 1750 RPM
    x_objetivo = 1750
    resultado = lagrange_simple(rpm, torque, x_objetivo)
    
    print("=" * 50)
    print("INTERPOLACIÓN SIMPLE DE LAGRANGE")
    print("=" * 50)
    print(f"Datos: {list(zip(rpm, torque))}")
    print(f"Valor a estimar: {x_objetivo} RPM")
    print(f"Resultado: {resultado:.4f} Nm")
    print("=" * 50)
