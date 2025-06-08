import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Paramètres physiques
hbar = 1
m = 1
V0 = 50    # Profondeur du puits (valeur positive)
a = 1.0    # Demi-largeur du puits

#Équations transcendantales pour niveaux d'énergie liés

def even_eq(E):
    k = np.sqrt(2 * m * E) / hbar
    kappa = np.sqrt(2 * m * (V0 - E)) / hbar
    return k * np.tan(k * a) - kappa

def odd_eq(E):
    k = np.sqrt(2 * m * E) / hbar
    kappa = np.sqrt(2 * m * (V0 - E)) / hbar
    return -k / np.tan(k * a) - kappa

#Recherche des solutions (états liés) 

even_guesses = [1, 6, 12, 20]
odd_guesses = [3, 9, 15]

even_E = [fsolve(even_eq, guess)[0] for guess in even_guesses if 0 < fsolve(even_eq, guess)[0] < V0]
odd_E = [fsolve(odd_eq, guess)[0] for guess in odd_guesses if 0 < fsolve(odd_eq, guess)[0] < V0]
energies = sorted(even_E + odd_E)

#Construction des fonctions d'onde

x = np.linspace(-2*a, 2*a, 1000)
V = np.array([-V0 if abs(xi) < a else 0 for xi in x])
psi_list = []

for E in energies:
    k = np.sqrt(2 * m * E) / hbar
    kappa = np.sqrt(2 * m * (V0 - E)) / hbar

    if E in even_E:
        psi = np.where(np.abs(x) < a, np.cos(k * x), np.cos(k * a) * np.exp(-kappa * (np.abs(x) - a)))
    else:
        psi = np.where(np.abs(x) < a, np.sin(k * x), np.sign(x) * np.sin(k * a) * np.exp(-kappa * (np.abs(x) - a)))

    psi /= np.max(np.abs(psi))  # Normalisation visuelle
    psi_list.append(psi)

#Tracé des courbes

plt.figure(figsize=(10, 6))
plt.plot(x, V, 'k-', label='Puits de potentiel $V(x)$')

# Afficher uniquement les 3 premiers états
for i, (E, psi) in enumerate(zip(energies[:3], psi_list[:3])):
    plt.plot(x, psi + E, label=f"$\psi_{i+1}(x)$, E = {E:.2f}")

plt.title("États stationnaires liés dans un puits de potentiel fini")
plt.xlabel("x")
plt.ylabel("Énergie et fonction d’onde")
plt.axhline(0, color='gray', linestyle='--')
plt.ylim(-V0 - 5, max(energies[:3]) + 5)  # Ajuster l'échelle verticale
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
