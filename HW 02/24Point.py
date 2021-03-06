import itertools
import random


# 洗牌函数
def shuffle(n, m=-1):
    if m == -1:
        m = n
    _list = list(range(n))
    for i in range(len(_list) - 1):
        x = random.randint(i, len(_list) - 1)
        _list[x], _list[i] = _list[i], _list[x]
        if i == m - 1:
            break
    return [_list[ind] for ind in range(n) if ind >= 0 and ind < m]


# 获取随机的四张牌
def AquireCards():
    _card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    _card_shu = shuffle(52, 4)
    return [_card[ind] for ind in _card_shu]


# 通过排列组合permutations获取所有可能的表达式
def TryExpressions(_cards, ops):
    # expr = []
    try:
        while True:
            _list = list(next(ops)) + _cards
            its = itertools.permutations(_list, len(_list))
            try:
                while True:
                    yield next(its)
            except StopIteration:
                pass
    except StopIteration:
        pass


# 遍历所有表达式判断是否能够凑出24点
def GetResult(expr, isPrint=False):
    opm = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / (b + 0.0)
    }
    exp_stack = []
    while expr:
        t = expr.pop(0)
        if type(t) == int:
            exp_stack.append(t)
        else:
            if len(exp_stack) < 2:
                return False
            else:
                a = exp_stack.pop()
                b = exp_stack.pop()
                if isPrint:
                    print(a, t, b, '=', opm[t](a, b))
                try:
                    exp_stack.append(opm[t](a, b))
                except ZeroDivisionError:
                    return False
    return exp_stack[0]


if __name__ == '__main__':
    _cards = AquireCards()
    print('随机生成四张牌：', _cards)
    ops = itertools.combinations_with_replacement('+-*/', 3)
    allExpr = TryExpressions(_cards, ops)
    isWin = False
    for expr in allExpr:
        result = GetResult(list(expr))
        if result and result == 24:
            GetResult(list(expr), True)
            print('你赢了!!')
            isWin = True
            break
    if isWin is False:
        print('无法凑出24点！！')
