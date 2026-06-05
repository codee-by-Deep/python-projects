import random

def guessTheNumber():
   score = []
   x = random.randint(0,100)
   attempts = 0
   while True:
      n  = int(input("guess the number: "))
      attempts += 1
      if n == x:
         print("You Won!!")
         break
      elif n < x:
         print("Your number is smaller then secret value")
      elif attempts == 7:
         print("game over")
         break
      else:
         print("Your number is greater then secret value")
   
   score.append(attempts)

guessTheNumber()
