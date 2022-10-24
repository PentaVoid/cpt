import random
import time

print("\nARGHH, WHAT THE-")
time.sleep(1.)
print("\nWAKE UP PUNK!")
time.sleep(1)
print("\nWhere am I... argh my head hurts...")
time.sleep(1.5)
print("\nYou are hear to play a good game of Russian Roullete, hahahah!\nTake this gun, its already loaded with 1 bullet HAHAHA!\nSpin the cylinder 1-4 times, and then fire!")
time.sleep(6)
print("\nWHAT, NOOO I'M TOO YOUNG TO DIE!, USER ITS UP TO YOU TO SAVE ME. CHOOSE A NUMBER, AND CHOOSE WISELY!")

user_choice = int(input("\nChoose the number of times the cylinder is spinned from 1-4: "))

while True:
  user_choice = int(input("\nChoose the number of times the cylinder is spinned from 1-4: "))
  muzzle = [1, 2, 3, 4]
  muzzle_random = random.choice(muzzle)
  print(muzzle_random)
  muzzle.remove(muzzle_random)
  print(muzzle)

  if user_choice == muzzle_random:
     print("YOU DIE!")
  else:
    print("Lucky, you live... ")

