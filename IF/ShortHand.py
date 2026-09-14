a = 5
b = 2
if a > b: print("a is greater than b")

c = 2
d = 330
print("C") if c > d else print("D")


e = 330
f = 330
print("E") if e > f else print("=") if e == f else print("F")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)