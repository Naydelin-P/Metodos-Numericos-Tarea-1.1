#   Codigo que implementa el calculo de errores
#   en operaciones numericas
# 
#           Autor:
#  Naydelin Palomo Martinez
#   naydelin.palomo.270602@gmail.com
#
#

import matplotlib.pyplot as plt
import numpy as np

# Función para los errores
def calcular_errores(x, y, valor_real):
    diferencia = x - y
    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    error_cuad = error_abs ** 2
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    print(f"Error cuadrático: {error_cuad}")
    return error_abs, error_rel, error_pct, error_cuad

# Valores
valores = [
    (1.0000001, 1.0000000, 0.0000001),
    (1.000000000000001, 1.000000000000000, 0.000000000000001)
]

# lista de los errores
errores_abs = []
errores_rel = []
errores_pct = []
errores_cuad = []

# errores para los valores
for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    error_abs, error_rel, error_pct, error_cuad = calcular_errores(x, y, real)
    errores_abs.append(error_abs)
    errores_rel.append(error_rel)
    errores_pct.append(error_pct)
    errores_cuad.append(error_cuad)

# figura con subplots  figura y uno (o varios) conjunto de ejes
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Gráfico de barras para los errores
axs[0, 0].bar([1, 2], errores_abs, color='blue', label='Error absoluto')
axs[0, 0].set_xticks([1, 2])
axs[0, 0].set_xticklabels(['Caso 1', 'Caso 2'])
axs[0, 0].set_ylabel('Error')
axs[0, 0].set_title('Error Absoluto')
axs[0, 0].grid(True)

axs[0, 1].bar([1, 2], errores_rel, color='red', label='Error relativo')
axs[0, 1].set_xticks([1, 2])
axs[0, 1].set_xticklabels(['Caso 1', 'Caso 2'])
axs[0, 1].set_ylabel('Error')
axs[0, 1].set_title('Error Relativo')
axs[0, 1].grid(True)

axs[1, 0].bar([1, 2], errores_pct, color='green', label='Error porcentual')
axs[1, 0].set_xticks([1, 2])
axs[1, 0].set_xticklabels(['Caso 1', 'Caso 2'])
axs[1, 0].set_ylabel('Error (%)')
axs[1, 0].set_title('Error Porcentual')
axs[1, 0].grid(True)

axs[1, 1].bar([1, 2], errores_cuad, color='purple', label='Error cuadrático')
axs[1, 1].set_xticks([1, 2])
axs[1, 1].set_xticklabels(['Caso 1', 'Caso 2'])
axs[1, 1].set_ylabel('Error')
axs[1, 1].set_title('Error Cuadrático')
axs[1, 1].grid(True)

# Ajusta el espacio de los ejes
plt.tight_layout()

# Muestra los graficos
plt.show()
