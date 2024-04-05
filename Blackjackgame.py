import random
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cardplay = random.choice(cards)
  return cardplay
  
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards):
  """Takes a list of cards and returns input"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) >21:
    cards.remove(11)
    cards.append(1)
  return sum(cards) 
  
def compare(user_score, computer_score):
  if computer_score == user_score:
    return "draw"
  elif computer_score == 0:
    return "You lose,computer wins!"
  elif user_score == 0:
    return "You win!"
  elif user_score > 21:
    return "You lose,computer wins"
  elif computer_score >21:
    return "You win!"
  if user_score > computer_score:
    return "You win"
  else:
    return "Try your luck next time!"
  
def replay():
  """Start over"""
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards{user_cards}, your score:{user_score}")
    print(f"Computer first card:{computer_cards[0]},")
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over = True
    else:
      replay=input("Do you want to draw another card?Type'y' to go ahead or 'n' to pass")
      if replay == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
    while computer_score !=0 and computer_score <17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
  print(f"Your final hand:{user_cards}, Your final score:{user_score}")
  print(f"Computer final hand:{computer_cards}, Computer final score:{computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack?Type 'y' to play or 'n' to end.") =='y':
  replay()
  