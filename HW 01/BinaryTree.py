# BinaryTree


class BinaryTree(object):
    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__data = value

    def insertLeftChild(self, value):
        if self.__left:
            print('Left Child Tree Already Exists!')
        else:
            self.__left = BinaryTree(value)
            return self.__left

    def insertRightChild(self, value):
        if self.__right:
            print('Right Child Tree Already Exists!')
        else:
            self.__right = BinaryTree(value)
            return self.__right

    def show(self):
        print(self.__data)

    def preOrder(self):
        print(self.__data)
        if self.__left:
            self.__left.preOrder()
        if self.__right:
            self.__right.preOrder()

    def inOrder(self):
        if self.__left:
            self.__left.inOrder()
        print(self.__data)
        if self.__right:
            self.__right.inOrder()

    def postOrder(self):
        if self.__left:
            self.__left.inOrder()
        if self.__right:
            self.__right.inOrder()
        print(self.__data)


if __name__ == '__main__':
    TreeRoot = BinaryTree(1)
    TreeRoot.insertLeftChild(2)
    TreeRoot.insertRightChild(3)
    print('中序遍历:')
    TreeRoot.inOrder()
    print('先序遍历:')
    TreeRoot.preOrder()
    print('后序遍历:')
    TreeRoot.postOrder()
