import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
rabbit_birth_rate = 0.1   # Tasa de nacimiento de conejos
fox_death_rate = 0.1      # Tasa de muerte de zorros si no tienen comida
predation_rate = 0.01     # Tasa de depredación (con qué frecuencia los zorros comen conejos)
fox_reproduction_rate = 0.01  # Tasa de reproducción de zorros cuando comen conejos

# Inicialización de poblaciones
num_steps = 200  # Número de pasos en la simulación
rabbits = np.zeros(num_steps)
foxes = np.zeros(num_steps)

# Poblaciones iniciales
rabbits[0] = 40  # Número inicial de conejos
foxes[0] = 9     # Número inicial de zorros

# Simulación
for t in range(1, num_steps):
    # Ecuaciones de Lotka-Volterra
    rabbits[t] = rabbits[t-1] + rabbit_birth_rate * rabbits[t-1] - predation_rate * rabbits[t-1] * foxes[t-1]
    foxes[t] = foxes[t-1] + fox_reproduction_rate * rabbits[t-1] * foxes[t-1] - fox_death_rate * foxes[t-1]
    
    # Asegurarse de que las poblaciones no sean negativas
    if rabbits[t] < 0:
        rabbits[t] = 0
    if foxes[t] < 0:
        foxes[t] = 0

# Visualización de la simulación
plt.figure(figsize=(10,6))
plt.plot(rabbits, label="Conejos")
plt.plot(foxes, label="Zorros", color="red")
plt.xlabel("Tiempo (días)")
plt.ylabel("Población")
plt.title("Simulación de un Ecosistema de Conejos y Zorros")
plt.legend()
plt.show()
