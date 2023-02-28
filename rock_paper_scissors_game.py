import random
def get_choices():
  player_choice = input("Enter your choice of either: Rock, Paper or Scissors:\n ").lower()
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  
  result = {"player1": player_choice, "player2": computer_choice}
  return (result)

def who_wins(player1, player2):
  print(f"Your selection is {player1} and the computer choice is {player2}\n")
  if (player1 == player2):
      print("Its a draw. Play again.")
  elif (player1 == "rock"):
    if (player2 == "scissors"):
      print("The Rock will smash the scissors. Hence You won.")
    else:
      print("The paper will cover the rock. Hence Computer won, You lose")
  elif (player1 == "paper"):
    if (player2 == "scissors"):
      print("The scissors will cut paper. Hence computer won, You lose")
    else:
      print("The paper will cover the rock. Hence You won.")
  elif (player1 == "scissors"):
    if (player2 =="paper"):
      print("The scissors will cut the paper. Hence You won")
    else:
      print ("The Rock will smash the scissors, Hence the Computer won, You lose")
  else:
    print("Your entered value is incorrect. Check your spellings of PAPER/ROCK/SCISSORS and try again. Thank you." )
  
game_test = get_choices()
testing = who_wins(game_test["player1"], game_test["player2"])
