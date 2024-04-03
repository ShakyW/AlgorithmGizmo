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
    print(' ', ' '.join([str(i) for i in range(len(graph))]))
    for i in range(len(graph)):
        print(i, ' '.join(graph[i]))

start = (len(graph)//2, len(graph)//2)
graph[start[0]][start[1]] = 'S'

def dfs():
    total = 0
    stack = [start]
    while stack:
        node = stack.pop()
        if node[0] == end[0] and node[1] == end[1]:
            graph[node[0]][node[1]] = 'E'
            print('Congratulations!')
            print_graph()
            print('Total nodes searched: ', total)
            break
        if graph[node[0]][node[1]] == '-':
            graph[node[0]][node[1]] = '*'
            total += 1
        for x, y in nbrs(node):
            if graph[x][y] == '#':
                graph[x][y] = '-'
                stack.append((x, y))
        print_graph()
        input()

def manual():
    total = 0
    for x, y in nbrs(start):
        graph[x][y] = '-'
    while True:
        user_x, user_y = 0, 0
        while True:
            print_graph()
            user_input = input('Where to search next? (Enter two integers with a space in between)').split(' ')
            user_x, user_y = int(user_input[0]), int(user_input[1])
            if user_x >= 0 and user_x < len(graph) and user_y >= 0 and user_y < len(graph[0]):
                char = graph[user_x][user_y]
                if char == '-':
                    break
                elif char == '#':
                    print('Invalid place to search!')
                elif char == '*' or char == 'S':
                    print('You have already searched this place.')
            else:
                print('This place is not on the graph.')

        node = (user_x, user_y)

        if node[0] == end[0] and node[1] == end[1]:
            graph[node[0]][node[1]] = 'E'
            print('Congratulations!')
            print_graph()
            print('Total nodes searched: ', total)
            break
        if graph[node[0]][node[1]] == '-':
            graph[node[0]][node[1]] = '*'
            total += 1
        for x, y in nbrs(node):
            if graph[x][y] == '#':
                graph[x][y] = '-'

print_graph()
while True:
    choice = input('What would you like to do? (type \'dfs\' for computer search, \'manual\' to manually search)')
    if choice == 'dfs':
        dfs()
        break
    elif choice == 'manual':
        manual()
    else:
        print('Invalid Choice!')

