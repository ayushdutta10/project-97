import random

secret_number = random.randint(1, 9)

chances_left = 5

for i in range(1, 6):
  guess = int(input("Take a guess: "))
  
  # checking
  if guess < secret_number:
    print("Guess is too low!")
  elif guess > secret_number:
    print("Guess is too high!")
  else:
    break

  chances_left = chances_left - 1
  print(chances_left)

if guess == secret_number:
  print("you won congratulations! ! !")
else:
  print("You lose the number is!"+secret_number)