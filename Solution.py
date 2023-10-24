def maxMoves(gird):
    rows = len(grid)
    columns = len(grid[0])

    # Initialize a helper grid with all zeros, except for the first column
    helper = [[0 for j in range(columns)] for i in range(rows)]
    for i in range(rows):
        helper[i][0] = 1

    #checking can i move to next column or not?
    def setValueHelper(column):
        flag = False
        for row in range(rows):
            if helper[row][column] == 1: #checking if i stand on valid cell or not
                # Check if it's possible topRight cell and check if topRight cell of helper grid set to valid or invalid
                if (row - 1 > -1 and column + 1 < columns) and (helper[row - 1][column + 1] == 0):
                    if grid[row][column] < grid[row - 1][column + 1]:
                        helper[row - 1][column + 1] = 1
                        flag = True
                # Check if it's possible Right cell and check if Right cell of helper grid set to valid or invalid
                if (column + 1 < columns) and (helper[row][column + 1] == 0):
                    if grid[row][column] < grid[row][column + 1]:
                        helper[row][column + 1] = 1
                        flag = True
                # Check if it's possible bottomRight cell and check if bottomRigh cell of helper grid set to valid or invalid
                if (row + 1 < rows and column + 1 < columns) and (helper[row + 1][column + 1] == 0):
                    if grid[row][column] < grid[row + 1][column + 1]:
                        helper[row + 1][column + 1] = 1
                        flag = True

                #if any if condition true it means i can move right column

        if flag:
            return True
        return False

    moves = 0
    for column in range(columns):
        if setValueHelper(column):
            moves += 1
    return moves



grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# grid = [[3,2,4],[2,1,9],[1,1,7]]

# m, n = map(int, input().split())
# grid = []
# for i in range(m):
#     row = [int(i) for i in input().split()]
#     grid.append(row)

print(maxMoves(grid))

