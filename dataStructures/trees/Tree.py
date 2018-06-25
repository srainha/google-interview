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

    def find(self, data):
        if (self.root.data == data):
            return self.root
        else:
            return self._find(data, this.root)

    def _find(self, data, node):
        if (node.data == data):
            return node
        elif (node.left is not None and data <= node.left.data):
            return self._find(data, node.left)
        elif (node.right is not None and node.right.data <= data):
            return self._contains(data, node.right)
        else:
            return None

    def findParent(self, data):
        if (self.root.data == data):
            return None
        else:
            return self._findParent(data, self.root)

    def _findParent(self, data, node):
        if (node.right is not None)
        if (node.left is not None)


    # Deletion: upper=O(n), average=Θ(log(n))
    def delete(self, data):
        node = self.find(data)
        if (node is not None):
            if (node.left is None and node.right is None):

        

    def deleteTree(self):
        self.root = None

    # Search: upper=O(n), average=Θ(log(n))
    def contains(self, data):
        return (self.find(data) is not None)

    # Index: upper=O(n), average=Θ(log(n))
    def index(self, data):
        pass
