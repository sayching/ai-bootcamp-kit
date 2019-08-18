class BasicTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_node(self):
        print(tree.left.data)
        print(tree.right.data)
        print(tree.left.left.data)

    def print_tree(self):
        i = 0
        if tree.data is not None:
            print("Level {} : {}".format(i, self.data))
            lelf_tree = self.left
            right_tree = self.right
            t = 1
            while t == 1:
                left_data = ""
                right_data = ""

                t = 0
                if (lelf_tree is not None):
                    left_data = lelf_tree.data
                    lelf_tree = lelf_tree.left
                    t = 1
                if (right_tree is not None):
                    right_data = right_tree.data
                    right_tree = right_tree.right
                    t = 1
                i += 1

                print("Level {} : [{}] [{}]".format(i, left_data, right_data))

tree = BasicTree()
tree.data = "ROOT"

tree.left = BasicTree()
tree.left.data = "L01"
tree.right = BasicTree()
tree.right.data = "R01"
tree.left.left = BasicTree()
tree.left.left.data = "L02"



tree.print_tree()
#tree.left.print_tree()
