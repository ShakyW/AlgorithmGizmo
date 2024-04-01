import random

graph = [['#' for i in range(10)] for j in range(10)]

end = (0, 0)
if random.randint(0, 1):
    end = (random.randint(0, 9), [0, 9][random.randint(0,1)])
else:
    end = ([0, 9][random.randint(0, 1)], random.randint(0, 9))

def nbrs(node):
    result = []
    if node[0] > 0 and graph[node[0] - 1][node[1]] == '#':
        result.append((node[0] - 1, node[1]))
    if node[0] < len(graph) - 1 and graph[node[0] + 1][node[1]] == '#':
        result.append((node[0] + 1, node[1]))
    if node[1] > 0 and graph[node[0]][node[1] - 1] == '#':
        result.append((node[0], node[1] - 1))
    if node[1] < len(graph) - 1 and graph[node[0]][node[1] + 1] == '#':
        result.append((node[0], node[1] + 1))
    return result

def print_graph():
    for i in range(len(graph)):
        print(''.join(graph[i]))

start = (5, 5)
graph[start[0]][start[1]] = 'S'

def dfs():
    stack = [start]
    while stack:
        node = stack.pop()
        if node[0] == end[0] and node[1] == end[1]:
            graph[node[0]][node[1]] = 'E'
            print('Congradulations!')
            print_graph()
            break
        if graph[node[0]][node[1]] == '-':
            graph[node[0]][node[1]] = '*'
        for x, y in nbrs(node):
            if graph[x][y] == '#':
                graph[x][y] = '-'
                stack.append((x, y))
        print_graph()
        input()
dfs()
