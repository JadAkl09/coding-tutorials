board =  [["","",""] 
        ,["","",""] 
        ,["","",""]]

turns = 0

def print_board():
    print(board)
 
def is_finished():
    for i in range(2):
        if check_line(board[i]):
            return True
    # get columns
    # [ x for x in y ]
    # name_of_the_list[integer]

    # 1 
    get_column = lambda i: [ row[i] for row in board ]
    # 2
    # def get_column(i):
    #     l = []
    #     for row in board:
    #         l.append(row[i])        

    # get_column(0) gives 0th column
    columns = [ [ row[i] for row in board ] for i in [0,1,2]]
    # check all the columns
    
    for column in columns:
        if check_line(column):
            return True
        
    # method 1 of getting diagonals
    # diagonals = [[ board[0][0], board[1][1], board[2][2]], [board[2][0],board[1][1],board[0][2]]]  
    
    # method 2 of getting diagonals
    
    diagonals = [[], []]
    for i in range(3):
        diagonals[0].append(board[i][i])
        diagonals[1].append(board[i][2-i])
    
    for diagonal in diagonals:
        if check_line(diagonal):
            return True
    
    return turns == 9


def check_line(line):
    return line == ["X","X","X"] or line == ["O","O","O"]
    

def insert(row, column, player):
    global turns
    if board[row][column] == "":
        board[row][column] = player
        turns += 1
        return True
    return False

def turn():
    if turns % 2 == 0:
        return "X"
    else:
        return "O"

def row_column(player):
    row = int(input("Which row do you want to input your " + player + "? "))
    column = int(input("Which column do you want to input your " + player + "? "))
    return (row, column)
        
def single_digit(player):
    place = int(input("Where do you want to put your " + player + "? "))
    row = (place - 1) // 3
    column = (place - 1) % 3 
    return (row, column)



def main():
    print("Welcome do Tic-Tac-Toe.")
    # ask player for the game mode
    game_mode = input("The default game mode is giving a single digit, if you want to change the game mode press 'Y', otherwise press any other key.  ")
    while not is_finished():
        player = turn()
        # get the identifier of a square
        row, column = row_column(player) if game_mode == "Y" else single_digit(player)    
        if insert(row, column, player):
            print_board()
        else:
            print('This place is already taken.')
            

main()

# Ideas for game improvement:
# 1. Print a nice 'game over' message at the end and announe which player won.
# 2. Print a 2 dimensional board instead of a list.
# 3. Simplify is_finished() to get rid of repeated code and reduce the number of lines