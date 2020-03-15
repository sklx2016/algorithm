def dfs(board, x, y, height, weight):
    if x < 0 or x >= height or y < 0 or y >= weight or board[x][y] != 'O':
        return
    board[x][y] = 'S'
    dfs(board, x - 1, y, height, weight)
    dfs(board, x + 1, y, height, weight)
    dfs(board, x, y - 1, height, weight)
    dfs(board, x, y + 1, height, weight)



def SurroundedRegions(board):
    if len(board) == 0:
        return board
    height = len(board)
    weight = len(board[0])
    for i in range(weight):
        if board[0][i] == 'O':
            dfs(board, 0, i, height, weight)
        if board[height][i] == 'O':
            dfs(board, height, i, height, weight)
    for j in range(height):
        if board[j][0] == 'O':
            dfs(board, j, 0, height, weight)
        if board[j][weight] == 'O':
            dfs(board, j, weight, height, weight)
    for i in range(height):
        for j in range(weight):
            if board[i][j] == 'S':
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'
    return board

