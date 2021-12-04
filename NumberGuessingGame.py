import random

secret number = random.randint(1, 9)

chances left = 5

for i in range(1, 6):
  guess = int(input("Take a guess: "))
  
  # checking
  if guess < secret_number:
    print("Guess is too low!")
  elif guess > secret number:
    print("Guess is too high!")
  else:
    break

  chances left = chances left - 1
  print(chances left)

if guess == secret number:
  print("you won congratulations! ! !")
else:
  print("You lose the number is!"+secret number)