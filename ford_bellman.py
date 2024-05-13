with open('in.txt', 'r') as file:
    vert_num = int(file.readline())
    graph = [[float('-inf') for _ in range(vert_num)] for _ in range(vert_num)]
    for i in range(vert_num):
        line = file.readline().strip()
        data = list(map(int, line.split()))
        for j in range(0, len(data), 2):
            vertex = data[j]
            if vertex == 0:
                break
            if j + 1 < len(data):
                if data[j + 1] == 0:
                    cost = float('-inf')
                else:
                    cost = data[j + 1]
            graph[i][vertex - 1] = cost
    start_vert = int(file.readline()) - 1
    end_vert = int(file.readline()) - 1


def bellman_ford(graph, start):
    n = len(graph)
    inf = float('-inf')
    dist = [inf] * n
    dist[start] = 0
    prev = [-1] * n

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != inf:
                    if dist[u] + graph[u][v] > dist[v]:
                        dist[v] = dist[u] + graph[u][v]
                        prev[v] = u

    return dist, prev


distances, prev_vertices = bellman_ford(graph, start_vert)

max_path = []

for i in range(len(distances)):
    path = []
    current_vertex = i
    while current_vertex != -1:
        path.insert(0, current_vertex)
        current_vertex = prev_vertices[current_vertex]
    if i == end_vert:
        max_path = path
        max_len = distances[end_vert]

path = ''
if max_len == float('-inf'):
    res = 'N'
else:
    for i in max_path:
        path += str(i + 1) + ' '
    res = 'Y\n' + path + '\n' + str(max_len)

with open("out.txt", "w") as file:
    file.write(res)
