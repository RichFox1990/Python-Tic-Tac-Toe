from time import sleep
import itertools


def checkWin(listName, location, number):
    """When funtion is called it pulls the 3 defined variables:
        'listName' define the list name to check that list of numbers to see if they are all the same (a win for a player)
        'location' define the location of the win (i.e. row, column, diagonally) for the print statement below
        'number' define the value of the winning row/column/diagonal for the print statement below
        **(check the   'win()'    function slightly below for example of its use)**  """
    if listName.count(listName[0]) == len(listName) and listName[0] != 0:
        ##This is saying-
        """take the first value in the defined list ('listName[0]') and count up how many times that value is in the list.
        if that  "==EQUALS==""  the total amount numbers in the list ('len(listName)')
        "AND"  the value of the items in list are not 0      THEN SOMEBODY HAS WON!        
        (0 would mean nobody has played there, we wouldnt want '[0, 0, 0]' becoming a win)
        """
        print("\nCongratulations!", current_player, "\nYou have won at", location, number)
        # Pull variables from above to print winner and the location of the win
        return True
        """returns 'True' so can be used to set another variable to 'True' in the main code (i.e. if checkwin() == True:
                                                                                                     game_won = True)"""
    else:
        return False
        # If no winners it returns 'False' so main code can continue to ask for player input etc. as above

def checkDraw():
    draw = []
    for n, row in enumerate(game):
        for r in row:
            draw.append(r)
    if draw.count(0) == 0:
        return True
    else:
        return False


def win():
    #HORIZONTAL CHECK
    for n, row in enumerate(game): 
        """ 'n' is set as the current iteration value of the 'for' loop (which always starts at '0', and in this case, ends on '2' 
            (Because [game] has '3' items in it's list to iterate through)
            'row' is equal to the value of each item in the list 'game' in this case an entre row. 
             For example: on the first iteration, the value of 'row' would be the first row e.g. [1, 0, 0] if someone has played A1 in game"""
        if checkWin(row, "row", n+1):
            """ This takes the values (row and n) from the above 'for' loop at every iteration '(0, 1, 2)'' and checks the 'row' numbers in the function.
                The first iteration would take first row of game, second would take the second row, and so on] 
                We take the value on 'n+1' instead of 'n' because our display of the board is '1, 2, 3' not '0, 1, 2' 
                So when is prints the winner, the value of the winning 'row' matches for the players display of the board"""
            return True
            # return a 'True' value to let the game code know there has been a winner

    #VERTICAL CHECK
    for col in range(len(game)):
        """'col' is set as the iteration value of the length of 'game'.   'game' has 3 items. 
            So 'col' will first equal '0' then '1' then '2' """
        check = []
        #Creating a list we will use to check for a winner
        for row in game:
            check.append(row[col])
        if checkWin(check, "column", col+1):
            #as previous in HORIZONTAL
            return True
            #as previous in HORIZONTAL

    #DIAGONAL CHECK 
    diag = []
    for ix in range(len(game)): 
        #Iterates through range of game and sets ix as that value, length of 'game' is 3.. so 'ix' becomes 0 then 1 then 2)
        diag.append(game[ix][ix]) 
        #'ix' numeric value substituted into function above. the value at that location in the 'game' list is put into the 'diag' list
    if checkWin(diag, "diagonally", "\\"):
        #Calling function 'checkWin' to see if the values in the 'diag' list are the same and not equal to 0
        return True
        #as previous in HORIZONTAL
    diag = []
    for diagcol, diagrow in enumerate(reversed(range(len(game)))):
        """diagcol's value = the iteration number of the for loop
           (in this case the length of the game list (which is 3, so diagcol value starts at 0 and ends at 2)
           diagrow == the function or main reference... in this case reverse number iteration of length of game. which is (2, 1, 0)"""
        diag.append(game[diagrow][diagcol]) 
        """This substitutes in the values of 'diagrow' and 'diagcol' and adds the numbers at that location in 'game' to the 'diag' list.
           The 3 locations it will grab the value from are ([0, 2], [1, 1], [2, 0])  --  diagnol top left to bottom right on the board"""
    if checkWin(diag, "diagonally", "/"):
        #as previous in HORIZONTAL
        return True
        #as previous in HORIZONTAL
    return False
        
