import time

myarr = list(range(-5000, 5000))
_first = myarr[0]
_last = myarr[len(myarr) - 1]


def timer(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    _name = getattr(func, '__name__')
    _time = end - start
    print('{:<10}:{time} => [{first},...,{last}]'.format(
        _name, time=_time, first=_first, last=_last))


def add_for(arr):
    for i in range(len(arr) - 1):
        arr[i] = arr[i] + 10
    return arr


def abs_for(arr):
    for i in range(len(arr) - 1):
        arr[i] = abs(arr[i])
    return arr


def add_comp(arr):
    return [n + 10 for n in arr]


def abs_comp(arr):
    return [abs(n) for n in arr]


def add_map(arr):
    return map(lambda n: n + 10, arr)


def abs_map(arr):
    return map(lambda n: abs(n), arr)


def add_gen(arr):
    g = (n + 10 for n in arr)
    for i in range(len(arr) - 1):
        arr[i] = next(g)


def abs_gen(arr):
    g = (abs(n) for n in arr)
    for i in range(len(arr) - 1):
        arr[i] = next(g)


def add_genfun(arr):
    for n in arr:
        yield n + 10


def abs_genfun(arr):
    for n in arr:
        yield abs(n)


timer(add_for, myarr[:])
timer(abs_for, myarr[:])
timer(add_comp, myarr[:])
timer(abs_comp, myarr[:])
timer(add_map, myarr[:])
timer(abs_map, myarr[:])
timer(add_gen, myarr[:])
timer(abs_gen, myarr[:])
timer(add_genfun, myarr[:])
timer(abs_genfun, myarr[:])
