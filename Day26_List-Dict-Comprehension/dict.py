import random

names = ["sai", "prudhvi", "mahesh", "mrudula"]

scores = {name: random.randint(1, 100) for name in names}
print(scores)

passed = {name: score for (name, score) in scores.items() if score > 60}
print(passed)
