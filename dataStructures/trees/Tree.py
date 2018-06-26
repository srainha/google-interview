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

    # Insertion: upper=O(n), average=O(log(n))
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
        if (node.right is not None):
            if (node.right.data == data):
                return node
            elif (node.right.data < data):
                return self._findParent(data, node.right)
        if (node.left is not None):
            if (node.left.data == data):
                return node
            elif (data < node.left.data):
                return self._findParent(data, node.left)
        else:
            return None

    # Deletion: upper=O(n), average=O(log(n))
    def delete(self, data):
        parent = self.findParent(data)
        if (parent is not None):
            if (parent.data < data):
                node = parent.right
                if (node.right is None and node.left is None):
                    parent.right = None
                    return
                elif (node.right is None):
                    parent.right = node.left
                elif (node.left is None):
                    parent.right = node.right
                else:
                    # TODO
                    pass
            else: 
                node = parent.left
                if (node.left is None and node.right is None):
                    parent.left = None
                    return
                elif (node.right is None):
                    parent.left = node.left
                elif (node.left is None):
                    parent.left = node.right
                else:
                    # TODO
                    pass

    def deleteTree(self):
        self.root = None

    # Search: upper=O(n), average=O(log(n))
    def contains(self, data):
        return (self.find(data) is not None)

    # Index: upper=O(n), average=O(log(n))
    def index(self, data):
        pass
