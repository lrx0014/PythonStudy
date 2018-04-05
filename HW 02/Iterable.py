import time

myarr = []
_first = 0
_last = 0


def init_list(first, last):
    global myarr
    myarr = list(range(first, last))
    global _first
    _first = first
    global _last
    _last = last


def timer(func, n, arr):
    start = time.time()
    i = n
    while i > 0:
        func(arr[:])
        i = i - 1
    end = time.time()
    _name = getattr(func, '__name__')
    _time = '%.5f' % (end - start)
    print('{:<10}:{time} => [{first},...,{last}]'.format(
        _name, time=_time, first=_first, last=_last))


# for循环加10
def add_for(arr):
    for i in range(len(arr) - 1):
        arr[i] = arr[i] + 10
    return arr

# for循环绝对值
def abs_for(arr):
    for i in range(len(arr) - 1):
        arr[i] = abs(arr[i])
    return arr


# 列表表达式加10
def add_comp(arr):
    return [n + 10 for n in arr]

# 列表表达式绝对值
def abs_comp(arr):
    return [abs(n) for n in arr]

# map加10
def add_map(arr):
    return map(lambda n: n + 10, arr)

# map绝对值
def abs_map(arr):
    return map(lambda n: abs(n), arr)

# 生成器函数加10
def add_gen(arr):
    g = (n + 10 for n in arr)
    for i in range(len(arr) - 1):
        arr[i] = next(g)

# 生成器函数绝对值
def abs_gen(arr):
    g = (abs(n) for n in arr)
    for i in range(len(arr) - 1):
        arr[i] = next(g)

# 生成器加10
def add_genfun(arr):
    for n in arr:
        yield n + 10

# 生成器绝对值
def abs_genfun(arr):
    for n in arr:
        yield abs(n)


n = input("输入测试次数：")
first = input("输入测试序列的开始数：")
last = input("输入测试序列的结束数：")
init_list(int(first), int(last))
n = int(n)

timer(add_for, n, myarr[:])
timer(abs_for, n, myarr[:])
timer(add_comp, n, myarr[:])
timer(abs_comp, n, myarr[:])
timer(add_map, n, myarr[:])
timer(abs_map, n, myarr[:])
timer(add_gen, n, myarr[:])
timer(abs_gen, n, myarr[:])
timer(add_genfun, n, myarr[:])
timer(abs_genfun, n, myarr[:])
