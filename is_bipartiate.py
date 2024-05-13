from collections import deque

with open('in.txt', 'r') as file:
    vertices_num = int(file.readline())
    adj_list = []
    for i in range(vertices_num):
        line = file.readline()
        row = [int(x)-1 for x in line.strip().split()]
        row.pop()
        adj_list.append(row)

    graph = {}
    for i in range(vertices_num):
        graph[i] = adj_list[i]

    print(graph)


def is_bipartiate(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    part1 = set()
    part2 = set()

    part1.add(start)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                if node in part1:
                    part2.add(neighbor)
                if node in part2:
                    part1.add(neighbor)
                queue.append(neighbor)
                visited.add(neighbor)
            else:
                if node in part1 and neighbor in part1 or node in part2 and neighbor in part2:
                    return None

    return part1, part2


s = ''
if is_bipartiate(graph, 0):
    part1, part2 = is_bipartiate(graph, 0)
    sort_part1 = sorted(part1)
    sort_part2 = sorted(part2)
    s += 'Y\n'
    for v in sort_part1:
        s += str(v+1) + ' '
    s += '\n'
    for v in sort_part2:
        s += str(v+1) + ' '
else:
    s = 'N'

with open("out.txt", "w") as file:
    file.write(s)


