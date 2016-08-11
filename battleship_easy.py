from random import randint as rand
board = []
for any in range(5):
    board.append(["O"] * 5)

def print_board():
    for row in board:
        print " ".join(row)

def random_row(board):
    row = rand(0, len(board) - 1)
    return row

def random_col(board):
    col = rand(0, len(board) - 1)
    return col

print_board()
ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row, ship_col

guess_row = []
guess_col = []

count = 5

while count > 0:
    try:
        guess_row = int(raw_input("Guess Row(Input 1-5): "))-1
        guess_col = int(raw_input("Guess Column(Input 1-5): "))-1

        count = count - 1
        print "You have %s guess left." % count

        if guess_row != ship_row or guess_col != ship_col:
            print "You missed."
            board[guess_row][guess_col] = "/"
        elif guess_row <= 0 or guess_col <= 0:
            print "Out of range"
        elif guess_row == ship_row or guess_col == ship_col:
            print "You've got it!"
            board[guess_row][guess_col] = "X"
            print_board()
            break
        else:
            print "Run out of guess!"
            break
        print_board()
    except:
        print "Out of range"
if count == 0:
    print "You have run out of guess!"
