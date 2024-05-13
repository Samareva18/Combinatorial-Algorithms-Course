with open('in.txt', 'r') as file:
    vertices_num = int(file.readline())
    adj_matrix = []
    for i in range(vertices_num):
        line = file.readline()
        row = [int(x) for x in line.strip().split()]
        adj_matrix.append(row)


def adj_matrix_to_adj_list(adjacency_matrix):
    adjacency_list = {}
    for i in range(len(adjacency_matrix)):
        neighbors = []
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                neighbors.append(j)
        adjacency_list[i] = neighbors
    return adjacency_list


graph = adj_matrix_to_adj_list(adj_matrix)


def find_cycle_via_dfs(adjacency_lists):
    n_vertices = len(adjacency_lists)
    visited = [False] * n_vertices
    path = []
    cycle = []

    def dfs(v, prev=-1):
        nonlocal cycle
        visited[v] = True
        path.append(v)

        for u in adjacency_lists[v]:
            if u == prev:
                continue
            if u in path:
                index = path.index(u)
                cycle += path[index:]
                return
            if not visited[u]:
                dfs(u, v)

        path.pop()

    for v in range(n_vertices):
        if cycle:
            return cycle
        if not visited[v]:
            dfs(v)

    return []


cycle = find_cycle_via_dfs(graph)

for i in range(len(cycle)):
    cycle[i] += 1


def res(cycle):
    if cycle == []:
        return 'A'
    else:
        s = ''
        sorted_cycle = sorted(cycle)
        for v in sorted_cycle:
            s += str(v) + ' '
        return 'N\n' + s


with open("out.txt", "w") as file:
    file.write(res(cycle))
