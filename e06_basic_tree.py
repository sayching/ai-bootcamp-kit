class BasicTree:
    def __init__(self, value='basicTree data', left=None, right=None):
        self.data = value
        self.left = left
        self.right = right


root = BasicTree()
root.data = "ROOT LVL 0"
root.left = BasicTree()
root.left.data = "LEFT LVL 1"
root.right = BasicTree()
root.right.data = "RIGHT LVL 1"
root.left.left = BasicTree()
root.left.left.data = "LEFT LVL 2"

print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
