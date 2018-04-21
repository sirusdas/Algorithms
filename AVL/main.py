from BalancedTree import BalancedTree

bst = BalancedTree()

bst.insert(4)
bst.insert(2)
bst.insert(3)

# bst.insert(25)
# bst.insert(15)
# bst.insert(90)

# bst.insert(5)
# bst.insert(20)
# bst.insert(30)
# bst.insert(50)

# bst.insert(3)
# bst.insert(7)
# bst.insert(18)
# bst.insert(21)
# bst.insert(26)
# bst.insert(33)
# bst.insert(120)
# bst.insert(45)
# bst.insert(55)

# bst.traverseInOrder()
bst.tree()

'''
                                    25

                        15                      90
                5               20          30

            3       7       18      21  26      50

                                            33
                                                45

rotateRight(self, node):
    n = 90
    nL = 30
    nP = 25
    b = 30(nL)
    bP = 25(nP)
    nL = 50(bR)
    nLP = 90(Node)
    bR = 90
    nP = 30(b)

    if bPR == node(n): True in this case
    bPR = b
return b
#Do check the result to see what b holds when u execute the program.
#After rotation Node becomes
                                    25
                               15         30
                                      26      90


rotateLeft(self, node):
    #using the above example
    n = 25
    nR = 30
    nP = None
    b = 30(nR)
    bP = None
    nR = 26(bL)
    nRP = 25(Node)
    bL = 25(n)
    nP = b(30)
return b

#Performing Rotate Left on Data
                                    25
                                15      30

#After Left Rotate Node Data
                                    30
                                25      90
                            15
'''
