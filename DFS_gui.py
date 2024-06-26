import random
from tkinter import *

graph = []
start, end = (0, 0), (0, 0)
directions = {}
buttons = []

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
        graph[x][y] = '-'\
        
    buttons = [['#' for i in range(10)] for j in range(10)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):                   
            buttons[i][j] = Button(
                            height = 1, width = 2, 
                            font = ("Helvetica","20"), 
                            text = graph[i][j],
                            command = lambda r = i, c = j : setButton(r,c))
            buttons[i][j].grid(row = i, column = j)

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
    char = graph[x][y]
    if char == '-':
        if end[0] == x and end[1] == y:
            graph[x][y] = 'E'
            updateButton(x, y)
            finish()
        graph[x][y] = '*'
        updateButton(x, y)
        for d, n in nbrs((x, y)):
            nx, ny = n
            if graph[nx][ny] == '#':
                graph[nx][ny] = '-'
                updateButton(nx, ny)

def finish():
    print('Congratulations!')

window = Tk()
window.resizable(0,0)

initialize()

mainloop()