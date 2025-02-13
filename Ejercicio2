#   Codigo que implementa un esquema numerico 
#   para determinar la aproximacion de Leibniz
# 
#           Autor:
#  Naydelin Palomo Martinez
#   naydelin.palomo.270602@gmail.com
#

import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n)) #serie de Leibniz con n términos.

# valores y errores
true_pi = np.pi
N_values = [10, 100, 1000, 10000]
errors_abs = []
errors_rel = []
errors_cuad = []

# calcula los errores
import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi(n):
    #Calcula una aproximación de pi 
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

# 2 V y E
true_pi = np.pi
N_values = [10, 100, 1000, 10000]
errors_abs = []
errors_rel = []
errors_cuad = []

# Evalua errores 
for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    error_cuad = error_abs**2
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_cuad.append(error_cuad)
    print(f"N={N}: Error absoluto={error_abs:.6e}, Error relativo={error_rel:.6e}, Error cuadrático={error_cuad:.6e}")

# Grafica
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(N_values, errors_abs, label='Error absoluto', marker='o', linestyle='--', color='blue')
ax.plot(N_values, errors_rel, label='Error relativo', marker='s', linestyle='-.', color='red')
ax.plot(N_values, errors_cuad, label='Error cuadrático', marker='p', linestyle=':', color='green')

# Configuración de la escala y los detalles
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Número de términos (N)', fontsize=12)
ax.set_ylabel('Error', fontsize=12)
ax.set_title('Errores en la aproximación de π', fontsize=14)
ax.legend()
ax.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.show()
