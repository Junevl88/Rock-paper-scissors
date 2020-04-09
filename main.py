from random import randint

def main():

  rounds = 3

  while rounds > 0:

    userInput = input("Rock Paper Scissors? ")

    computer = randint(0,2)

    if computer == 0 and userInput =="Rock":
      print("AI Chose Rock. It's a tie")
      print(computer)
    elif computer == 0 and userInput =="Scissors":
      print("AI Chose Rock. You Lost")
      print(computer)
    elif computer == 0 and userInput =="Paper":
      print("AI Chose Rock. You Won")
      print(computer)
    
    if computer == 1 and userInput =="Paper":
      print("AI Chose Paper. It's a tie")
      print(computer)
    elif computer == 1 and userInput =="Scissors":
      print("AI Chose Paper. You Lost")
      print(computer)
    elif computer == 1 and userInput =="Rock":
      print("AI Chose Paper. You Won")
      print(computer)

    if computer == 2 and userInput =="Scissors":
      print("AI Chose Scissors. It's a tie")
      print(computer)
    elif computer == 2 and userInput =="Scissors":
      print("AI Chose Scissors. You Lost")
      print(computer)
    elif computer == 2 and userInput =="Scissors":
      print("AI Chose Scissors. You Won")
      print(computer)

    rounds = rounds - 1

main()
