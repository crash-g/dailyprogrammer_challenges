"""An implementation of the A* algorithm. The heuristic which is used must be monotonic.
The algorithm is designed to work on graphs, but it can be completely adjusted by overriding the get_neighbors and get_edge_weight functions. The heuristic too can be chosen freely.
In particular, there is no need to provide the full graph at the start: a "streaming" approach can be adopted with the correct implementation of get_neighbors.
"""

import math
from sortedcontainers import SortedSet
import networkx as nx
# networkx is only used by the default implementation, which can be overriden.

def get_neighbors(node, graph):
    return set(graph.neighbors(node))

def get_edge_weight(node1, node2, graph):
    return graph.get_edge_data(node1, node2)["weight"]

def heuristic_cost_estimate(node1, node2, graph):
    return 0
# default implementation of some utility functions: each of them can be overriden.

def a_star_search(start, goal, graph, heuristic_cost_estimate=heuristic_cost_estimate,
                  get_neighbors=get_neighbors, get_edge_weight=get_edge_weight):
    gScore = {start: 0}
    # real cost to reach a node
    fScore = {start: heuristic_cost_estimate(start, goal, graph)}
    # estimated cost to reach a node
    closedSet = set()
    # set of processed nodes
    openSet = SortedSet(key=lambda node:fScore[node])
    # set of nodes being processed
    openSet.add(start)
    cameFrom = {}
    # used to reconstruct the path at the end
    while openSet:
        current = openSet.pop(0)
        if current == goal:
            return construct_path(current, cameFrom)
        for neighbor in get_neighbors(current, graph)-closedSet:
            tentativeGScore = gScore[current] + get_edge_weight(current, neighbor, graph)
            if neighbor not in gScore or tentativeGScore < gScore[neighbor]:
                gScore[neighbor] = tentativeGScore
                fScore[neighbor] = tentativeGScore + heuristic_cost_estimate(neighbor, goal, graph)
                cameFrom[neighbor] = current
                if neighbor not in openSet:
                    openSet.add(neighbor)
        closedSet.add(current)
        del fScore[current]
        del gScore[current]
        # clean up to free resources
    return []

def construct_path(current, cameFrom):
    totalPath = [current]
    while current in cameFrom:
        current = cameFrom[current]
        totalPath.append(current)
    return list(reversed(totalPath))
    
if __name__ == "__main__":
    G=nx.Graph()
    G.add_edges_from([(1,2), (1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9), (4,10),
                      (5,11), (5,12), (6,13)], weight=1)
    print(a_star_search(5,13,G))