abc = ["A", "B", "C", "D", "E", "F", "G"]

def checkGameInput(player_input, current_player):
    if len(player_input) == 2:
        try:
            for n, char in enumerate(player_input):
                if n == 0:
                    row = abc.index(char.upper())
                elif n == 1 and int(char) > 0:
                    column = int(char) - 1
                else:
                    print("wrong format, Try Again")
                    return False
        except:
            print("That Entry is not recognised, Try Again")
            return False
        if game[row][column] == 0:
            game[row][column] = current_player
            return True
        else:
            print("A player has already played there, Try another Input", row, column)
            return False
    else:
        print("Wrong Input, Try Again")
        return False


def playerNames(list, player):
    player = input(f"{player}'s name is: ")   
    confirm = input(f"Hi ,{player}.. did I say that right?\n    (y/n): ")
    while not confirm.lower() in ("y", "yes"):
        player = input(f"Whoops, excuse me!\nYour name is: ")
        confirm = input(f"Ok, So your name is {player}?\n    (y/n): ")
    else:
        print("Setting name as", player, "\n")
        list.append(player)


def inputSizeCheck():
    done = "no"
    while not done == "yes":
        inputOK = ""
        while inputOK != "yes":
            n = input("What grid size would you like to play with?\nFor Example: Enter '3' for a regular 3x3 : ")
            if len(n) == 1:
                try:
                    n = int(n)
                    if n<=2:
                        print("You can count higher than that ;) Let's go bigger!\n3 or above")
                        continue
                    elif n>2 and n<=7:
                        InputOK = "yes"
                        break
                    elif n >7:
                        print("I've got things to do, I'm not sticking around for that long :o...\n7 or below please")
                        continue
                except:
                    print("Make sure you enter a number\n")
                    continue
            else:
                print("Please enter a single number between 3 and 7")
        confirm = ""
        while confirm.lower() not in ("y", "yes"):
            confirm = input(f"\nAre you sure you want your game to be {n}x{n}?\n    (y/n): ")
            if confirm.lower() in ("y", "yes"):
                print("Ok, Let's begin")
                done = "yes"
                break
            elif confirm.lower() in ("n", "no"):
                break
            else:
                print("Please enter a valid input (y/n)")
                continue
    return n

def playAgain():
    play = input("\nWould you like to play again (y/n): ")
    while not play.lower() in ("y", "n"):
        play = input("\nInvalid input... Would you like to play again (y/n): ")
    if play.lower() == "y":
        return True
    elif play.lower() == "n":
        return False

def buildGameBoard(size):
    for i in range(size):
        row = []
        for i in range(size):
            row.append(0)
        game.append(row)


def displayGame(size):
    s = " "
    for n in range(size):
        s += "  "+str(n+1)
    print(s)
    for iteration, row in enumerate(game):
        print(abc[iteration], row)

"""------------------------------------------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------------"""

players = []
playerNum = [1, 2]

play = True
print("Welcome to my Tic Tac Toe Game!\n\nLet's start with player names\n")
playerNames(players, "Player 1")
playerNames(players, "Player 2")
game = []
size = inputSizeCheck()
buildGameBoard(size)
while play:
    game_won = False
    player_choice = itertools.cycle(players)
    while not game_won:
        displayGame(size)
        current_player = next(player_choice)
        print("\nIts",current_player,"'s turn")
        played = False
        while not played:
            player_input = input("\nWhere do you want to play?\n    : ")
            played  = checkGameInput(player_input, playerNum[0])
        if win():
            game_won = True
            if playAgain():
                play = True
            else:
                play = False
        if checkDraw():
            print("It's a stalemate\n")
            game_won = True
            if playAgain():
                play = True
            else:
                play = False
        playerNum.reverse()
    players.reverse()
    game = []
    buildGameBoard(size)