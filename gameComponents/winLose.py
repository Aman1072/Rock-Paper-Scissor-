from gameComponents import gameVars

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    if status == "won":
        pre_message = "You are awesome player! "
    else:
        pre_message = "ohh you were not good in game! "

    print(pre_message + 'Would you like to play again?')

    choice = False

    while choice == False:
        choice = input("Y / N? ")

        if choice == "Y" or choice == "y":
            # reset the game loop and start over again
            gameVars.player_lives = gameVars.total_lives
            gameVars.computer_lives = gameVars.total_lives
            gameVars.player_choice = False
        elif choice == "N" or choice == "n":
            # exit message and quit
            print("You chose to quit. Better luck next time!")
            exit()
        else:
            print("Make a valid choice - Y or N")
            choice = False

   