# Import packages to extend Python (just like we extend Sublime, Atom, or VSCode )
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose

while  gameVars.player_choice is False:
    print("*****************************/ RPS GAME */*****************************")
    print("Computer Lives:", gameVars.computer_lives, "/",  gameVars.total_lives)
    print("Player Lives:",  gameVars.player_lives, "/",  gameVars.total_lives)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #Version 1, to explain array indexing
    #player_chioce = choices[1]
    #print("index 1 in the chice array is " + player_chioce + ", which is paper")
    
    print("Choose your weapon! Or type quit to exit\n")

    gameVars.player_chioce = input("Choose rock, paper, scissors: \n ")
    #player_choice now equals TRUE -> it has a value

    if  gameVars.player_chioce == "quit":
        print("You chose to quit")
        exit()

    print("user chose" +  gameVars.player_chioce)

    # this will be the AI choice -> a random pick from the choices array 
    gameVars.computer_chioce = gameVars.choices [randint(0,2)]

    print("computer chose: " +  gameVars.computer_chioce)

    if  gameVars.computer_chioce ==  gameVars.player_chioce:
        print("tie")

    elif  gameVars.computer_chioce == "rock":
        if  gameVars.player_chioce == "scissors":
            print("you lose!")
        else:
            print("you win")    
            #verbose way
            # player_lives = plyer_lives - 1
            #simplified way
            gameVars.computer_lives -= 1    

    elif  gameVars.computer_chioce == "paper":
        if  gameVars.player_chioce == "scissors":
            print("you win!")
        else:
            print("you lose!")    
            gameVars.player_lives -= 1

    elif  gameVars.computer_chioce == "scissors":
        if  gameVars.player_chioce == "paper":
            print("you lose!")
        else:
            print("you win")    
            gameVars.computer_lives -= 1

    elif  gameVars.computer_chioce == "rock":
        if  gameVars.player_chioce == "paper":
            print("you win!")
        else:
            print("you lose!")    
            gameVars.player_lives -= 1

    elif  gameVars.computer_chioce == "scissors":
        if  gameVars.player_chioce == "rock":
            print("you win!")
        else:
            print("you lose!")    
            gameVars.player_lives -= 1 

    elif  gameVars.computer_chioce == "paper":
        if  gameVars.player_chioce == "rock":
            print("you lose!")
        else:
            print("you win")    
            gameVars.player_lives -= 1               

    if  gameVars.player_lives == 0:
        winLose.winorlose("lose")
        
    if  gameVars.computer_lives == 0:
        winLose.winorlose("won")
       
    print("Player lives:",  gameVars.player_lives)
    print("Computer lives:",  gameVars.computer_lives)

    # map the loop keep running, by setting player_cioce back to False 
    # unset, so that our loop condition will evaluate to True
    gameVars.player_chioce = False 



