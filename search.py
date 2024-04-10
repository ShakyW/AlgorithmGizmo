from BFS import init_board, printBoard, bfsStep, getNeighbors, idxToRowCol
from dfs import dfs_step, print_graph_graph_supplied, manual_step

WIDTH = 10
HEIGHT = 10

def main():
    board, startPos, endPos = init_board(WIDTH, HEIGHT)
    print("Board: ")
    printBoard(board)
    print()
    choiche = input("Would you like to do (D)FS, (B)FS, or (M)anual search? ")
    if (choiche.lower() == 'b'):
        fringe = [*getNeighbors(startPos, WIDTH, HEIGHT)]
        isDone = 0
        total = 0

        while(not isDone): # Until we are finished loop through the BFS
            isDone = bfsStep(board, fringe, endPos, WIDTH, HEIGHT)
            total += not isDone
            print_graph_graph_supplied(board)
            input()

        print('Total nodes searched: ', total)

    if (choiche.lower() == 'd'):
        stack = [('E', *idxToRowCol(startPos, WIDTH))]
        total = 0
        while stack:
            board, stack, flag = dfs_step(board, stack)
            print_graph_graph_supplied(board)
            input()
            total += not flag
            if flag:
                break

        print('Total nodes searched: ', total)
            
    if (choiche.lower() == 'm'):
        total = 0
        for n in getNeighbors(startPos, WIDTH, HEIGHT):
            x, y = idxToRowCol(n, WIDTH)
            board[x][y] = '-'
        while True:
            print_graph_graph_supplied(board)
            total, flag = manual_step(board, total)
            if flag:
                break       


if __name__ == "__main__":
    main()