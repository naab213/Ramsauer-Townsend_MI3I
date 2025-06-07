import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.linalg import eigh

dx = 0.002
nx = int(1 / dx) * 2  # 2000 points
x = np.linspace(0, (nx - 1) * dx, nx)

V0 = -4000
x1, x2 = 0.8, 0.9

V = np.zeros(nx)
V[(x >= x1) & (x <= x2)] = V0
V += abs(V0)

# Laplacien
main_diag = np.full(nx, -2.0)
off_diag = np.ones(nx - 1)
laplacian = diags([off_diag, main_diag, off_diag], [-1, 0, 1]) / dx**2

# Hamiltonien H = -1/2 Δ + V(x)
H = (-0.5) * laplacian.toarray() + np.diag(V)

num_states = 4
energies, wavefuncs = eigh(H, subset_by_index=(0, num_states - 1))

# Normalisation
wavefuncs_normalized = wavefuncs / np.sqrt(np.sum(wavefuncs**2, axis=0) * dx)

# Affichage
plt.figure(figsize=(10, 6))
plt.plot(x, V / abs(V0), 'k-', label="Potentiel (normalisé)")

for n in range(num_states):
    psi = wavefuncs_normalized[:, n]
    plt.plot(x, psi + energies[n] / abs(V0), label=f"État {n} (E = {energies[n]:.1f})")

plt.xlabel("x")
plt.ylabel("Fonction d’onde + énergie")
plt.title("États stationnaires dans le puits (potentiel décalé)")
plt.grid(True)
plt.legend()
plt.show()
