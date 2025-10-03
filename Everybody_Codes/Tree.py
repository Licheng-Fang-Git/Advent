class TreeNode:
    def __init__(self, symbol, rank):
        self.symbol = symbol
        self.rank = rank
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def inorder_traversal(self, node, direction):
        if node:
            print(node.symbol, node.rank, direction)
            self.inorder_traversal(node.left, "left")
            self.inorder_traversal(node.right, "right")
