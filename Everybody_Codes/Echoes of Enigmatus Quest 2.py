from Everybody_Codes.Tree import TreeNode

file = open("../input").read()
root_left_tree = TreeNode("",0)
root_right_tree = TreeNode("",0)

def dfs(node, rank, symbol):
    if node is None:
        return

    if node.right is None:
        if rank > node.rank:
            node.right = TreeNode(symbol, rank)
            return
    if node.left is None:
        if rank < node.rank:
            node.left = TreeNode(symbol, rank)
            return
    dfs(node.right, rank, symbol)
    dfs(node.left, rank, symbol)

for line in file.split('\n'):
    line = line.split(" ")
    print(line)
    id = line[1][3:]
    comma = line[2].find(",")
    left_rank = line[2][6:comma]
    left_symbol = line[2][comma+1: len(line[2])-1]
    comma = line[3].find(",")
    right_rank = line[3][7:comma]
    right_symbol = line[3][comma+1:len(line[3])-1]
    print(id, left_rank, left_symbol, right_rank, right_symbol)
    if not root_left_tree.symbol:
        root_left_tree = TreeNode(left_symbol, int(left_rank))
        root_right_tree = TreeNode(right_symbol, int(right_rank))
        continue
    dfs(root_left_tree, int(left_rank), left_symbol)
    dfs(root_right_tree, int(right_rank), right_symbol)

    print(root_left_tree.inorder_traversal(root_left_tree, "root"))
    print()
    print(root_right_tree.inorder_traversal(root_right_tree, "root"))
