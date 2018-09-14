import random

def splashscreen():
  print("\n" * 20)
  print("\
            ____   __    ___  __ _              \n\
           (  _ \ /  \  / __)(  / )             \n\
            )   /(  O )( (__  )  (              \n\
           (__\_) \__/  \___)(__\_)             \n\
         ____   __   ____  ____  ____           \n\
        (  _ \ / _\ (  _ \(  __)(  _ \          \n\
         ) __//    \ ) __/ ) _)  )   /          \n\
        (__)  \_/\_/(__)  (____)(__\_)          \n\
   ____   ___  __  ____  ____   __  ____  ____  \n\
  / ___) / __)(  )/ ___)/ ___) /  \(  _ \/ ___) \n\
  \___ \( (__  )( \___ \\___ \(  O ))   /\___ \ \n\
  (____/ \___)(__)(____/(____/ \__/(__\_)(____/ \n\
               CHEAT EDITION!!!")
  print("\n\n\n")
splashscreen()

playerwins = 0
aiwins = 0
choices = ['rock','paper','scissors']

difficulty = input("Select a difficulty:\nEasy\nMedium\nHard\n ")
if difficulty.lower() == "easy":
  max = 60
elif difficulty.lower() == "medium":
  max = 40
elif difficult.lower() == "hard":
  max = 20

def choose(choices):
  playerupper = input("Choose here: ")
  player = playerupper.lower()
  if player not in choices:
    ("Not a choice!")
    choose(choices)
  else:
    return player

def decide(choices,max,aiwins,playerwins):
  playerchoice = choose(choices)
  aichoice = random.choice(choices)
  if random.randint(1,max) == 1:
    cheat = True
  else:
    cheat = False
  #draw condition
  if playerchoice == aichoice and cheat != True:
    print("It's a draw!")
  #player wins
  elif playerchoice == 'rock' and aichoice == 'scissors' and cheat != True:
    print("You chose rock, which beats ai scissors!")
    playerwins += 1
  elif playerchoice == 'paper' and aichoice == 'rock' and cheat != True:
    print("You chose paper, which beats ai rock!")
    playerwins += 1
  elif playerchoice == 'scissors' and aichoice == 'paper' and cheat != True:
    print("You chose scissors, which beats ai paper!")
    playerwins += 1
  #cheating AI wins  
  elif playerchoice == 'rock' and cheat == True:
    print("You chose rock, which is beaten by ai paper!")
    aiwins += 1
  elif playerchoice == 'paper' and cheat == True:
    print("You chose paper, which is beaten by ai scissors!")
    aiwins += 1
  elif playerchoice == 'scissors' and cheat == True:
    print("You chose scissors, which is beaten by ai rock!")
    aiwins += 1

  #Player loses
  elif playerchoice == 'rock' and aichoice == 'paper':
    print("You chose rock, which is beaten by ai paper!")
    aiwins += 1
  elif playerchoice == 'paper' and aichoice == 'scissors':
    print("You chose paper, which is beaten by ai scissors!")
    aiwins += 1
  elif playerchoice == 'scissors' and aichoice == 'rock':
    print("You chose scissors, which is beaten by ai rock!")
    aiwins += 1
  print("Your Score: " + str(playerwins) + " : " + str(aiwins) + " :AI Score")
  decide(choices,max,aiwins,playerwins)
  return

def play():
  decide(choices,max,aiwins,playerwins)
play()
