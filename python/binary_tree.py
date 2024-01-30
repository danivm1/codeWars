from queue import Queue

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

    def inOrderTraversal(self):
            res = []
            if self:
                res = self.inOrderTraversal(self.left)
                res.append(self.value)
                res = res + self.inOrderTraversal(self.right)
            return res
    
    def preOrderTraversal(self):
        res = []
        if self:
            res.append(self.value)
            res = res + self.preOrderTraversal(self.left)
            res = res + self.preOrderTraversal(self.right)
        return res
    
    def postOrderTraversal(self):
        res = []
        if self:
            res = self.postOrderTraversal(self.left)
            res = res + self.postOrderTraversal(self.right)
            res.append(self.value)
        return res
    
    def levelOrder(self):
        if self==None:
            return
        q=Queue()
        q.put(self)
        while(not q.empty()):
            self=q.get()
            if self==None:
                continue
            yield self.value
            q.put(self.left)
            q.put(self.right)



binaryTree = Node(              # root  0
                Node(           # left  l1
                    None,       # left  l1-l2
                    Node(       # right l1-r2
                        None,   # left  l1-r2-l3
                        None,   # right l1-r2-r3
                        4),     # value l1-r2-v3
                    2),         # value l1-v2
                Node(           # right r1
                    Node(       # left  r1-l2
                        None,   # left  r1-l2-l3
                        None,   # right r1-l2-r3
                        5),     # value r1-l2-v3
                    Node(       # right r1-r2
                        None,   # left  r1-r2-l3
                        None,   # right r1-r2-r3
                        6),     # value r1-r2-v3
                    3),         # value r1-v2
                1)              # value v1

                                #     1
                                #  2     3
                                #   4   5 6



result = [i for i in binaryTree.levelOrder()]
print(result)