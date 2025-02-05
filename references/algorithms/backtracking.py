#Backtracking on grid of size N (tic-tac-toe example)
#Returns if grid is valid
def valid(row, col):
    return True

def backtrack(row, col):
    if row == N: return True
    if col == N: return backtrack(row+1, 0)
    if grid[row][col] != ".": return backtrack(row, col+1)

    for token in "XO":
        grid[row][col] = token
        if valid(row, col) and backtrack(row, col+1): return True

    grid[row][col] = "."
    return False