import random
from art import logo
import clear 

def difficulty_level():
  difficult=input("Please choose a difficulty. Type 'easy' or 'hard': ")
  if difficult == "easy":
    difficult=10
  elif difficult == "hard":
    difficult=5
  return difficult

def give_random_num():
  number=random.randint(1,100)
  return number
  
def start(num,dif):
  while dif >0:
    guess=int(input("Make a guess: "))
    if guess == num:
      return "Congratulations!! you are won"
    elif guess > num:
      print("To hight")
      dif-=1
      print(f"you have {dif} attempt remaining to guess the number.\n ")
    elif guess < num:
      dif-=1
      print("To low")
      print(f"you have {dif} attempt remaining to guess the number.\n ")
      
  return "You are lost"
      
      
      
  







Start_game=True

while Start_game == True:
  print(logo)
  
  print("Welcome to the number guessing game! \n I'm thinking of a number between 1 to 100")
  
  difficult=difficulty_level()
  print(f"you have {difficult} attempt remaining to guess the number.\n ")
  number=give_random_num()
  print(start(number,difficult))
  
  again=input("do you want to run the game again? 'yes' or 'no': ")
  if again == "no":
    print("goodbye, see you soon! ")
    break
  
    
  
  
    
  










