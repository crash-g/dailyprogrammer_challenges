import a_star

def _get_neighbors_on_grid(index, size):
    neighbors = []
    if index%size > 0:
        neighbors.append(index-1)
    if index%size < size-1:
        neighbors.append(index+1)
    if index >= size:
        neighbors.append(index-size)
    if index < size*(size-1):
        neighbors.append(index+size)
    return neighbors

def _find_index(value, grid):
    return grid.index(value)

def _swap(index1, index2, grid):
    grid2 = list(grid)
    grid2[index1], grid2[index2] = grid2[index2], grid2[index1]
    return tuple(grid2)

# following three functions are needed by A*
def get_neighbors(node, size):
    zeroIndex = _find_index(0, node)
    return set([_swap(zeroIndex, x, node) for x in _get_neighbors_on_grid(zeroIndex, size)])

def get_edge_weight(node1, node2, size):
    return 1

def heuristic_cost_estimate(node1, node2, size):
    # naïve heuristic cost estimate: count minimum number of necessary swaps
    return sum([1 for i,x in enumerate(node1) if x != node2[i]])/2

if __name__ == "__main__":
    def solve():
        solution = a_star.a_star_search(start, goal, size, heuristic_cost_estimate, get_neighbors, get_edge_weight)
        print(solution)
        print("moves: " + str(len(solution)-1))        
    start = (0,1,2,4,8,3,7,6,5)
    goal = (1,2,3,4,5,6,7,8,0)
    size = 3
    solve()
    start = (7,6,4,0,8,1,2,3,5)
    solve()
    start = (1,2,3,4,5,6,8,7,0)
    solve()
    with open("large_slider_input.txt", "r") as lines:
        l = []
        for line in lines:
            l.extend([int(x) for x in line.split(" ") if x != "\n"])
        start = tuple(l)
        goalList = list(range(1,10000))
        goalList.append(0)
        goal = tuple(goalList)
        size = 100
        solve()
