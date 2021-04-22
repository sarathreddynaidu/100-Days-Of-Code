# with for loop
# nums = [1, 2, 3]
# new_nums = []
# for n in nums:
#     add_1 = n + 1
#     new_nums.append(add_1)
# print(new_nums)

# using list comprehension
nums = [1, 2, 3]
new_nums = [n+1 for n in nums]
print(new_nums)

# also works for strings
name = "sarath"
new = [n for n in name]
print(new)

# with range
new = [n*2 for n in range(1, 5)]
print(new)

# conditional list comprehension
names = ["sai", "prudhvi", "mahesh", "mrudula"]
new_names = [name.upper() for name in names if len(name) < 7]
print(new_names)
