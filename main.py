# Temat: Percolation Simulation

import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Generates an n x n matrix, draws numbers from [0,1), and 'p' converts them into logical values.
def generate_grid(n, p):
    return np.random.rand(n, n) < p


# The function finds clusters using the BFS method: it starts from one open cell, visits all its neighbors
# and then neighbors of neighbors, thus determining the entire connected cluster of open cells.
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


# The function checks for each cluster whether it contains a cell from row 0 and row n-1;
# it returns True if percolation occurs, otherwise False.
def check_percolation(clusters, n):
    for cluster in clusters:
        rows = {cell[0] for cell in cluster}
        if 0 in rows and n - 1 in rows:
            return True
    return False


# The function performs many random simulations for fixed n and p, counts the cases of percolation
# and the sizes of the largest clusters; returns the percolation frequency and the average size of the largest cluster.
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


# Graphical representation of a single random percolation configuration as an n × n grid,
# where white cells represent open sites and black cells represent closed sites.
def plot_grid(grid):
    plt.imshow(grid, cmap='Greys')
    plt.title('Percolation configuration')
    plt.show()


# Creates a map of cluster sizes: for each open cell it assigns the size of the cluster it belongs to.
def cluster_size_map(grid):
    clusters = find_clusters(grid)
    size_map = np.zeros_like(grid, dtype=int)

    for cluster in clusters:
        size = len(cluster)
        for (i, j) in cluster:
            size_map[i, j] = size

    return size_map


# Cluster visualization: the color of a cell corresponds to the size of the cluster.
def plot_cluster_sizes(grid, p=None):
    size_map = cluster_size_map(grid)
    plt.figure()
    plt.imshow(size_map)
    plt.colorbar(label='Cluster size')
    if p is not None:
        plt.title(f'Cluster sizes for p={p}')
    else:
        plt.title('Cluster sizes')
    plt.show()


# Returns the percolating cluster or None if it does not exist.
def get_percolating_cluster(grid):
    n = grid.shape[0]
    clusters = find_clusters(grid)

    for cluster in clusters:
        rows = {cell[0] for cell in cluster}
        if 0 in rows and n - 1 in rows:
            return cluster
    return None


# Visualization of the percolating cluster: background = grid, and the percolating cluster highlighted in red.
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

        title = 'Percolating cluster (highlighted)'
    else:
        title = 'No percolating cluster'

    if p is not None:
        plt.title(f'{title}, p={p}')
    else:
        plt.title(title)

    plt.show()


# The function creates plots showing the dependence of percolation frequency and the average size
# of the largest cluster on the probability of a site being open p.
def plot_results(p_values, freqs, avg_clusters):
    plt.figure()
    plt.plot(p_values, freqs)
    plt.xlabel('p')
    plt.ylabel('Percolation frequency')
    plt.title('Percolation vs p')
    plt.show()

    plt.figure()
    plt.plot(p_values, avg_clusters)
    plt.xlabel('p')
    plt.ylabel('Average size of the largest cluster')
    plt.title('Largest cluster vs p')
    plt.show()


# Main program.
if __name__ == '__main__':
    n = 50
    trials = 200
    p_values = np.linspace(0.3, 0.8, 20)  # range of tested p values, equal step

    freqs = []
    avg_clusters = []

    for p in p_values:
        f, avg = simulation(n, p, trials)
        freqs.append(f)
        avg_clusters.append(avg)
        print(f"p={p:.2f}, percolation={f:.2f}, avg_max_cluster={avg:.1f}")

    plot_results(p_values, freqs, avg_clusters)

    # example visualization of a single grid
    p0 = 0.6
    grid = generate_grid(n, p0)
    plot_grid(grid)

    # additional visualization
    plot_cluster_sizes(grid, p0)

    # highlighting the percolating cluster on the grid background
    plot_percolating_cluster(grid, p0)

    # additional example visualizations for other p values
    p1 = 0.7
    grid2 = generate_grid(n, p1)
    plot_cluster_sizes(grid2, p1)
    plot_percolating_cluster(grid2, p1)

    p2 = 0.4
    grid3 = generate_grid(n, p2)
    plot_cluster_sizes(grid3, p2)
    plot_percolating_cluster(grid3, p2)



