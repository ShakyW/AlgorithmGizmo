from random import randint

UNSEEN_TILE = 0
SEEN_TILE = 1
FRINGE_TILE = 2
END_TILE = 3
WIN_TILE = 4

# Create board with given width and height and a random end tile
def init_board(width=10, height=10):
    newBoard = [[UNSEEN_TILE for i in range(width)] for j in range(height)]
    startPos = (width//2, height//2) # Start in middle of board
    
    randCol = randint(0, 9)
    randRow = randint(0, 9)
    while randCol==startPos[0] and randRow==startPos[0]: # Don't have spot chosen be where we start - that would be really lame
        randCol = randint(0, 9)
        randRow = randint(0, 9)

    newBoard[randRow][randCol] = END_TILE
    newBoard[startPos[1]][startPos[0]] = SEEN_TILE

    return (newBoard, rowColToIdx(startPos[1], startPos[0], width))

# Return row-major-order index of item at given row and column
def rowColToIdx(row: int, col: int, width: int):
    return row*width+col

# Return (row, col) 
def idxToRowCol(idx: int, width: int):
    return (idx//width, idx%width)

def getNeighbors(idx: int, width: int, height: int):
    nbrs = []
    row, col = idxToRowCol(idx, width)
    if (row > 0): nbrs.append(rowColToIdx(row-1, col, width)) # Not on top => can go up
    if (row < height-1): nbrs.append(rowColToIdx(row+1, col, width)) # Not on bottom => can go down
    if (col > 0): nbrs.append(rowColToIdx(row, col-1, width)) # Not on left side => can go left
    if (col < width-1): nbrs.append(rowColToIdx(row, col+1, width)) # Not on right side => can go down

    return nbrs


# Does a single step of bfs, updates the fringe and returns if at end (0 if not, 1 if so)
def bfsStep(board: list[list[int]], fringe: set[int], width: int, height: int):
    nextIdx = fringe.pop(0)
    nextRow, nextCol = idxToRowCol(nextIdx, width)
    board[nextRow][nextCol] = SEEN_TILE
    nbrs = getNeighbors(nextIdx, width, height)
    for node in nbrs:
        nodeRow, nodeCol = idxToRowCol(node, width)
        if board[nodeRow][nodeCol] == UNSEEN_TILE: # New neighbor, add to fringe
            board[nodeRow][nodeCol] = FRINGE_TILE
            fringe.append(node)
        elif board[nodeRow][nodeCol] == END_TILE:   # Yay we win
            board[nodeRow][nodeCol] = WIN_TILE 
            return 1
    
    return 0    # Did not find goal this step so return 0

def doBFS(board: list[list[int]], startPos:int, width:int=10, height:int=10):
    fringe = [startPos]
    isDone = 0
    while(not isDone): # Until we are finished loop through the BFS
        isDone = bfsStep(board, fringe, width, height)
        printBoard(board)
        print() # Extra line for spacing
        input()
    
def printBoard(board: list[int]):
    for row in board:
        strToPrint = ""
        for itm in row:
            strToPrint += f"{itm} "
        strToPrint = strToPrint[:len(strToPrint)-1]
        print(strToPrint)

def main():
    width = 11
    height = 10
    board, startPos = init_board(width, height)
    doBFS(board, startPos, width, height)

if __name__ == "__main__":
    main()