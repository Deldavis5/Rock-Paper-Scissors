import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors:) ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choice = {"player" : player_choice , "computer" : computer_choice}
  return choice

def check_winner(player, computer):
  print (f"Player chose {player} and Computer chose {computer}.")
  if player == computer:
    return "It's a tie!"
  elif player == "rock" and computer == "scissors":
    return "Rock smashes scissors! You Win!"
  elif player == "rock" and computer == "paper":
    return "Paper covers rock. You Lose whomp whomp"
  elif player == "paper" and computer == "rock":
    return "Paper covers rock! You Win!"
  elif player == "paper" and computer == "sissors":
    return "Scissors cuts paper. You lose. whomp whomp"
  elif player == "scissors" and computer == "rock":
    return "Rock smashes scissors. You Lose whomp whomp"
  elif player == "scissors" and computer == "paper":
    return "Scissors slices paper. You Win!"
  
  
choice = get_choices()
result = check_winner(choice["player"], choice["computer"])
print(result)
