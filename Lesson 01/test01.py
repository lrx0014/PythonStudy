import math

# 1-1
print("1-1\n")
x = input("input x:")
print(int(x) // 100)
print(int(x) // 10 % 10)
print(int(x) % 10, "\n")

# 1-2
print("1-2\n")
x = input("input a b and theta:")
a, b, theta = map(float, x.split())
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(theta * math.pi / 180))
print("c=", c, "\n")

# 1-3
print("1-3\n")
s = input("x,y,z:")
x, y, z = s.split(',')
x, y, z = sorted([x, y, z])
print(x, y, z, "\n")
