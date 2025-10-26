# src/tsp_algorithms.py
import random
import itertools

# ------------------------------------------------------------
# 1️⃣ Méthode du plus proche voisin
# ------------------------------------------------------------
def nearest_neighbor_tsp(graph):
    """Algorithme du plus proche voisin pour le TSP."""
    visited = [False] * len(graph)
    path = [0]  # commencer au premier nœud
    visited[0] = True

    for _ in range(len(graph) - 1):
        last = path[-1]
        next_city = min(
            [(i, graph[last][i]) for i in range(len(graph)) if not visited[i]],
            key=lambda x: x[1]
        )[0]
        path.append(next_city)
        visited[next_city] = True

    path.append(path[0])  # revenir au départ
    return path


# ------------------------------------------------------------
# 2️⃣ Méthode aléatoire
# ------------------------------------------------------------
def random_tsp(graph):
    """Algorithme TSP aléatoire — teste un ordre de villes choisi au hasard."""
    cities = list(range(len(graph)))
    random.shuffle(cities)
    path = [0] + [c for c in cities if c != 0] + [0]
    return path


# ------------------------------------------------------------
# 3️⃣ Méthode exhaustive (recherche complète)
# ------------------------------------------------------------
def exhaustive_tsp(graph):
    """Algorithme TSP exhaustif — teste toutes les permutations possibles."""
    n = len(graph)
    cities = list(range(1, n))
    best_path = None
    best_distance = float('inf')

    for perm in itertools.permutations(cities):
        path = [0] + list(perm) + [0]
        distance = sum(graph[path[i]][path[i + 1]] for i in range(n))
        if distance < best_distance:
            best_distance = distance
            best_path = path

    return best_path, best_distance
