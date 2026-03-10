# Temat: Symulacja perkolacji
# Autor: Aleksandra Janic

import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Generowanie macierzy n x n, losuje liczby [0,1), a 'p' zmienia je na wartości logiczne.
def generate_grid(n, p):
    return np.random.rand(n, n) < p


# Funkcja znajduje klastry metodą BFS: startuje z jednego otwartego pola, odwiedza wszystkich jego sąsiadów
# oraz kolejnych sąsiadów sąsiadów, wyznaczając w ten sposób cały spójny klaster otwartych pól.
def find_clusters(grid):
    n = grid.shape[0]
    visited = np.zeros_like(grid, dtype=bool)
    clusters = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(n):
        for j in range(n):
            if grid[i, j] and not visited[i, j]:
                queue = deque([(i, j)])
                visited[i, j] = True
                cluster = [(i, j)]

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if grid[nx, ny] and not visited[nx, ny]:
                                visited[nx, ny] = True
                                queue.append((nx, ny))
                                cluster.append((nx, ny))

                clusters.append(cluster)

    return clusters


# Funkcja dla każdego klastra sprawdza, czy zawiera pole z wiersza 0 oraz n-1;
# zwraca True, jeśli perkolacja zachodzi, w przeciwnym razie False.
def check_percolation(clusters, n):
    for cluster in clusters:
        rows = {cell[0] for cell in cluster}
        if 0 in rows and n - 1 in rows:
            return True
    return False


# Funkcja wykonuje wiele losowych symulacji dla ustalonego n i p, zlicza przypadki perkolacji
# oraz rozmiary największych klastrów; zwraca częstość perkolacji i średni rozmiar największego klastra.
def simulation(n, p, trials):
    percolations = 0
    max_cluster_sizes = []

    for _ in range(trials):
        grid = generate_grid(n, p)
        clusters = find_clusters(grid)

        if clusters:
            max_cluster_sizes.append(max(len(c) for c in clusters))
        else:
            max_cluster_sizes.append(0)

        if check_percolation(clusters, n):
            percolations += 1

    freq = percolations / trials
    avg_max_cluster = np.mean(max_cluster_sizes)
    return freq, avg_max_cluster


# Graficzne przedstawienie pojedynczej losowej konfiguracji perkolacji w postaci siatki n × n,
# gdzie białe pola oznaczają pola otwarte, a czarne zamknięte.
def plot_grid(grid):
    plt.imshow(grid, cmap='Greys')
    plt.title('Konfiguracja perkolacji')
    plt.show()


# Tworzy mapę rozmiarów klastrów: dla każdego otwartego pola wpisuje rozmiar klastra, do którego należy.
def cluster_size_map(grid):
    clusters = find_clusters(grid)
    size_map = np.zeros_like(grid, dtype=int)

    for cluster in clusters:
        size = len(cluster)
        for (i, j) in cluster:
            size_map[i, j] = size

    return size_map


# Wizualizacja klastrów: kolor pola odpowiada rozmiarowi klastra.
def plot_cluster_sizes(grid, p=None):
    size_map = cluster_size_map(grid)
    plt.figure()
    plt.imshow(size_map)
    plt.colorbar(label='Rozmiar klastra')
    if p is not None:
        plt.title(f'Rozmiar klastrów dla p={p}')
    else:
        plt.title('Rozmiar klastrów')
    plt.show()


# Zwraca klaster perkolujący albo None, jeśli nie istnieje.
def get_percolating_cluster(grid):
    n = grid.shape[0]
    clusters = find_clusters(grid)

    for cluster in clusters:
        rows = {cell[0] for cell in cluster}
        if 0 in rows and n - 1 in rows:
            return cluster
    return None


# Wizualizacja klastra perkolującego: tło = siatka, a klaster perkolujący wyróżniony czerwonym kolorem.
def plot_percolating_cluster(grid, p=None):
    perc = get_percolating_cluster(grid)

    plt.figure()
    plt.imshow(grid, cmap='Greys')

    if perc is not None:
        n = grid.shape[0]
        mask = np.zeros((n, n), dtype=bool)
        for (i, j) in perc:
            mask[i, j] = True

        overlay = np.ma.masked_where(~mask, mask)
        plt.imshow(overlay, cmap='autumn', alpha=0.9)

        title = 'Klaster perkolujący (wyróżniony)'
    else:
        title = 'Brak klastra perkolującego'

    if p is not None:
        plt.title(f'{title}, p={p}')
    else:
        plt.title(title)

    plt.show()


# Funkcja tworzy wykresy pokazujące zależność częstości perkolacji oraz średniego rozmiaru największego klastra
# od prawdopodobieństwa otwarcia pola p.
def plot_results(p_values, freqs, avg_clusters):
    plt.figure()
    plt.plot(p_values, freqs)
    plt.xlabel('p')
    plt.ylabel('Częstość perkolacji')
    plt.title('Perkolacja vs p')
    plt.show()

    plt.figure()
    plt.plot(p_values, avg_clusters)
    plt.xlabel('p')
    plt.ylabel('Średni rozmiar największego klastra')
    plt.title('Największy klaster vs p')
    plt.show()


# Program główny.
if __name__ == '__main__':
    n = 50
    trials = 200
    p_values = np.linspace(0.3, 0.8, 20)  # przedział badanych p, równy skok

    freqs = []
    avg_clusters = []

    for p in p_values:
        f, avg = simulation(n, p, trials)
        freqs.append(f)
        avg_clusters.append(avg)
        print(f"p={p:.2f}, perkolacja={f:.2f}, avg_max_cluster={avg:.1f}")

    plot_results(p_values, freqs, avg_clusters)

    # przykładowa wizualizacja jednej siatki
    p0 = 0.6
    grid = generate_grid(n, p0)
    plot_grid(grid)

    # dodatkowa wizualizacja
    plot_cluster_sizes(grid, p0)

    # wyróżnienie klastra perkolującego na tle siatki
    plot_percolating_cluster(grid, p0)

    # dodatkowe przykład wizualizacji dla innych wartości p
    p1 = 0.7
    grid2 = generate_grid(n, p1)
    plot_cluster_sizes(grid2, p1)
    plot_percolating_cluster(grid2, p1)

    p2 = 0.4
    grid3 = generate_grid(n, p2)
    plot_cluster_sizes(grid3, p2)
    plot_percolating_cluster(grid3, p2)



