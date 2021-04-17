#Overwrite
with open("data.txt", mode="w") as file:
    file.write("Name: Sai""\nAge: 24")

#Append
with open("data.txt", mode="a") as file:
  file.write("\nCity: Austin")
