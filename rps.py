import random
import time

def rps():
    wins = 0
    losses = 0
    ties = 0

    time.sleep(2)
    while True:
        choices = ["Computer plays ROCK!","Computer plays PAPER!","Computer plays SCISSORS"]
        user_choice = input("Enter " + "\u001b[1m" + "R " + "\u001b[0m" + "for rock, " + "\u001b[1m" + "P " + "\u001b[0m" + "for paper, and " "\u001b[1m" + "S " + "\u001b[0m" + "for scissors.\nIf you would like to quit, type " + "\u001b[1m" + "exit: ")
        print("\u001b[0m")
    
        computer_choice = random.choice(choices)
        if computer_choice[15].lower() == user_choice.lower():
            print(computer_choice)
            time.sleep(0.5)
            print("Tie!\n")
            ties += 1
        elif user_choice.lower() == "r":
            if computer_choice[15].lower() != "p":
                print(computer_choice)
                time.sleep(0.5)
                print("You Win!\n")
                wins +=1
    
            else:
                print(computer_choice)
                time.sleep(0.5)
                print("You lose!\n")
                losses += 1
        elif user_choice.lower() == "p":
            if computer_choice[15].lower() != "s":
                print(computer_choice)
                time.sleep(0.5)
                print("You win!\n")
                losses += 1
    
            else:
                print(computer_choice)
                time.sleep(0.5)
                print("You lose!\n")
                wins += 1
    
        elif user_choice.lower() == "s":
            if computer_choice[15].lower() != "r":
                print(computer_choice)
                time.sleep(0.5)
                print("You win!\n")
                wins += 1
    
            else:
                print(computer_choice)
                time.sleep(0.5)
                print("You lose!\n")
                losses += 1
    
        elif user_choice.lower() == "exit".lower():
                print("\nThanks for playing\n")
                time.sleep(1)
                print("Game Stats loading")
                time.sleep(1)
                print("25% LOADED..")
                time.sleep(1)
                print("50% LOADED...")
                time.sleep(1)
                print("100% LOADED....\n\n")
                time.sleep(1)
                print("\033[1m" + "STATS" + "\033[0m")
                print("Wins:", wins)
                print("Losses:", losses)
                print("Draws:", ties)
                time.sleep(2)
                break

