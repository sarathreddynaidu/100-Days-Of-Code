#Method 1
# file = open("data.txt")
# content = file.read()
# print(content)
# file.close()

#Method 2
with open("data.txt") as file:
    content = file.read()
    print(content)
