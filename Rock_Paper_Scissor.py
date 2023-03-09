import random

NAME = input("welcome for rock scissor game.enter your name please:")

while True:
    my_choices = ["rock", "paper", "scissor"]
    computer_choices = random.choice(my_choices)
    player = None
    while player not in my_choices:
        player = input("enter any one from,\"paper,scissor,rock\":").lower()
    if player == computer_choices:
        print("player:" + player)
        print("computer:" + computer_choices)
        print("both are tie {}".format(NAME))
    elif player == "paper":
        if computer_choices == "scissor":
            print("player:" + player)
            print("computer:" + computer_choices)
            print("you lose {}".format(NAME))
        if computer_choices == "rock":
            print("player:" + player)
            print("computer:" + computer_choices)
            print("you won {}".format(NAME))
    elif player == "scissor":
        if computer_choices == "rock":
            print("player:" + player)
            print("computer:" + computer_choices)
            print("you lose {}".format(NAME))
        if computer_choices == "paper":
            print("player:" + player)
            print("computer:" + computer_choices)
            print("you won {}".format(NAME))
    elif player == "rock":
        if computer_choices == "scissor":
            print("player:" + player)
            print("computer:" + computer_choices)
            print("you lose {}".format(NAME))
        if computer_choices == "paper":
            print("player:" + player)
            print("computer:" + computer_choices)
            print("you won {}".format(NAME))
    playagain = input("do you want to play again?(yes)/(no)").lower()
    if playagain != "yes":
        break
print("bye hope you enjoyed this game")