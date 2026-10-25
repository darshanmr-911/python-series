"""
Traveling Salesman Problem (TSP) — heuristic approach.

1. Nearest Neighbor: greedy tour construction
2. 2-opt: local search to shorten the tour
"""

import math
import random


def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def build_distance_matrix(cities):
    n = len(cities)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(cities[i], cities[j])
            dist[i][j] = dist[j][i] = d
    return dist


def tour_length(tour, dist):
    total = 0.0
    for i in range(len(tour)):
        total += dist[tour[i]][tour[(i + 1) % len(tour)]]
    return total


def nearest_neighbor(dist, start=0):
    """Greedy heuristic: always visit the closest unvisited city."""
    n = len(dist)
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    current = start

    while unvisited:
        nxt = min(unvisited, key=lambda city: dist[current][city])
        tour.append(nxt)
        unvisited.remove(nxt)
        current = nxt

    return tour


def two_opt(tour, dist, max_passes=100):
    """
    2-opt local search: reverse a segment if it shortens the tour.
    Repeats until no improvement or max_passes reached.
    """
    n = len(tour)
    improved = True
    passes = 0

    while improved and passes < max_passes:
        improved = False
        passes += 1
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue
                a, b = tour[i - 1], tour[i]
                c, d = tour[j - 1], tour[j % n]
                delta = (dist[a][c] + dist[b][d]) - (dist[a][b] + dist[c][d])
                if delta < -1e-9:
                    tour[i:j] = reversed(tour[i:j])
                    improved = True

    return tour


def solve_tsp_matrix(dist, start=0, use_two_opt=True):
    """Solve TSP using a given distance matrix (graph[i][j] = cost)."""
    tour = nearest_neighbor(dist, start=start)
    if use_two_opt:
        tour = two_opt(tour, dist)
    return tour, tour_length(tour, dist)


def multi_start_tsp_matrix(dist, restarts=None, use_two_opt=True):
    """Try each city as start; keep the best tour."""
    n = len(dist)
    if restarts is None or restarts >= n:
        starts = list(range(n))
    else:
        starts = random.sample(range(n), restarts)

    best_tour, best_len = None, float("inf")
    for start in starts:
        tour, length = solve_tsp_matrix(dist, start=start, use_two_opt=use_two_opt)
        if length < best_len:
            best_tour, best_len = tour, length
    return best_tour, best_len


def solve_tsp(cities, start=0, use_two_opt=True):
    dist = build_distance_matrix(cities)
    return solve_tsp_matrix(dist, start=start, use_two_opt=use_two_opt)


def multi_start_tsp(cities, restarts=10, use_two_opt=True):
    dist = build_distance_matrix(cities)
    return multi_start_tsp_matrix(dist, restarts=restarts, use_two_opt=use_two_opt)


def print_matrix(dist):
    n = len(dist)
    print("     ", end="")
    for j in range(n):
        print(f"{j:5}", end="")
    print()
    for i in range(n):
        print(f"  {i}:", end="")
        for j in range(n):
            print(f"{dist[i][j]:5}", end="")
        print()


if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    print("Distance matrix (graph):")
    print_matrix(graph)

    tour, length = multi_start_tsp_matrix(graph)

    print("\nBest tour (city indices, returns to start):")
    print(" -> ".join(str(i) for i in tour) + f" -> {tour[0]}")
    print(f"\nMinimum tour cost: {length}")

    print("\nNearest neighbor from each start (before 2-opt):")
    for start in range(len(graph)):
        t, L = solve_tsp_matrix(graph, start=start, use_two_opt=False)
        print(f"  start {start}: {' -> '.join(map(str, t))} -> {t[0]}  cost = {L}")
