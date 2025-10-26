# src/test_tsp.py

from tsp_algorithms import nearest_neighbor_tsp, random_tsp, exhaustive_tsp
import matplotlib.pyplot as plt
import random

# Exemple de graphe (matrice des distances)
graph = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

# Pour la visualisation, on attribue des positions aléatoires aux villes
positions = {
    0: (0, 0),
    1: (2, 1),
    2: (3, 5),
    3: (1, 4)
}

# --- Exécution des algorithmes ---
path_nn = nearest_neighbor_tsp(graph)
path_random = random_tsp(graph)
path_exh, dist_exh = exhaustive_tsp(graph)

print("🟢 Plus proche voisin :", path_nn)
print("🎲 Chemin aléatoire :", path_random)
print("💪 Chemin optimal (exhaustif) :", path_exh)
print("   Distance totale :", dist_exh)


# --- Fonction pour tracer un chemin ---
def plot_path(path, title):
    x = [positions[i][0] for i in path]
    y = [positions[i][1] for i in path]

    plt.figure(figsize=(5, 4))
    plt.plot(x, y, 'o-', linewidth=2, markersize=8)
    for i, (px, py) in positions.items():
        plt.text(px + 0.05, py + 0.05, str(i), fontsize=10)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


# --- Afficher les résultats graphiques ---
plot_path(path_nn, "🟢 Chemin - Plus proche voisin")
plot_path(path_random, "🎲 Chemin - Aléatoire")
plot_path(path_exh, f"💪 Chemin optimal (distance={dist_exh})")
