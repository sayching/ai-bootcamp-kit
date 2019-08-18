# You will create a function that check the winner of TicTacToe game.

def ttt_winner(board):
    # rows
    for x in range(0, 3):
        row = {board[x][0], board[x][1], board[x][2]}
        if len(row) == 1 and board[x][0] != 0:
            return board[x][0]

    # columns
    for x in range(0, 3):
        column = {board[0][x], board[1][x], board[2][x]}
        if len(column) == 1 and board[0][x] != 0:
            return board[0][x]

    # diagonals
    diag1 = {board[0][0], board[1][1], board[2][2]}
    diag2 = {board[0][2], board[1][1], board[2][0]}
    if len(diag1) == 1 or len(diag2) == 1 and board[1][1] != 0:
        return board[1][1]

    return 0


p1_win = ([[1, 1, 1],
           [2, 1, 2],
           [2, 2, 1]])

draw = ([[1, 2, 1],
         [2, 1, 2],
         [2, 1, 2]])

p2_win = ([[1, 2, 2],
           [1, 2, 0],
           [2, 1, 0]])

print("P1 win", ttt_winner(p1_win))
print("Draw", ttt_winner(draw))
print("P2 win", ttt_winner(p2_win))
