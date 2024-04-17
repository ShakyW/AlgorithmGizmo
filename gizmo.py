import random
from tkinter import *
from tkinter import messagebox 

graph = []
start, end = (0, 0), (0, 0)
directions = {}
buttons = []
total, state = 0, 0
stack, queue = [], []
nothing = 0

size = 10

def initialize():
    global graph, start, end, directions, buttons, stack, queue, total, state, nothing, size
    graph = []
    start, end = (0, 0), (0, 0)
    directions = {}
    buttons = []
    total, state = 0, 0
    stack, queue = [], []
    nothing = 0
    graph = [['#' for i in range(size)] for j in range(size)]

    end = (0, 0)
    if random.randint(0, 1):
        end = (random.randint(0, size - 1), [0, size - 1][random.randint(0,1)])
    else:
        end = ([0, size - 1][random.randint(0, 1)], random.randint(0, size - 1))

    directions = {
        'E' : (0, 1),
        'W' : (0, -1),
        'N' : (-1, 0),
        'S' : (1, 0),
    }

    start = (len(graph)//2, len(graph)//2)
    graph[start[0]][start[1]] = 'S'
    for d, n in nbrs((start[0], start[1])):
        x, y = n
        graph[x][y] = '-'
        
    buttons = [['#' for i in range(size + 2)] for j in range(size)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):                   
            buttons[i][j] = Button(
                                height = 1, width = 2, 
                                font = ("Helvetica","20"), 
                                text = graph[i][j],
                                command = lambda r = i, c = j : setButton(r,c))
            buttons[i][j].grid(row = i, column = j)
    
    buttons[0][size] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'DFS',
                        command = lambda r = 0, c = 10 : dfs())
    buttons[0][size].grid(row = 0, column = size)
    buttons[0][size + 1] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'BFS',
                        command = lambda r = i, c = j : bfs())
    buttons[0][size + 1].grid(row = 0, column = size + 1)

    buttons[size - 1][size + 1] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'Reset',
                        command = lambda r = i, c = j : initialize())
    buttons[size - 1][size + 1].grid(row = size - 1, column = size + 1)

def nbrs(node, dir = 'N'):
    result = []
    flag = False
    for d in directions:
        new_node = (node[0] + directions[d][0], node[1] + directions[d][1])
        if new_node[0] >= 0 and new_node[0] < len(graph) and new_node[1] >= 0 and new_node[1] < len(graph[0]):
            if d == dir:
                flag = True
            else:
                result.append((d, new_node))
    if flag == True:
        result.append((dir, (node[0] + directions[dir][0], node[1] + directions[dir][1])))
    return result

def updateButton(x, y):
    buttons[x][y].configure(text = graph[x][y])

def setButton(x, y):
    global total, nothing
    char = graph[x][y]
    if char == '-' and state == 0 and nothing == 0:
        total += 1
        if end[0] == x and end[1] == y:
            graph[x][y] = 'E'
            updateButton(x, y)
            finish()
            return
        graph[x][y] = '*'
        updateButton(x, y)
        for d, n in nbrs((x, y)):
            nx, ny = n
            if graph[nx][ny] == '#':
                graph[nx][ny] = '-'
                updateButton(nx, ny)

def reset(arg):
    global buttons, stack, queue, state, graph, total, nothing
    stack, queue, state, total, nothing = [], [], 0, 0, 1
    graph = [['#' for i in range(size)] for j in range(size)]
    graph[start[0]][start[1]] = 'S'
    for d, n in nbrs((start[0], start[1])):
        x, y = n
        graph[x][y] = '-'
    graph[end[0]][end[1]] = 'E'

    for i in range(len(graph)):
        for j in range(len(graph[0])):                   
            buttons[i][j] = Button(
                                height = 1, width = 2, 
                                font = ("Helvetica","20"), 
                                text = graph[i][j],
                                command = lambda r = i, c = j : setButton(r,c))
            buttons[i][j].grid(row = i, column = j)

    if arg == 'dfs':
        buttons[1][size] = Button(
                            height = 1, width = 4, 
                            font = ("Helvetica","20"), 
                            text = '>',
                            command = lambda r = i, c = j : dfs_step())
        buttons[1][size].grid(row = 1, column = size)

        buttons[1][size + 1] = Button(
                            height = 1, width = 4, 
                            font = ("Helvetica","20"), 
                            text = '>>',
                            command = lambda r = i, c = j : dfs_all())
        buttons[1][size + 1].grid(row = 1, column = size + 1)
    elif arg == 'bfs':
        buttons[1][size] = Button(
                            height = 1, width = 4, 
                            font = ("Helvetica","20"), 
                            text = '>',
                            command = lambda r = i, c = j : bfs_step())
        buttons[1][size].grid(row = 1, column = size)

        buttons[1][size + 1] = Button(
                            height = 1, width = 4, 
                            font = ("Helvetica","20"), 
                            text = '>>',
                            command = lambda r = i, c = j : bfs_all())
        buttons[1][11].grid(row = 1, column = size + 1)
    buttons[size - 1][size + 1] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'Reset',
                        command = lambda r = i, c = j : initialize())
    buttons[size - 1][size + 1].grid(row = size - 1, column = size + 1)

def dfs():
    reset('dfs')
    global start, stack, graph
    for d, n in nbrs(start):
        n1, n2 = n
        stack.append((d, n1, n2))

def dfs_step():
    global graph, total, stack
    if state == 0 and nothing == 1:
        total += 1
        temp = stack.pop()
        dir, node = temp[0], (temp[1], temp[2])
        if node[0] == end[0] and node[1] == end[1]:
            updateButton(node[0], node[1])
            finish()
        if graph[node[0]][node[1]] == '-':
            graph[node[0]][node[1]] = '*'
            updateButton(node[0], node[1])
        for d, n in nbrs(node, dir):
            x, y = n
            if graph[x][y] == '#':
                graph[x][y] = '-'
                updateButton(x, y)
                stack.append((d, x, y))
            elif graph[x][y] == 'E':
                stack.append((d, x, y))

def dfs_all():
    global stack, state, nothing
    while stack and state == 0 and nothing == 1:
        dfs_step()

def bfs():
    reset('bfs')
    global start, queue, graph
    for d, n in nbrs(start):
        n1, n2 = n
        queue.append((d, n1, n2))

def bfs_step():
    global graph, total, queue
    if state == 0 and nothing == 1:
        total += 1
        temp = queue.pop(0)
        dir, node = temp[0], (temp[1], temp[2])
        if node[0] == end[0] and node[1] == end[1]:
            updateButton(node[0], node[1])
            finish()
        if graph[node[0]][node[1]] == '-':
            graph[node[0]][node[1]] = '*'
            updateButton(node[0], node[1])
        for d, n in nbrs(node, dir):
            x, y = n
            if graph[x][y] == '#':
                graph[x][y] = '-'
                updateButton(x, y)
                queue.append((d, x, y))
            elif graph[x][y] == 'E':
                queue.append((d, x, y))

def bfs_all():
    global queue, state, nothing
    while queue and state == 0 and nothing == 1:
        bfs_step()

def finish():
    global state
    state = 1
    messagebox.showinfo('Congratulations!', 'Total nodes searched: ' + str(total))

window = Tk()
window.resizable(0,0)

initialize()

mainloop()