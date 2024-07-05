def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def playagain():
    w=input("do you want to play again:(yes/no)").lower().strip()
    print(w)
    if w!=("yes" or "y"):
        tic_tac_toe()

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row[1-3] column[1-3]): ").split(  ))
            if(row>0 and col >0) :

                if board[row-1][col-1] == ' ':
                    board[row-1][col-1] = current_player
                    
                    if check_win(board, current_player):
                        print_board(board)
                        print(f"Player {current_player} wins!")
                        if current_player!="X":
                            print(f"Player X loser!")
                            # print("O is the winner")
                        else:
                            print(f"Player O loser!")
                            # print("X is the winner")
                
                            playagain()
                        break
                    elif check_draw(board):
                        print_board(board)
                        print("It's a draw!")
                        playagain()
                        break
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'
                else:
                    print("That cell is already taken. Try again.")
            else:
                print("enter a move from row[1-3] and col[1-3]!!") 
        except ValueError:
            print("enter both the values!!") 
        except IndexError:
            print("entered value is out of range")


if __name__ == "__main__":
    tic_tac_toe()


















