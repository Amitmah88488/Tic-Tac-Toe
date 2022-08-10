from random import randrange

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
Hello world

    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   ", board[row][col], "   ", sep="", end="")  # Getting list values of board
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    valid = False  # to check users input and initiate the loop

    while not valid:
        user_input = input("Enter your move: ")
        valid = len(user_input) == 1 and user_input >= '1' and user_input <= '9'  # check value is in range
        if not valid:
            print("Input not in range")
            continue
        move = int(user_input) - 1  # starts from 0 so -1
        row = move // 3  # which row does it contain in example :(3-1//3)=0 meaning first row
        col = move % 3  # column example (8-1%3)=1 so second column

        sign = board[row][col]  # getting the current value of to check
        valid = sign not in ["X", "O"]
        if not valid:
            print("Already used ")
            continue
        board[row][col] = "O"  # change the value in board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ["X", "O"]:
                free.append((r, c))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if sign == "X":
        who = "me"
    if sign == "O":
        who = "you"
    cross1 = cross2 = True

    # for sides
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        if board[rc][rc] != sign:
            cross1 = False
        if board[2 - rc][2 - rc] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    freelist = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        r, c = freelist[this]
        board[r][c] = "X"


board[1][1] = "X"
display_board(board)
free = make_list_of_free_fields(board)
humanturn = True
while len(free):
    display_board(board)
    if humanturn:
        enter_move(board)
        victor = victory_for(board, "O")
    else:
        draw_move(board)
        victor = victory_for(board, "X")
    if victor != None:
        break
    humanturn = not humanturn
    free = make_list_of_free_fields(board)

if victor == 'you':
    display_board(board)
    print("You won!")

elif victor == 'me':
    display_board(board)
    print("I won")

else:
    display_board(board)
    print("Draw!")


