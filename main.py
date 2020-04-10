from random import randint

#For this program to work, user input must start with a capital case. For example: "Rock", not "rock"

def main():

  rounds = 3

  while rounds > 0:

    userInput = input("Rock Paper Scissors? ")

    computer = randint(0,2)

    if computer == 0 and userInput =="Rock":
      print("AI Chose Rock. It's a tie")
    elif computer == 0 and userInput =="Scissors":
      print("AI Chose Rock. You Lost")
    elif computer == 0 and userInput =="Paper":
      print("AI Chose Rock. You Won")
   
    elif computer == 1 and userInput =="Paper":
      print("AI Chose Paper. It's a tie")
    elif computer == 1 and userInput =="Scissors":
      print("AI Chose Paper. You Lost")
    elif computer == 1 and userInput =="Rock":
      print("AI Chose Paper. You Won")

    elif computer == 2 and userInput =="Scissors":
      print("AI Chose Scissors. It's a tie")
    elif computer == 2 and userInput =="Paper":
      print("AI Chose Scissors. You Lost")
    elif computer == 2 and userInput =="Rock":
      print("AI Chose Scissors. You Won")
    
    else:
      print("error")

    rounds = rounds - 1

main()

