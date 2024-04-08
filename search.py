from BFS import init_board, printBoard, bfsStep, getNeighbors
# DFS imports

WIDTH = 10
HEIGHT = 10

def main():
    board, startPos, endPos = init_board(WIDTH, HEIGHT)
    print("Board: ")
    printBoard(board)
    print()
    choiche = input("Would you like to do (D)FS or (B)FS search? ")
    if (choiche.lower() == 'b'):
        fringe = [*getNeighbors(startPos, WIDTH, HEIGHT)]
        isDone = 0

        while(not isDone): # Until we are finished loop through the BFS
            isDone = bfsStep(board, fringe, endPos, WIDTH, HEIGHT)
            printBoard(board)
            print() # Extra line for spacing
            input()

if __name__ == "__main__":
    main()