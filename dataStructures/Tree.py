class TreeNode():
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


