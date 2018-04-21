from Node import Node
from pprint import pprint

class BalancedTree(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        print("Inserting: ",data)
        parentNode = self.rootNode

        if self.rootNode == None:
            parentNode = Node(data, None)
        else:
            parentNode = self.rootNode.insert(data, self.rootNode)

        self.rebalanceTree(parentNode)

    def tree(self):
        if self.rootNode is None:
            print("Tree is empty")
        else:
            print("...Tree Structure...")
            self.rootNode.tree()

    def traverseInOrder(self):
        if self.rootNode is None:
            print("Tree is empty")
        else:
            print("...Traversing...")
            self.rootNode.traverseInOrder()

    def rebalanceTree(self, parentNode):
        self.setBalance(parentNode)
        print("Height of Tree from {} is {}"
              .format(parentNode.data, parentNode.balance))


        if parentNode.balance < -1:
            print("Current Tree details")
            self.rootNode.tree()
            print("\n.... Balancing the Tree ... \n")
            if self.height(parentNode.leftChild.leftChild) >= self.height(parentNode.leftChild.rightChild):
                parentNode = self.rotateRight(parentNode)
            else:
                parentNode = self.rotateLeftRight(parentNode)
        elif parentNode.balance > 1:
            print("Current Tree details")
            self.rootNode.tree()
            print("\n.... Balancing the Tree ... \n")
            if self.height(parentNode.rightChild.rightChild) >= self.height(parentNode.rightChild.leftChild):
                parentNode = self.rotateLeft(parentNode)
            else:
                parentNode = self.rotateRightLeft(parentNode)

        if parentNode.parentNode is not None:
            self.rebalanceTree(parentNode.parentNode)
        else:
            print("Current RootNode",parentNode.data,"\n----------------------------")
            self.rootNode = parentNode

    def rotateLeftRight(self, node):

        # print("BeforeRotation Node- Node:{}, NodeL:{}, NodeR:{}"
        #       .format(node.data, node.leftChild.data, node.rightChild.data))
        print("Before Rotation Node data:")
        self.print_data(node)
        print("...Performing Rotation Left followed by Right...")
        node.leftChild = self.rotateLeft(node.leftChild)
        # print("Node.leftChild = RL")
        return self.rotateRight(node)

    def rotateRightLeft(self, node):

        # print("BeforeRotation Node- Node:{}, NodeL:{}, NodeR:{}"
        #       .format(node.data, node.leftChild.data, node.rightChild.data))
        print("Before Rotation Node data:")
        self.print_data(node)
        print("...Performing Rotation Right followed by Left...")
        node.rightChild = self.rotateRight(node.rightChild)
        # print("Node.rightChild = RR")
        return self.rotateLeft(node)

    def rotateLeft(self, node):
        print("...Performing Rotate Left...")

        print("Before Left Rotate Node Data:")
        self.print_data(node)
        # print("LR Node- Node:{}, NodeL:{}, NodeR:{}"
        #       .format(node.data, node.leftChild.data, node.rightChild.data))

        b = node.rightChild
        b.parentNode = node.parentNode

        node.rightChild = b.leftChild

        if node.rightChild is not None:
            node.rightChild.parentNode = node

        b.leftChild = node
        node.parentNode = b

        # if b.parentNode is not None:
        #     if b.parentNode.rightChild == node:
        #         b.parentNode.rightChild = b
        #     else:
        #         b.parentNode.leftChild = b

        self.setBalance(node)
        self.setBalance(b)

        print("After Left Rotate Node Data:")
        self.print_data(b)
        # print("LR- b:{}, bL:{}, bR:{}"
        #       .format(b.data, b.leftChild.data, b.rightChild.data))
        return b

    def rotateRight(self, node):

        print("...Performing Rotate Right...")

        print("Before Right Rotation Node data:")
        self.print_data(node)
        # print("RR Node- Node:{}, NodeL:{}, NodeR:{}"
        #       .format(node.data, node.leftChild.data, node.rightChild.data))

        b = node.leftChild
        b.parentNode = node.parentNode

        node.leftChild = b.rightChild

        if node.leftChild is not None:
            node.leftChild.parentNode = node


        b.rightChild = node
        node.parentNode = b

        # if b.parentNode is not None:
        #     if b.parentNode.rightChild == node:
        #         b.parentNode.rightChild = b
        #     else:
        #         b.parentNode.leftChild = b
        self.setBalance(node)
        self.setBalance(b)

        print("After Right Rotate Node Data:")
        self.print_data(b)
        # print("RR- b:{}, bP:{}, bL:{}, bR:{}"
        #       .format(b.data, b.parentNode.data, b.leftChild.data, b.rightChild.data))
        return b

    def print_data(self,node):

        if node.data:
            print("Node:",node.data)
        if node.leftChild:
            print("NodeL:",node.leftChild.data)
        if node.rightChild:
            print("NodeR:",node.rightChild.data)
        if node.parentNode:
            print("NodeP:",node.parentNode.data)


    def setBalance(self, node):
        node.balance = (self.height(node.rightChild) - self.height(node.leftChild))
        node.name = "sirus"

    def height(self, node):

        if node == None:
            return -1
        else:
            return 1 + max(self.height(node.leftChild), self.height(node.rightChild))
