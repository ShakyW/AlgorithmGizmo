from random import randint

SEEN_TILE = 1
END_TILE = 3

def init_board(width=10, height=10):
    newBoard = [[0 for i in range(width)] for j in range(height)]
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

def doBFS(board, startPos, width=10, height=10):
    printBoard(board)
    print(idxToRowCol(startPos, width))
    
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