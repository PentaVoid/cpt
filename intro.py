import pyfiglet 
import time
from rps import rps
from roullete import roullete

cpt_text = pyfiglet.figlet_format("Welcome to AYO'S CPT")
print(cpt_text)

while True:
  choose_game = input("\n\n\nHere is a list of the possible games to play. To choose one, simply type the corresponding digit:\n\n1. Rock Paper Scissors\n2. Russian Roullete\n3. Tic Tac Toe\n4. Snake\nType any other number or key to exit\nchoice: ")

  if choose_game == "1":
    print("\nChosen Game: Rock Paper Scissors\n\n\n")
    time.sleep(1)
    rps()
  elif choose_game == "2":
    print("Chosen Game: Russian Roullette\n\n\n")
    time.sleep(2)
    roullete()
  elif choose_game == "3":
    print("Chosen Game: Tic Tac Toe\n\n\n")
    time.sleep(2)
    roullete()
  elif choose_game == "4":
    print("Chosen Game: Snake\n\n\n")
    time.sleep(2)
    roullete()

  else:
    print("\n\n\nThanks for playing Ayo's CPT")
    time.sleep(1)
    print("Have a great day Miss Pozzebon!")
    print("\nInfo:\n\nLibraries Used:\nPyfiglet for fancy text\nTime library for delayed text\nRandom Library for randomizing computer choice")
    break
