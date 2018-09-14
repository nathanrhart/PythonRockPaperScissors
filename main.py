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
  (____/ \___)(__)(____/(____/ \__/(__\_)(____/ \n")
  print("\n\n\n")
splashscreen()

#Choices:
choices = ['rock','paper','scissors']
playerwins = 0
aiwins = 0

def ai():
  aichoice = random.choice(choices)
  return aichoice

def play(playerwins,aiwins):
  aichoice = ai()
  playerchoice = input("Type your choice here: ")
  if playerchoice in choices:
    if playerchoice == aichoice:
      print("It's a draw!")
      play(playerwins,aiwins)
      return
    elif playerchoice == 'rock' and aichoice == 'scissors':
      print("You chose rock, which beats ai scissors!")
      playerwins += 1
    elif playerchoice == 'rock' and aichoice == 'paper':
      print("You chose rock, which is beaten by ai paper!")
      aiwins += 1
    elif playerchoice == 'paper' and aichoice == 'rock':
      print("You chose paper, which beats ai rock!")
      playerwins += 1
    elif playerchoice == 'paper' and aichoice == 'scissors':
      print("You chose paper, which is beaten by ai scissors!")
      aiwins += 1
    elif playerchoice == 'scissors' and aichoice == 'paper':
      print("You chose scissors, which beats ai paper!")
      playerwins += 1
    elif playerchoice == 'scissors' and aichoice == 'rock':
      print("You chose scissors, which is beaten by ai rock!")
      aiwins += 1
    print("Your Score: " + str(playerwins) + " : " + str(aiwins) + " :AI Score")
    play(playerwins,aiwins)
    return
    
  else:
    print("That's not a choice!")
    play(playerwins,aiwins)
    return

play(playerwins,aiwins)

