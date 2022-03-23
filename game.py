# Import packages to extend Python (just like we extend Sublime, Atom, or VSCode )
from random import randint

# [] => this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

# True or false are boolean data types 
# essentially, booleans are equivalent to an on or off switch, 1 or 0.
player_choice = False

#define a win or lose function
def winorlose(status):
    #version 1 of function
    #print("Inside winorlose function; status is: ", status)
    print("You", status, "! Would you like to play again?")
    choice = input("Y / N? ")

    if choice == "N" or choice == "n":
        print("You chose to quite! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":
        #reset the player lives and computer lives 
        #and reste player choices to False, so our loop restarts
        global player_lives
        global computer_lives
        global total_lives

        player_lives = total_lives
        computer_lives = total_lives
    else:
        print("Make a valid choice - Y or N")
        #this might generate a bug that we need to fix later 
        choice = input("Y / N?")         

# plyer_chioce == False
while player_choice is False:
    print("=========================*/ RPS GAME */==========================")
    print("Computer Lives:", computer_lives, "/", total_lives)
    print("Player Lives:", player_lives, "/", total_lives)
    print("==============================================")
    #Version 1, to explain array indexing
    #player_chioce = choices[1]
    #print("index 1 in the chice array is " + player_chioce + ", which is paper")

    player_chioce = input("Choose rock, paper, scissors: \n ")
    #player_choice now equals TRUE -> it has a value

    print("user chose" + player_chioce)

    # this will be the AI choice -> a random pick from the choices array 
    computer_chioce = choices [randint(0,2)]

    print("computer chose: " + computer_chioce)

    if computer_chioce == player_chioce:
        print("tie")

    elif computer_chioce == "rock":
        if player_chioce == "scissors":
            print("you lose!")
        else:
            print("you win")    
            #verbose way
            # player_lives = plyer_lives - 1
            #simplified way
            computer_lives -= 1    

    elif computer_chioce == "paper":
        if player_chioce == "scissors":
            print("you win!")
        else:
            print("you lose!")    
            player_lives -= 1

    elif computer_chioce == "scissors":
        if player_chioce == "paper":
            print("you lose!")
        else:
            print("you win")    
            computer_lives -= 1

    elif computer_chioce == "rock":
        if player_chioce == "paper":
            print("you win!")
        else:
            print("you lose!")    
            player_lives -= 1

    elif computer_chioce == "scissors":
        if player_chioce == "rock":
            print("you win!")
        else:
            print("you lose!")    
            player_lives -= 1 

    elif computer_chioce == "paper":
        if player_chioce == "rock":
            print("you lose!")
        else:
            print("you win")    
            computer_lives -= 1               

    if player_lives == 0:
        winorlose("lose")
        
    if computer_lives == 0:
        winorlose("won")
       
    print("Player lives:", player_lives)
    print("Computer lives:", computer_lives)

    # map the loop keep running, by setting player_cioce back to False 
    # unset, so that our loop condition will evaluate to True
    player_chioce = False 




