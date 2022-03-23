# board = [[0, 0, 0, 0, "x"],
#          [0, 0, 1, 0, 0],
#          [0, 0, 0, 2, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0]]

# added comment
# board = [[1, 4, 7, 10], [12, 9, 2, 5], [3, 6, 11, 8]]
board = []


def create_board(row, col, x, y):
    global cell_size
    for a in range(row):
        board.append([])
        for _ in range(col):
            board[a].append(0)

    board[len(board) - y][x - 1] = 1

    if row >= 4 or col >= 4:
        cell_size = 1
    elif row > 9 or col > 9:
        cell_size = 2
    else:
        cell_size = 0


def number_of_moves(x, y):
    positions = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
    moves = 0
    temp = 0

    for a in range(len(positions)):
        for b in range(2):
            positions[a][b] += [x, y][b]

    for z in positions:
        try:
            if z[0] < 0 or z[1] < 0:
                raise IndexError
            temp = board[z[0]][z[1]]
            moves += 1
        except IndexError:
            continue

    return moves


def possible_moves(x, y):
    positions = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
    moves_dictp = {}
    moves = 0
    temp = 0

    # for xc in range(len(board)):
    #     for yc in range(len(board[0])):
    #         if type(board[xc][yc]) == int:
    #             if board[xc][yc] > last_index:
    #                 last_index = board[xc][yc]

    for a in range(len(positions)):
        for b in range(2):
            positions[a][b] += [x, y][b]

    for z in positions:
        try:
            if z[0] < 0 or z[1] < 0:
                raise IndexError
            elif board[z[0]][z[1]] != 0:
                raise IndexError
            elif board[z[0]][z[1]] == 0:
                temp = board[z[0]][z[1]]
                moves_dictp[tuple(z)] = 0
        except IndexError:
            continue

    for z in positions:
        try:
            if z[0] < 0 or z[1] < 0:
                raise IndexError
            temp = board[z[0]][z[1]]
            moves += 1
        except IndexError:
            continue

    for x in moves_dictp.keys():
        moves_dictp[x] = number_of_moves(x[0], x[1])

    return moves_dictp


def next_title():
    for x in possible_moves(-1, -1):
        if board[x[0]][x[1]] == 0:
            return x[0], x[1]
        else:
            return None, None


def print_board():
    this_row = ""
    for x in board:
        for y in x:
            if y == 0:
                this_row += " __"
            elif y == "x":
                this_row += " _X"
            elif y == "O":
                this_row += " _O"
            else:
                this_row += " {}".format(y)
        print(this_row)
        this_row = ""
    print("\n")


def print_status():
    row_length = len(board)
    col_length = len(board[0])
    line_length = (col_length * (cell_size + 2)) + 3
    cell_str = [["_ ", "__ ", "___ "], ["X ", " X ", "  X "], ["{} ", " {} ", "  {} "]]
    cell_space = [" ", "  ", "   "]
    print(" " + "-" * line_length)

    for x in range(row_length):
        this_row = ""
        for y in board[x]:
            if y == 0:
                this_row += cell_str[0][cell_size]
            elif y == 'x':
                this_row += cell_str[1][cell_size]
            elif y == "*":
                this_row += cell_str[2][cell_size].format(y)
            elif type(y) == int:
                if len(str(y)) == 1:
                    this_row += " " + str(y) + " "
                elif len(str(y)) == 2:
                    this_row += str(y) + " "
        print(f"{row_length - x}| {this_row}|")

    columns = ''

    if cell_size > 0:
        columns = " "
        for x in range(col_length):
            columns += str(x + 1) + cell_space[cell_size]
    else:
        columns = " "
        for x in range(col_length):
            columns += str(x + 1) + "  "

    print(" " + "-" * line_length)
    print(f'   {columns}')


