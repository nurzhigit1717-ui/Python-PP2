# Exercise 1
def squares_to_n(n):
    for i in range(n + 1):
        yield i * i


# Exercise 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# Exercise 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# Exercise 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


# Exercise 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


print("Exercise 1")
n = int(input("Enter N: "))
for x in squares_to_n(n):
    print(x)


print("Exercise 2")
n = int(input("Enter N: "))
print(",".join(str(x) for x in even_numbers(n)))


print("Exercise 3")
n = int(input("Enter N: "))
for x in divisible_by_3_and_4(n):
    print(x)


print("Exercise 4")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

for x in squares(a, b):
    print(x)


print("Exercise 5")
n = int(input("Enter N: "))

for x in countdown(n):
    print(x)