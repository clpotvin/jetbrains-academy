def print_board():
    print("---------")
    print("|", brd[0][0], brd[0][1], brd[0][2], "|")
    print("|", brd[1][0], brd[1][1], brd[1][2], "|")
    print("|", brd[2][0], brd[2][1], brd[2][2], "|")
    print("---------")


def check_end():
    x_count = 0
    o_count = 0

    for i in brd:
        for j in i:
            if j is 'X':
                x_count += 1
            if j is 'O':
                o_count += 1

    x_win = False
    o_win = False

    if brd[0][0] == brd[1][1] == brd[2][2] == 'X' or brd[0][2] == brd[1][1] == brd[2][0] == 'X':
        x_win = True
    elif brd[0][0] == brd[1][1] == brd[2][2] == 'O' or brd[0][2] == brd[1][1] == brd[2][0] == 'O':
        o_win = True
    else:
        for i in range(3):
            if (brd[i][0] == brd[i][1] == brd[i][2] == 'X' or
                    brd[0][i] == brd[1][i] == brd[2][i] == 'X'):
                x_win = True
            elif (brd[i][0] == brd[i][1] == brd[i][2] == 'X' or
                  brd[0][i] == brd[1][i] == brd[2][i] == 'O'):
                o_win = True

    if x_win:
        print('X wins')
        return True
    elif o_win:
        print('O wins')
        return True
    elif not x_win and not o_win and x_count + o_count == 9:
        print('Draw')
        return True
    else:
        return False


def player_move(player):
    valid = False
    row = -1
    col = -1

    while valid is False:
        coords_str = input("Enter coordinates (Separated by a Space): ")
        coords = coords_str.split()

        try:
            row = int(coords[0])
            col = int(coords[1])

            if 0 < row < 4 and 0 < col < 4:
                if brd[row - 1][col - 1] is ' ' or brd[row - 1][col - 1] is '_':
                    if player is 'X':
                        brd[row - 1][col - 1] = 'X'
                    else:
                        brd[row - 1][col - 1] = 'O'
                    valid = True
                else:
                    print('This cell is occupied! Choose another one!')
                    valid = False
            else:
                print("Coordinates should be from 1 to 3!")
                valid = False
        except:
            print('You should enter numbers!')
            valid = False

    print_board()


brd = [[' ', ' ', ' '],
       [' ', ' ', ' '],
       [' ', ' ', ' ']]

print_board()

while True:
    player_move('X')
    if check_end() is True:
        break
    player_move('O')
    if check_end() is True:
        break
