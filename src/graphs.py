from typing import Dict, List


def calculate_degrees(g: Dict[int, List[int]]) -> Dict[int, int]:
    """
    :param g: A dict that represents a adjacency list like Dict[u, [v1,v2,v3]
    :return: A dict that represents the degree of each vertex like Dict[u, 2]
    """
    in_degree = {
        u: 0 for u, v in g.items()
    }

    for u, vs in g.items():
        for v in vs:
            in_degree[v] += 1

    return in_degree


def topological_sorter(g: Dict[int, List[int]]) -> List[int]:
    """
    :param g: A dict that represents a adjacency list like Dict[u, [v1,v2,v3]
    :return: a list of vertices topologically ordered
    """
    in_degree = calculate_degrees(g)

    vertices_with_zero_degree = [
       u for u, d in in_degree.items() if d == 0
    ]

    linear_order = []

    while vertices_with_zero_degree:
        u = vertices_with_zero_degree.pop()
        linear_order.append(u)

        for v in g[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                vertices_with_zero_degree.append(v)

    return linear_order
