# 1

import random

names = ["sai", "prudhvi", "mahesh", "mrudula"]

scores = {name: random.randint(1, 100) for name in names}
print(scores)

passed = {name: score for (name, score) in scores.items() if score > 60}
print(passed)

# 2 

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# 3

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)
