import time
import sys
import os

# Add parent directory to path to access other lab modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab1.route_search import tsp_bfs, tsp_dfs
from lab2.greedy import tsp_nn, tsp_greedy
from tsp_utils import *

   
def min_path(map):
    n = len(map)
    h = float('inf')
    for i in range(n):
        for j in range(n):
            if map[i][j] != 0 and i != j and map[i][j]<h:
                h = map[i][j]
    return h
    

def astar(map, start_city):
    n = len(map)
    open = [(start_city, 0, 0, 0, [start_city])] # (city, g, h, f, path)
    closed = []

    h_cost = min_path(map)
    
    while open:
        current_index = 0
        for i, (_, _, _, f, _) in enumerate(open): # lowest f cost
            if f < open[current_index][3]:
                current_index = i

        # remove current city from open and add to closed
        current = open.pop(current_index)
        current_city, g_cost, _, _, path = current
        closed.append(current_city)
        
        if len(path) == n:
            if map[current_city][start_city] > 0:
                final_cost = g_cost + map[current_city][start_city]
                final_path = path + [start_city]
                return final_path, final_cost
            continue # if cannot return to start city, try next path
        
        for child in range(n):
            
            # skip if no path or already visited
            if map[current_city][child] == 0 or child in path:
                continue
            
            new_g = g_cost + map[current_city][child]
            
            new_h = h_cost * (n - len(path))
            new_f = new_g + new_h
            
            new_path = path + [child]
            
            # check if child is in open list with a lower f cost
            skip = False
            for _, (city, _, _, f_, _) in enumerate(open):
                if city == child and f_ <= new_f:
                    skip = True
                    break
            
            if skip:
                continue
            
            open.append((child, new_g, new_h, new_f, new_path))
            
    return None, -1


def main(num_cities, density, symmetric, debug):
    #generate cities
    n = num_cities
    cities = gen_cities(n)
    if debug:
        [print(c) for c in cities]

    #generate map
    map = gen_map(cities, n, density, symmetric)
    if debug:
        print("Map:")
        map_print(n, map)
    

    #TSP
    start_city = 0 

    start_time = time.time()
    path, cost = astar(map, start_city)
    end_time = time.time()
    astar_time = end_time - start_time
    print(f"A*\nTime: {astar_time}\nCost: {cost:.4f}\nPath: {path}\n")

    start_time = time.time()
    bfs_path, bfs_cost = tsp_bfs(map, start_city)
    end_time = time.time()
    bfs_time = end_time - start_time
    print(f"BFS\nTime: {bfs_time}\nCost: {bfs_cost:.4f}\nPath: {bfs_path}\n")

    start_time = time.time()
    dfs_path, dfs_cost = tsp_dfs(map, start_city)
    end_time = time.time()
    dfs_time = end_time - start_time
    print(f"DFS\nTime: {dfs_time}\nCost: {dfs_cost:.4f}\nPath: {dfs_path}")

    start_time = time.time()
    nn_path, nn_cost = tsp_nn(map, start_city)
    end_time = time.time()
    nn_time = end_time - start_time
    print(f"NN\nTime: {nn_time}\nCost: {nn_cost:.4f}\nPath: {nn_path}")

    start_time = time.time()
    greedy_path, greedy_cost = tsp_greedy(map, start_city)
    end_time = time.time()
    greedy_time = end_time - start_time
    print(f"Greedy\nTime: {greedy_time}\nCost: {greedy_cost:.4f}\nPath: {greedy_path}")


if __name__ == "__main__":
    # main(num_cities = 7, density=1.0, symmetric=True, debug=False)
    n_cities = 9

    print("\n100% connections, Symmetric")
    main(num_cities=n_cities, density=1.0, symmetric=True, debug=True)
    
    # print("\n80% connections, Symmetric")
    # main(num_cities=n_cities, density=0.8, symmetric=True, debug=False)
    
    # print("\n100% connections, Asymmetric")
    # main(num_cities=n_cities, density=1.0, symmetric=False, debug=False)
    
    # print("\n80% connections, Asymmetric")
    # main(num_cities=n_cities, density=0.8, symmetric=False, debug=False)