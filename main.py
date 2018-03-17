from random import *

class Game:
  def __init__(self, userScore, npcScore):
    self.userScore = userScore
    self.npcScore = npcScore
    
  def setNPCInput(self):
    return randint(1,3)
    
  def setUserInput(self):
    done = False
    while not(done):
      userInput = raw_input("Rock, paper, scissors, shoot!\nEnter your choice: ")
      userNum = toNum(userInput)
      if userNum != -1:
        done = True
      else:
        print "It looks like you didn't enter a valid choice. Try again.\n"
    return userNum
  
  def getWinner(self, npc, user):
    if abs(npc-user) == 1:
      if npc > user:
        self.npcScore+=1
        return "NPC wins..."
      else:
        self.userScore+=1
        return "You win!"
    if abs(npc-user) == 2:
      if npc < user:
        self.npcScore+=1
        return "NPC wins..."
      else:
        self.userScore+=1
        return "You win!"
    if npc-user == 0:
      return "It's a tie!"
  
#####

def toString(input):
  if input == 1:
    return "rock"
  elif input == 2:
    return "paper"
  elif input == 3:
    return "scissors"
  else:
    return "Error"

def toNum(input):
  if input.lower() == "rock":
    return 1
  elif input.lower() == "paper":
    return 2
  elif input.lower() == "scissors":
    return 3
  else:
    return -1
    


#####

game = Game(0,0)
keepPlaying = True
while keepPlaying:
  user = game.setUserInput()
  npc = game.setNPCInput()
  print "\nThe NPC chooses " + toString(npc) + "."
  print game.getWinner(npc, user)
  print "Your score: " + str(game.userScore)
  print "NPC score: " + str(game.npcScore)
  
  enterYN = False
  while not enterYN:
    userCont = raw_input("\nPlay again? (Y/N) \n>")
    if userCont.lower() == "n":
      enterYN = True
      keepPlaying = False
      print "\nThanks for playing!"
    elif userCont.lower() == "y":
      enterYN = True
      print "\nOkay, here we go again!\n"
      print "#############\n"
    else:
      print "Error, unexpected input."


  
  
