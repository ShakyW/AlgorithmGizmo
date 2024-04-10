import random

graph = [['#' for i in range(10)] for j in range(10)]

end = (0, 0)
if random.randint(0, 1):
    end = (random.randint(0, 9), [0, 9][random.randint(0,1)])
else:
    end = ([0, 9][random.randint(0, 1)], random.randint(0, 9))

directions = {
    'E' : (0, 1),
    'W' : (0, -1),
    'N' : (-1, 0),
    'S' : (1, 0),
}

def in_graph(node):
    return node[0] >= 0 and node[0] < len(graph) and node[1] >= 0 and node[1] < len(graph)

def nbrs(node, dir = 'N'):
    result = []
    flag = False
    for d in directions:
        new_node = (node[0] + directions[d][0], node[1] + directions[d][1])
        if in_graph(new_node):
            if d == dir:
                flag = True
            else:
                result.append((d, new_node))
    if flag == True:
        result.append((dir, (node[0] + directions[dir][0], node[1] + directions[dir][1])))
    return result

def print_graph():
    print(' ', ' '.join([str(i) for i in range(len(graph))]))
    for i in range(len(graph)):
        print(i, ' '.join(graph[i]))

def print_graph_graph_supplied(graph):
    print(' ', ' '.join([str(i) for i in range(len(graph))]))
    for i in range(len(graph)):
        print(i, ' '.join(graph[i]))

start = (len(graph)//2, len(graph)//2)
graph[start[0]][start[1]] = 'S'

def dfs(graph, start):
    total = 0
    stack = [('E', start[0], start[1])]
    while stack:
        graph, stack, flag = dfs_step(graph, stack)
        if flag:
            return

def dfs_step(graph, stack):
    temp = stack.pop()
    dir, node = temp[0], (temp[1], temp[2])
    if node[0] == end[0] and node[1] == end[1]:
        graph[node[0]][node[1]] = 'E'
        return graph, stack, True
    if graph[node[0]][node[1]] == '-':
        graph[node[0]][node[1]] = '*'
        total += 1
    for d, n in nbrs(node, dir):
        x, y = n
        if graph[x][y] == '#':
            graph[x][y] = '-'
            stack.append((d, x, y))
    return graph, stack, False

def manual():
    total = 0
    for d, n in nbrs(start):
        x, y = n
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
        for d, n in nbrs(node):
            x, y = n
            if graph[x][y] == '#':
                graph[x][y] = '-'


def main():
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


if __name__ == "__main__":
    main()
