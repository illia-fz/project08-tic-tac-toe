def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current = 'X'
    for _ in range(9):
        print_board(board)
        print(f"Player {current}'s turn")
        row = int(input('Enter row (0-2): '))
        col = int(input('Enter col (0-2): '))
        if board[row][col] != ' ':
            print('Cell already taken. Try again.')
            continue
        board[row][col] = current
        if check_winner(board, current):
            print_board(board)
            print(f'Player {current} wins!')
            return
        current = 'O' if current == 'X' else 'X'
    print_board(board)
    print("It's a tie!")
if __name__ == '__main__':
    tic_tac_toe()
