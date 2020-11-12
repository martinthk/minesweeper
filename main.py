import math
import random

# Task 1
# Create a menu
def menu():
    # Description: This function allows the user to choose from a set of options to perform
    selection = '0'  # Defaulting the choice to be 0 when menu function being called
    userBoard = []  # Tracks all the users' play entries
    mineBoard = []  # Contains all the mins and the mine count

    while selection != '6':
        print()
        print('What would you like to do?')
        print('1 - Read board')
        print('2 - New board')
        print('3 - Minecount')
        print('4 - Play')
        print('5 - Brute force')
        print('6 - Quit')
        selection = input('?')

        # 1- Read board
        if selection == '1':
            fileName = input('Please enter a valid filename: ')
            mineBoard = readBoard(fileName)

        # 2- New board
        elif selection == '2':
            userBoard = []
            mineBoard = newBoard()
            for i in range(len(mineBoard)):
                temp = [' ']*len(mineBoard)
                userBoard.append(temp)
            printBoard(userBoard)

        # 3- Mine count
        elif selection == '3':
            printBoard(mineCount(mineBoard))

        # 4- Play
        elif selection == '4':
            mineBoard = mineCount(mineBoard)
            play(userBoard,mineBoard,0,0)

        # 5- Brute force
        elif selection == '5':
            mineBoard = bruteForce(mineBoard)

        # 6- Quit
        elif selection == '6':
            print('Thanks for playing, bye')



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

def newBoard():
    #Description: This function generate a new random board according to the user's input
    mines = 0
    new_board = [] # Resetting the list every time after newBoard() being called

    # Ask for user inputs
    size = int(input("Please enter a board size from 2 to 10: "))
    # Validate input: in the range of 5-10 inclusive and is an integer (cannot be a float)
    while (size < 2 or size > 10 or math.floor(size) != size):
        size = int(input("Please enter a board size from 2 to 10: "))

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

def printBoard(board):
    # Description: This function prints the contents of the board to the screen. It will replace ‘-‘ with spaces and emd with '|' in each item.
    # Empty board
    if len(board) == 0:
        for i in range (5):
            board.append([' ']*5)

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

# Part 2A: Check Function
def check(userBoard, mineBoard):
    # Descriptions: takes userBoard and mineBoard and checks if the user wins, loses or is still playing
    lose = False
    win = False

    # Check loses
    # lose when userBoard contains an 'x'
    for rows in range (len(userBoard)):
        for cols in range(len(userBoard[rows])):
            if userBoard[rows][cols] == 'x':
                lose = True

    # Check wins
    # win if all empty squares have been revealed in userBoard
    if win == False and lose == False:
        empty = 0
        mines = 0
        for row in range(len(userBoard)):
            empty += userBoard[row].count(' ')  # Count how many empty squares
            mines += mineBoard[row].count('x')  # Count how many mines in the board
        if empty == mines:  # Win if no of empty squares left = no of mines in the board
            win = True

    if lose == True:
        return -1   # Return -1 if the user loses
    elif win == True:
        return 1    # Return 1 if the user wins
    else:
        return 0    # Return 0 if still playing

# Part 2B: Play
def play(userBoard, mineBoard,row,col):
    # Description: take the row and col as input from the user and update userBoard with what is present at that location
    # a number 0-8 or an ‘x’.
    while check(userBoard,mineBoard) == 0:
        # Take input from player
        row = int(input('row: '))
        col = int(input('col: '))
        print()
        # Update userBoard with what is present at that location
        value = mineBoard[row][col]
        userBoard[row][col] = value
        printBoard(userBoard)
        # using check() to update player's progress
        condition = check(userBoard,mineBoard)
        if condition == -1:
            print('you lose')
            print()
            printBoard(mineBoard)
        elif condition == 1:
            print('you win')
            print()
            printBoard(mineBoard)

# Part 3B: Implementation
def bruteForce(mineBoard):
    mines = 0   # Keep track no of mines
    size = len(mineBoard) # Store the size of the board
    # Start with a empty board
    for i in range (size):
        mines += mineBoard[i].count('x')    # Count how many mines before empty the list

    t = Subset(size*size,mines)
    for item in t:
        temp = slice(item,size)
        printBrute(temp)
        if temp == mineBoard:
            print('Correct')
            return temp
        else:
            print('Incorrect')
            print('==>')
            print()

def slice(aList,size):
    # Description: This function will convert a list to board by slicing
    l = []
    start = 0   # Initial start index with 0
    base = size # base stores how much items each row has in a board
    end = size  # Initial end with the size
    while end <= len(aList):
        l.append(aList[start:end])
        start = end
        end = base + end  # e.g. 3x3: 3 -> 6 -> 9
    return l

def dec2bin_bits(dec, bitlength):
    # Description: Convert dec to bin
    if bitlength:
        l = [0] * bitlength
    k = -1
    while dec>0:
        l[k] = dec%2
        dec = dec//2
        k -= 1
    return l

def Subset(n,mines):
    # Description: Generate all subsets in n
    l = []
    for k in range(2**n):
        temp = dec2bin_bits(k,n)
        # Only append solutions with exact same no of mines
        if temp.count(1) == mines:
            l.append(temp)
    return l

def printBrute(board):
    # Description: Print function for brute force
    for rows in range(len(board)):
        print(rows, end='|')
        for cols in range(len(board[rows])):
            if (board[rows][cols] == 0):  # Replace '-' with spaces
                board[rows][cols] = ' '
            else:
                board[rows][cols] = 'x'
            print(board[rows][cols], end='|')  # Seperate each item with "|"
        print()

    for cols in range(len(board[rows]) + 1):
        if cols == 0:
            print(' ', end='|')
        else:
            print(cols - 1, end='|')
    print()


### Main ###
menu()
