import pyfiglet 
from rps import rps

cpt_text = pyfiglet.figlet_format("Welcome to AYO'S CPT")
print(cpt_text)
choose_game = input("Here is a list of the possible games to play. To choose one, simply type the corresponding digit:\n1. Rock Paper Scissors\n2. Roullete\n 3. Tic Tac Toe\4 Snake")
rps()

