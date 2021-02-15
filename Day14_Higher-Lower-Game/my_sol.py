from random import choice
from art import logo, vs
from game_data import data
from replit import clear

print(logo)

rand_a = choice(data)
rand_b = choice(data)

game_over = False
count = 0

while not game_over:
  print(f"Compare A: {rand_a['name']}, a {rand_a['description']}, from {rand_a['country']}.")
  print(vs)
  print(f"Compare B: {rand_b['name']}, a {rand_b['description']}, from {rand_b['country']}.")
  ans = input("Who has more followers? 'A' or 'B': ").lower()
  clear()
  if (rand_a['follower_count'] > rand_b['follower_count'] and ans == "a") or rand_a['follower_count'] < rand_b['follower_count'] and ans == "b":
    count += 1
    print(logo)
    print(f"You're right! Current Score: {count}")
    rand_a = rand_b
    rand_b = choice(data)
  else:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {count}")
    game_over = True
