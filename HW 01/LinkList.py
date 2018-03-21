# LinkList


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next = node

    def getValue(self, index):
        index = index if index >= 0 else len(self) + index
        if len(self) < index or index < 0:
            return None
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        return pre.data

    def setValue(self, index, data):
        node = self.getValue(index)
        if node:
            node.data = data
        return node

    def insert(self, index, data):
        node = Node(data)
        if abs(index + 1) > len(self):
            return False
        index = index if index >= 0 else len(self) + index + 1
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pre = self.getValue(index - 1)
            if pre:
                next = pre.next
                pre.next = node
                node.next = next
            else:
                return False
        return node

    def delete(self, index):
        f = index if index > 0 else abs(index + 1)
        if len(self) <= f:
            return False
        pre = self.head
        index = index if index >= 0 else len(self) + index
        prep = None
        while index:
            prep = pre
            pre = pre.next
            index -= 1
        if not prep:
            self.head = pre.next
        else:
            prep.next = pre.next
        return pre.data

    def show(self):
        for n in range(self.__len__()):
            print(self.getValue(n), end=' ')


if __name__ == '__main__':
    link = LinkList()
    link.append(1)
    link.append(4)
    link.append(5)
    link.append(7)
    print('原链表: ', end='')
    link.show()
    print()
    link.append(10)
    print('使用append追加元素10后: ', end='')
    link.show()
    print()
    link.delete(0)
    print('删除第一个元素后: ', end='')
    link.show()
    print()
    link.insert(0, 11)
    print('在首部插入元素11后: ', end='')
    link.show()
