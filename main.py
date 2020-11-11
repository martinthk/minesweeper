import math
import random

# Part A: Initial setup
def readBoard(fileName):
    # Description: this function takes the name of a file as input and produces a two- dimensional table (board) to represent this board as a list of lists.
    file = open(fileName,'r') # Open file 'fileName' for reading
    new_board = []
    for line in file:
        line = line.split() # Split each item by a ' '
        new_board.append(line) # Add each line to the board
    file.close()
    print(fileName, 'has been successfully read.') # Notify the user the file has successfully read
    return new_board

# Part B: Display
def printBoard(board):
    # Description: This function prints the contents of the board to the screen. It will replace ‘-‘ with spaces and emd with '|' in each item.
    # Empty board
    if len(board) == 0:
        for i in range (5):
            board.append(['-']*5)
    for rows in range(len(board)):
        print(rows,end='|')
        for cols in range(len(board[rows])):
            if (board[rows][cols] == '-'): # Replace '-' with spaces
                board[rows][cols] = ' '
            print(board[rows][cols],end = '|') # Seperate each item with "|"
        print()
    for cols in range (len(board[rows])+1):
        if cols == 0:
            print(' ',end='|')
        else:
            print(cols-1,end='|')
    print()


# Part C: File input/output
def saveBoard(fileName,board):
    # Description: This function writes the current board state in its original format to a fileName entered by the user.

    # Convert the whole table into str
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = str(board[row][col])

    file = open(fileName, 'w')  # Creating a file object with 'write' option

    # Iterating through the whole list
    for row in range(len(board)):
        for col in range(len(board[row])):
            file.write(board[row][col]) # Write one item at each time
        file.write("\n")    # Add a new line in the text file to separate each row
    file.close()    # Close the file at the end which can close all the access to the file
    print(fileName, 'has been successfully saved.') # Notify the user the file has successfully saved

# Part D: Menu
def menu():
    # Description: This function allows the user to choose from a set of options to perform
    selection = '0' # Defaulting the choice to be 0 when menu function being called
    board = []
    while selection != '6':
        print('What would you like to do?')
        print('1 - Read board')
        print('2 - Save board')
        print('3 - Printboard')
        print('4 - Minecount')
        print('5 - New board')
        print('6 - Quit')
        selection = input('?')

        # 1- Read board
        if selection == '1':
            fileName = input('Please enter a valid filename: ')
            board = readBoard(fileName)


        # 2- Save board
        elif selection == '2':
            fileName = input('Please enter a valid filename: ')
            saveBoard(fileName,board)

        # 3- Print board
        elif selection == '3':
            printBoard(board)

        # 4- Mine count
        elif selection == '4':
            printBoard(mineCount(board))

        # 5- New board
        elif selection == '5':
            board = newBoard()
            printBoard(board)

        # 6- Quit
        elif selection == '6':
            print('Thanks for playing, bye')

def mineCount(board):
    # Description: This function counts the neighbour mines
    # Strategy: Search through the whole list to find the mines first, then +1 to the eight neighbour.

    new_board = [] # Generating a new list

    # Generating a new board (list) with all value = 0
    for i in range (len(board)):
        new_board.append([0]* len(board[i]))

    # Iterate the board to find mind
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col] == 'x'):    # Check if the location contains mine
                new_board[row][col] = 'x'   # Change the value inside the new_board to 'x' if there is a mine

                # Get the neighbour index
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if not(col == 0 and row == 0):  # [0][0] will be itself so it has to be excluded
                            # n stands for neighbour
                            # Calculate the 8 possible combinations
                            n_row = row - x
                            n_col = col - y
                            if (n_row >= 0 and n_row < len(board) and n_col >= 0 and n_col < len(board[row])):  # Make sure the index is not out of the board
                                if not(board[n_row][n_col] == 'x'): # Exclude those mine next to each other
                                    new_board[n_row][n_col] += 1 # Add 1 to the neighbour
    return new_board

def newBoard():
    #Description: This function generate a new random board according to the user's input
    mines = 0
    new_board = [] # Resetting the list every time after newBoard() being called

    # Ask for user inputs
    size = int(input("Please enter a board size from 5 to 10: "))
    # Validate input: in the range of 5-10 inclusive and is an integer (cannot be a float)
    while (size < 5 or size > 10 or math.floor(size) != size):
        size = int(input("Please enter a board size from 5 to 10: "))

    mines = int(input("Please enter mines number less than size^2: "))

    # Validate input: in the range of 0 - size^ 2 exclusive and is an integer (cannot be a float)
    while (mines >= size ** 2 or mines <= 0 or math.floor(mines) != mines):
        mines = int(input("Please enter mines number less than size^2: "))

    # Generating a empty board according to the user's input
    for j in range(size):
        temp = [' '] * size
        new_board.append(temp)

    # Generating mines in random locations
    for i in range(mines):
        r_row = random.randint(0, size - 1) # Set the range 0 - (size - 1)
        r_col = random.randint(0, size - 1)
        check =False    # Resetting the check boolean to FALSE (default). This variable holds the status of checking repeated location.
        while not(check):   # This while loop is to ensure no repeated locations are ignored
            if (new_board[r_row][r_col] == 'x'):    # Keep generating a random location until there is a non-repeated location
                r_row = random.randint(0, size - 1)
                r_col = random.randint(0, size - 1)
            else:
                new_board[r_row][r_col] = 'x' # Place the mine inside the board
                check = True    # Change to TRUE after successfully placed a mine
    return new_board

### Main program ###
#board = []
menu()