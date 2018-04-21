
class Node(object):

    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rightChild = None
        self.leftChild = None
        self.balance = 0

    def insert(self, data, parentNode):

        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data, parentNode)
            else:
                self.leftChild.insert(data, parentNode)
        else:
            if not self.rightChild:
                self.rightChild = Node(data, parentNode)
            else:
                self.rightChild.insert(data, parentNode)

        return parentNode

    def traverseInOrder(self):
        if self.leftChild:
            print("L - ",self.leftChild.data)
            self.leftChild.traverseInOrder()

        #print(self.data)

        if self.rightChild:
            print("R - ",self.rightChild.data)
            self.rightChild.traverseInOrder()

    def tree(self):
        if self.data and (self.leftChild or self.rightChild):
            print("...P - ",self.data)
        if self.leftChild:
            print("L - ",self.leftChild.data)

        if self.rightChild:
            print("R - ",self.rightChild.data)

        if self.leftChild:
            self.leftChild.tree()
        if self.rightChild:
            self.rightChild.tree()

    def getMax(self):
        if not self.rightChild:
            return self.data
        else:
            return self.rightChild.getMax()

    def getMin(self):
        if not self.leftChild:
            return self.data
        else:
            return self.leftChild.getMin()
