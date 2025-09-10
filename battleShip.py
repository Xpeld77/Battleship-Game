import random
totalScore = 0

def addShip(board, numShips):
    """ Function Description:
            Randomly places the specified number of ships ('S') on the board.
        Parameter(s): 
            board : The list of lists representing the game board
            numShips [int]: The number of ships that user wants on the board
        Return: None   
    """
    size = len(board)
    ships = 0
    while ships < numShips:

        #Generates random row and column coordinates within the given board range
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

        #Ship is placed only if the selected cell is empty
        if board[row][col] == '~':
            board[row][col] = 'S'
            ships += 1
    return board

def checkSetUpError(size, numShips):
    """ Function Description:
            Validates user input for the size of the board and the number of ships.
        Parameter(s): 
            size [int]: The size of the board
            numShips [int]: The number of ships
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """
    #Check if board is within valid range
    if not (2 <= size <= 5):
        return True #Error if board size is outside valid range
    
    maxShips = (size * size) - 2
    
    #Check if number of ships is within valid range
    if not (1 <= numShips <= maxShips):
        return True #Error if number of ships is outside valid range
    
    return False #False if there are no errors

def checkFireError(board, row, col):
    """ Function Description:
            Validates user input for the coordinates to shot a ship
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return [Boolean]: Return True if an error is found or False if there is no error.   
    """
    size = len(board)
    #Check if coordinates are within valid board range
    if not (0 <= row < size) or not (0 <= col < size):
        print('Error: Coordinates are out of bounds. Please re-enter the coordinates')
        return True
    #Check if the cell at the coordinates has already been targeted
    if board[row][col] == 'X' or board[row][col] == 'O':
        print('Error. You have already fired at these coordinates')
        return True
    
    return False #If no errors, the shot is valid

def createBoard(size):
    """ Function Description:
            Creates a size-by-size game board initialized with '~'
        Parameter(s):
            size [int]: The size of the board which will be used to create a board of size x size
                        Example: size 2 will create [ ['~', '~'], ['~', '~']]
        Return: board which is a list of lists  
    """
    board = []
    
    #Iterates each row and appends "~" to the current row list, then appends the row to the board list
    for i in range(size):
        row = []
        for j in range(size):
            row.append('~') 
        board.append(row)
    return board

def displayBoard(board, round=True):
    """ Function Description:
            Displays the current state of the board.  If round is True then print out the current
            state of the board without showing the ships 'S'.  Else round is False then print out the
            current state of the board showing hits 'X', misses 'O', ships that have not been hit 'S'
            and everything else '~'.
        Parameter(s):
            board : The list of lists representing the game board.
            round [Boolean] : True if you are print the board after each shot and False to display
            the end of a round version.  Default value of True.
        
        Return: None  
    """
    for row in board:
        rows = []
        for cell in row:
            if round:
                #During the round show '~' for ships, 'X' for hits, 'O' for misses
                if cell == 'S':
                    rows.append('~')
                else:
                    rows.append(cell)
            else:
                #At the end of the round show 'X' for hits, 'O' for misses and 'S' for unhit ships
                rows.append(cell)
        print(" ".join(rows))

def fireShot(board, row, col):
    """ Function Description:
            Marks a shot on the board.
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return[Boolean]: Return True if a ship was hit and False if the shot missed a ship.     
    """ 
    #If the shot at the given coordinates is a ship, the cell will change to 'X' to mark a hit 
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return True
    
    #If the shot at the given coordinates isnt a ship, the cell will change to 'O' to mark a miss
    else: 
        board[row][col] = 'O'
        return False

def playRound(board, numShips):
    """ Function Description:
            Main logic for playing one round 
        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships
        Return [int]: The number of hits (ships that were hit) for the round.   
    """
    shots_left = numShips 
    hits = 0

    print(f'Start of the round: You have {shots_left} shots')

    while shots_left > 0:
        shot = input('Enter the coordinates for your shot (e.g., 3 1): ').split()
        row, col = int(shot[0]), int(shot[1])

        #validate the shot using checkFireError
        if checkFireError(board, row, col):
            print('Invalid shot. Please try again.')
            continue

        #Fire the shot using the fireShot function
        if fireShot(board, row, col):
            print(f'Shot {numShips - shots_left + 1} is a hit!')
            hits += 1
        else:
            print(f'Shot {numShips - shots_left + 1} is a miss!')
        
        #Display the board after each shot
        displayBoard(board)

        shots_left -= 1
    
    print('End of the round:')
    displayBoard(board, round=False) #Display final board with the ships and shots at the end of the round

    return hits

def main():  
    """ Function Description:
            Play the game in a designated number of rounds and present the final score to the user.
            You can not change the code in the main function.  If student changes the main function code
            then they will lose 25 marks.
        Parameter(s): No parameters
        Return: None  
    """
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
            
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return

if __name__ == '__main__':
    main()
