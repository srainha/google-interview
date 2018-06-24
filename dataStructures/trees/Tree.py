class BinaryTreeNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    # Insertion: upper=O(n), average=Θ(log(n))
    def add(self, data):
        if (self.root is None):
            self.root = BinaryTreeNode(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if (data < node.data):
            if (node.left is None):
                node.left = BinaryTreeNode(data)
            else:
                self._add(data, node.left)
        else:
            if (node.right is None):
                node.right = BinaryTreeNode(data)
            else:
                self._add(data, node.right)

    # Deletion: upper=O(n), average=Θ(log(n))
    def delete(self, data):
        pass

    def deleteTree(self):
        self.root = None

    # Search: upper=O(n), average=Θ(log(n))
    def contains(self, data):
        if (self.root.data == data):
            return True
        else:
            return self._contains(data, self.root)

    def _contains(self, data, node)
        if (node.data == data):
            return True
        if (self.root.data <= data): #check right
            pass
        if (val < self.data): # check left
            if (self.left is not None and )

    # Index: upper=O(n), average=Θ(log(n))
    def index(self, data):
        pass
