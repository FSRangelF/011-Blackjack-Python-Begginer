from os import cpu_count
#import art
import random

Cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def score_calc(card_list):
  score = 0
  for card in card_list:
    if card == "A":
      if score + 11 > 21:
        score += 1
      else:
        score += 11
    elif card == "J" or card == "Q" or card == "K":
      score += 10
    else:
      score += card
  if score == 21 and len(card_list) == 2:
    return "BLACKJACK"
  else:
    return score

def compare(player_score, cpu_score):
  if player_score == cpu_score:
    return "Draw!"
  elif cpu_score > 21 or player_score == "BLACKJACK":
    return "You Win!"
  elif player_score > 21 or cpu_score == "BLACKJACK":
    return "You Lose!"
  elif player_score > cpu_score:
    return "You Win!"
  else:
    return "You Lose!"

restart = 'y'
while restart != 'n':
  #print(art.logo)
  print("logo")

  #First deal
  player_hand = [random.choice(Cards), random.choice(Cards)]
  cpu_hand = [random.choice(Cards), random.choice(Cards)]

  #Initial Statement
  print(f"Your Cards: {player_hand}")
  print(f"Computer firt card: {cpu_hand[0]}")

  #Player hand check
  choice = input("Type 'y' to get another card, type 'n' to pass: ")
  while choice == 'y' and score_calc(player_hand) < 21:
    player_hand.append(random.choice(Cards))
    print(f"Your Cards: {player_hand}")
    choice = input("Type 'y' to get another card, type 'n' to pass: ")

  #CPU hand check
  if score_calc(cpu_hand) != "BLACKJACK":
    while score_calc(cpu_hand) < 17:
      cpu_hand.append(random.choice(Cards))

  #Final Check
  player_final_score = score_calc(player_hand)
  cpu_final_score = score_calc(cpu_hand)
  print(f"Your final hand: {player_hand} ---> {player_final_score}")
  print(f"Computer´s final hand: {cpu_hand} ---> {cpu_final_score}")

  print(compare(player_final_score,cpu_final_score))

  #New game check
  restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  print("\n"*10)
