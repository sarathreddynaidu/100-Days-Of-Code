import random

print("I'm thinking of a number between 1 and 100 (both included).")
diff = input("Easy or Hard: ").lower()
num = random.randint(1, 100)
print(num)
def guess(diff):
  if diff == "easy":
    limit = 10
  elif diff == "hard":
    limit = 5
  count = 0
  got = 1
  while count <= limit:
    print(f"You have {limit} attempts remaining")
    guess = int(input("Make a guess: "))
    if guess > num:
      limit -= 1
      got += 1
      print("Too High")
    elif guess < num:
      limit -= 1
      got += 1
      print("Too low")
    elif guess == num:
      print(f"You got it in {got} turns! The number is {num}.")
      limit = 0
      break
    if limit == 0:
      print(f"You Lose! The number is {num}")
      break
    print("Guess again")
guess(diff)
