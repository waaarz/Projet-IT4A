# src/generator.py
import os
import numpy as np
import pandas as pd

def generate_coords(n, bbox=(0.0, 100.0), seed=None):
    """Génère n coordonnées (x,y) uniformes dans un carré [bbox_min, bbox_max]."""
    rng = np.random.RandomState(seed)
    low, high = bbox
    coords = rng.uniform(low, high, size=(n, 2))
    return coords

def euclidean_distance_matrix(coords):
    """Calcule la matrice des distances euclidiennes."""
    diff = coords[:, None, :] - coords[None, :, :]
    dists = np.sqrt((diff ** 2).sum(axis=2))
    return dists

def save_instance_csv(coords, filename):
    """Sauvegarde les coordonnées en CSV (id,x,y)."""
    df = pd.DataFrame({
        "id": np.arange(1, coords.shape[0] + 1),
        "x": coords[:, 0],
        "y": coords[:, 1]
    })
    df.to_csv(filename, index=False)

def save_instance_tsp(coords, filename, name="TSP-instance"):
    """
    Sauvegarde au format TSPLIB (EUC_2D).
    """
    n = coords.shape[0]
    header = [
        f"NAME: {name}",
        "TYPE: TSP",
        f"DIMENSION: {n}",
        "EDGE_WEIGHT_TYPE: EUC_2D",
        "NODE_COORD_SECTION"
    ]
    with open(filename, "w") as f:
        for line in header:
            f.write(line + "\n")
        for i, (x, y) in enumerate(coords, start=1):
            f.write(f"{i} {x:.6f} {y:.6f}\n")
        f.write("EOF\n")

def generate_and_save(n, out_dir="data", prefix="inst", seed=None, bbox=(0,100)):
    """Génère une instance et sauve CSV + TSP."""
    os.makedirs(out_dir, exist_ok=True)
    coords = generate_coords(n, bbox=bbox, seed=seed)
    csv_name = os.path.join(out_dir, f"{prefix}_n{n}_s{seed}.csv")
    tsp_name = os.path.join(out_dir, f"{prefix}_n{n}_s{seed}.tsp")
    save_instance_csv(coords, csv_name)
    save_instance_tsp(coords, tsp_name, name=f"{prefix}_n{n}_s{seed}")
    return coords

if __name__ == "__main__":
    categories = {
        "test": [6, 8, 10],
        "petite": [12, 14, 15],
        "moyenne": [16, 18, 20],
        "grande": [20, 25, 30, 40]
    }

    for cat, sizes in categories.items():
        for n in sizes:
            for s in range(5):  # 5 instances par taille
                generate_and_save(
                    n,
                    out_dir=f"data/{cat}",
                    prefix=f"{cat}_inst",
                    seed=1000 + n*10 + s
                )
    print("Toutes les instances ont été générées dans ./data/")


