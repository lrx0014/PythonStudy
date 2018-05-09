import re

def count(path):
    txt = open(path, 'r').read()
    _A_Z = len(re.compile(r'[A-Z]').findall(txt))
    _a_z = len(re.compile(r'[a-z]').findall(txt))
    _num = len(re.compile(r'[0-9]').findall(txt))
    _other = len(txt) - _A_Z - _a_z - _num
    print("Upper: ", _A_Z)
    print("Lower: ", _a_z)
    print("Number: ", _num)
    print("Other: ", _other)


def replace_hi(path1, path2):
    old_txt = open(path1, 'r').read()
    new_txt = old_txt.replace('hi','hello')
    open(path2, 'w').write(new_txt)


if __name__ == '__main__':
    count(r'R:\\cnt.txt')

    replace_hi(r'R:\\hi.txt', r'R:\\hello.txt')