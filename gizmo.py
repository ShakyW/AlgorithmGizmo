import random
from tkinter import *
from tkinter import messagebox 

graph = []
start, end = (0, 0), (0, 0)
directions = {}
buttons = []
total, state = 0, 0
stack, queue = [], []

def initialize():
    global graph, start, end, directions, buttons
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

    start = (len(graph)//2, len(graph)//2)
    graph[start[0]][start[1]] = 'S'
    for d, n in nbrs((start[0], start[1])):
        x, y = n
        graph[x][y] = '-'
        
    buttons = [['#' for i in range(12)] for j in range(10)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):                   
            buttons[i][j] = Button(
                                height = 1, width = 2, 
                                font = ("Helvetica","20"), 
                                text = graph[i][j],
                                command = lambda r = i, c = j : setButton(r,c))
            buttons[i][j].grid(row = i, column = j)
    
    buttons[0][10] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'DFS',
                        command = lambda r = 0, c = 10 : dfs(graph, start))
    buttons[0][10].grid(row = 0, column = 10)
    buttons[0][11] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'BFS',
                        command = lambda r = i, c = j : setButton(r,c))
    buttons[0][11].grid(row = 0, column = 11)

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
    global total
    char = graph[x][y]
    if char == '-' and state == 0:
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

def reset():
    graph = [['#' for i in range(10)] for j in range(10)]
    graph[start[0]][start[1]] = 'S'
    for d, n in nbrs((start[0], start[1])):
        x, y = n
        graph[x][y] = '-'
    graph[end[0]][end[1]] = 'E'

    buttons = [['#' for i in range(12)] for j in range(10)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):                   
            buttons[i][j] = Button(
                                height = 1, width = 2, 
                                font = ("Helvetica","20"), 
                                text = graph[i][j],
                                command = lambda r = i, c = j : setButton(r,c))
            buttons[i][j].grid(row = i, column = j)

    buttons[0][10] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'DFS',
                        command = lambda r = 0, c = 10 : dfs(graph, start))
    buttons[0][10].grid(row = 0, column = 10)
    buttons[0][11] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = 'BFS',
                        command = lambda r = 0, c = 11 : setButton(r,c))
    buttons[0][11].grid(row = 0, column = 11)

    buttons[5][10] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = '>',
                        command = lambda r = i, c = j : step())
    buttons[5][10].grid(row = 0, column = 10)
    buttons[5][11] = Button(
                        height = 1, width = 4, 
                        font = ("Helvetica","20"), 
                        text = '>>',
                        command = lambda r = i, c = j : step_all())
    buttons[5][11].grid(row = 0, column = 11)

def step():
    global next_step
    next_step = 1

def step_all():
    global all_step
    all_step = 1

def dfs(graph, start):
    global stack
    for d, n in nbrs(start):
        n1, n2 = n
        stack.append((d, n1, n2))
    while stack:
        graph, stack, flag = dfs_step(graph, stack)
        if flag:
            finish()
            break

def dfs_step(graph):
    global total
    global stack
    total += 1
    temp = stack.pop()
    dir, node = temp[0], (temp[1], temp[2])
    if node[0] == end[0] and node[1] == end[1]:
        graph[node[0]][node[1]] = 'E'
        updateButton(node[0], node[1])
        return graph, stack, True
    if graph[node[0]][node[1]] == '-':
        graph[node[0]][node[1]] = '*'
        updateButton(node[0], node[1])
    for d, n in nbrs(node, dir):
        x, y = n
        if graph[x][y] == '#':
            graph[x][y] = '-'
            updateButton(x, y)
            stack.append((d, x, y))
    return graph, stack, False

def finish():
    global state
    state = 1
    messagebox.showinfo('Congratulations!', 'Total nodes searched: ' + str(total))

window = Tk()
window.resizable(0,0)

initialize()

mainloop()