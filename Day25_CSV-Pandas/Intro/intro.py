# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"]) # or print(data.condition) # these are case sensitive

# get data in row
print(data[data.day == "Monday"]) # day is monday
print(data[data.temp == data.temp.max()]) # max temperature

# create data from scratch
data_Dict1 = {
    "students": ["Sai", "pru", "Mah", "Mru"],
    "scores": [99, 97, 95, 92]
}
data1 = pandas.DataFrame(data_Dict1)
print(data1)
data1.to_csv("new_data.csv") # creates new csv file
