import math
import random

# 3-4
print("3-4")
print('1+2+3+...+100=', sum(range(1, 101)), '\n')

# 3-5
print("3-5")
a_list = ['a', 'b', 'c', 'abc']
i = 0
for ele in a_list:
    print('No.', i, ele)
    i += 1
print('\n')

# 3-6
print("3-6")
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
print('\n')

# 3-7
print("3-7")
for i in range(100, 1000):
    x, y, z = map(int, str(i))
    if x**3 + y**3 + z**3 == i:
        print(i)
print('\n')

# 3-8
print("3-8")
score = [70, 80, 90, 100, 120]
print(sum(score) / len(score))

# 3-9
print("3-9")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, '\t', end=' ')
    print('\n')

# 3-10
print("3-10")
for i in range(200, 0, -1):
    if i % 17 == 0:
        print(i)
        break

# 3-11
print("3-11")
n = input("input X:")
n = int(n)
m = math.ceil(math.sqrt(n) + 1)
for i in range(2, m):
    if n % i == 0 and i < n:
        print("NO")
        break
    else:
        print("YES")
        break
print("\n")

# 3-12
print("3-12")
for chick in range(0, 31):
    if 2 * chick + (30 - chick) * 4 == 90:
        print("Chick:", chick, "Rabbit:", 30 - chick, '\n')

# 3-13
print("3-13")
digits = (1, 2, 3, 4)
for i in digits:
    for j in digits:
        if j == i:
            continue
        for k in digits:
            if k == i or k == j:
                continue
            print(i * 100 + j * 10 + k, end=' ')
print('\n')

# 3-14
print("3-14")
x = []
while True:
    if len(x) == 20:
        break
    n = random.randint(1, 100)
    if n not in x:
        x.append(n)
print(x, '\n')

# 3-15
print("3-15")


def Cni(n, i):
    if not (isinstance(n, int) and isinstance(i, int) and n >= i):
        print("ERROR")
        return
    result = 1
    Min, Max = min(i, n - 1), max(i, n - 1)
    for i in range(n, 0, -1):
        if i > Max:
            result *= i
        elif i <= Min:
            result /= i
    return result


print(Cni(6, 2), '\n')

# 3-16
print("3-16")


def bank(base, rate, days):
    result = base
    times = 365 // days
    for i in range(times):
        result = result + result * rate / 365 * days
    return result


print(bank(100000, 0.0385, 14))
