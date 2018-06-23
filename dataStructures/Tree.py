class TreeNode():

    # A basic recursive binary tree structure

    # Time Complexities 
    # Insertion: upper=O(n), average=Θ(log(n))
    # Deletion: upper=O(n), average=Θ(log(n))
    # Search: upper=O(n), average=Θ(log(n))
    # Index: upper=O(n), average=Θ(log(n))

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if (data < self.data):
            if (self.left is None):
                self.left = TreeNode(data)
            else:
                self.left.add(data)
        else:
            if (self.right is None):
                self.right = TreeNode(data)
            else:
                self.right.add(data)

    def delete(self, data):
        pass

    def contains(self, data):
        pass