def print_status_playing():
    row_length = len(board)
    col_length = len(board[0])
    line_length = (col_length * (cell_size + 2)) + 3
    cell_str = [["_ ", "__ ", "___ "], ["X ", " X ", "  X "], ["{} ", " {} ", "  {} "]]
    cell_space = [" ", "  ", "   "]
    print(" " + "-" * line_length)

    for x in range(row_length):
        this_row = ""
        for y in board[x]:
            if y == 0:
                this_row += cell_str[0][cell_size]
            elif xc == x and yc == board[x].index(y):
                this_row += cell_str[1][cell_size]
            else:
                this_row += cell_str[2][cell_size].format(y)

        print(f"{row_length - x}| {this_row}|")

    columns = ''

    if cell_size > 0:
        columns = " "
        for x in range(col_length):
            columns += str(x + 1) + cell_space[cell_size]
    else:
        columns = " "
        for x in range(col_length):
            columns += str(x + 1) + "  "

    print(" " + "-" * line_length)
    print(f'   {columns}')


def zero_in_board():
    for row in board:
        if 0 in row:
            return True
    else:
        return False


def solve():
    global board
    last_index = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] > last_index:
                last_index = board[x][y]
                xc, yc = x, y

    for move in possible_moves(xc, yc):
        if board[move[0]][move[1]] == 0:
            board[move[0]][move[1]] = last_index + 1
        if solve():
            return True
        board[move[0]][move[1]] = 0

    if zero_in_board():
        return False
    else:
        return True


def set_next_move():
    while True:
        try:
            a, b = [int(x) for x in str(input("Enter your next move: ")).split()]
            pos = (len(board) - b, a - 1)
            if pos in moves_dict.keys():
                break
            else:
                raise ValueError
        except ValueError:
            while True:
                try:
                    a, b = [int(x) for x in str(input("Invalid move! Enter your next move: ")).split()]
                    pos = (len(board) - b, a - 1)
                    if pos in moves_dict.keys():
                        break
                    else:
                        raise ValueError
                except ValueError:
                    continue
            break
    clean_board()
    board[pos[0]][pos[1]] = last_index + 1


def clean_board():
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != "*" and board[x][y] != last_index:
                board[x][y] = 0
            elif board[x][y] == last_index:
                board[x][y] = "*"


def play_game():
    global last_index, moves_dict, xc, yc
    max_moves = len(board) * len(board[0])
    moves_dict = {}
    last_index = 0

    while True:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if type(board[x][y]) == int:
                    if board[x][y] > last_index:
                        last_index = board[x][y]
                        xc, yc = x, y
                        break

        moves_dict = possible_moves(xc, yc)
        for x in moves_dict.keys():
            board[x[0]][x[1]] = moves_dict[x]
        print_status_playing()
        if last_index == max_moves or not moves_dict:
            break
        set_next_move()

    checking = []
    for x in board:
        for y in x:
            checking.append(y)

    for x in checking:
        if x != "*" and x != max_moves:
            print("No more possible moves!")
            moves = 0
            for y in board:
                moves += y.count("*")
            print(f"Your knight visited {moves} squares!")
            break
    else:
        print("What a great tour! Congratulations!")


def game():
    global board
    while True:
        try:
            dim_x, dim_y = [int(x) for x in str(input("Enter your board dimensions: ")).split()]
            if dim_x <= 0 or dim_y <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid dimensions!")
    while True:
        try:
            a, b = [int(x) for x in str(input("Enter the knight's starting position: ")).split()]
            if a <= 0 or b <= 0:
                raise ValueError
            elif a > dim_x or b > dim_y:
                raise ValueError
            break
        except ValueError:
            print("Invalid dimensions!")
    while True:
        try:
            create_board(dim_x, dim_y, a, b)
            break
        except IndexError:
            print("Invalid dimensions!")

    original_board = [x.copy() for x in board]
    ans = str(input("Do you want to try the puzzle? (y/n): "))
    if ans == "y":
        if solve():
            board = original_board
            play_game()
        else:
            print("No solution exists!")
    elif ans == "n":
        if solve():
            print("Here's the solution!")
            print_status()
        else:
            print("No solution exists!")


if __name__ == "__main__":
    game()
