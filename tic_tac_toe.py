board =  [["","",""]
        ,["","",""]
        ,["","",""]]

def print_board():
    print(board)

def is_finished():
    return False

def insert(row, column, player):
    board[row][column] = player

def turn():
    return "X"

def main():
    while not is_finished():
        player = turn()
        row = int(input("Which row do you want to input your " + player))
        column = int(input("Which column do you want to input your " + player))
        insert(row, column, player)
        print_board()


main()


# l = [1,2,3]
# l[0] = 3
# now list is 3,2,3

# print("x", "y)
        