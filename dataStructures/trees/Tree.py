class BinaryTreeNode():

    # A basic recursive binary tree structure

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insertion: upper=O(n), average=Θ(log(n))
    def add(self, data):
        if (data < self.data):
            if (self.left is None):
                self.left = BinaryTreeNode(data)
            else:
                self.left.add(data)
        else:
            if (self.right is None):
                self.right = BinaryTreeNode(data)
            else:
                self.right.add(data)

    # Deletion: upper=O(n), average=Θ(log(n))
    def delete(self, data):
        pass

    # Search: upper=O(n), average=Θ(log(n))
    def contains(self, data):
        pass

    # Index: upper=O(n), average=Θ(log(n))
    def index(self, data):
        pass