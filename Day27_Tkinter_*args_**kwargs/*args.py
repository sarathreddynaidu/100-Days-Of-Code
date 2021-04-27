# *args: Positional Variable-Length Arguments

def my_func(*args):
    for n in args:
        print(n)

my_func(1, 2, 3)
my_func(10, 45)

# add
def add(*args):
    sol = 0
    for n in args:
        sol += n
    print(sol)

add(10, 45)
add(4, 5)
