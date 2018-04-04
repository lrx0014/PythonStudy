from functools import reduce


def BlackHole(n):
    result = []
    for i in range(10**(n - 1), 10**n):
        a = [int(c) for c in str(i)]
        a.sort()
        s1 = reduce(lambda x, y: 10 * x + y, a[::-1])
        s2 = reduce(lambda x, y: 10 * x + y, a)
        if (s1 - s2 == i):
            result.append(i)
    return result


for n in BlackHole(3):
    print(n)
