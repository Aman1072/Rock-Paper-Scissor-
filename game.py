# Import packages to extend Python (just like we extend Sublime, Atom, or VSCode )
from random import randint

# [] => this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

#Version 1, to explain array indexing
#player_chioce = choices[1]
#print("index 1 in the chice array is " + player_chioce + ", which is paper")

player_chioce = input("Choose rock, paper, scissors: ")

print("user chose" + player_chioce)

# this will be the AI choice -> a random pick from the choices array 
computer_chioce = choices [randint(0,2)]

print("computer chose: " + computer_chioce)

if computer_chioce == player_chioce:
    print("tie")

elif computer_chioce == "rock":
    if player_chioce == "scissors":
        print("you lose!")

elif computer_chioce == "paper":
    if player_chioce == "scissors":
        print("you win!")

elif computer_chioce == "scissors":
    if player_chioce == "paper":
        print("you lose!")


