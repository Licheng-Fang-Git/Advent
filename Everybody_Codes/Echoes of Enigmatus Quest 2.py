from collections import deque
from Everybody_Codes.Tree import TreeNode
import copy

file = open("../input").read()
root_left_tree = TreeNode("","",0)
root_right_tree = TreeNode("","",0)
tree_dictionary = {}

def get_same_branch(node, swap_id, rank):
    if node is None:
        return

    if node.left and node.left.id == swap_id and node.left.rank == rank:
        return tuple((node, node.left))
    if node.right and node.right.id == swap_id and node.right.rank == rank:
        return tuple((node, node.right))

    return get_same_branch(node.left, swap_id, rank, ) or get_same_branch(node.right, swap_id, rank)

#swap id nodes of the same tree
def same_tree_swap(node, swap_id, parent, branch):
    if node is None:
        return
    if node.id == parent.id and node.rank == parent.rank:
        if node.left and node.left.id == branch.id and branch.rank != node.left.rank:
            node.left = None
            node.left = branch
            return

    if node.id == parent.id and node.rank == parent.rank:
        if node.right and node.right.id == branch.id and branch.rank != node.right.rank:
            node.right = None
            node.right = branch
            return

    same_tree_swap(node.left, swap_id, parent, branch)
    same_tree_swap(node.right, swap_id, parent, branch)

# every line set up for a binary tree
def dfs_binary(node, id, rank, symbol):
    if node is None:
        return
    if rank > node.rank:
        if node.right is None:
            node.right = TreeNode(id, symbol, rank)
        else:
            dfs_binary(node.right, id, rank, symbol)

    elif rank < node.rank:
        if node.left is None:
            node.left = TreeNode(id, symbol, rank)
        else:
            dfs_binary(node.left, id, rank, symbol)

# delete the branch and get the children nodes
def delete_branch(node, swap_node_id, tree_place, found):
    global swap_branch_left, swap_branch_right, left_tree_children, right_tree_children
    if node is None:
        if found is True:
            if tree_place == 'left':
                left_tree_children.append(None)
            elif tree_place == 'right':
                right_tree_children.append(None)
        return

    if node.id == swap_node_id:
        if tree_place == 'left':
            swap_branch_left = node
        if tree_place == 'right':
            swap_branch_right = node
        found = True

    elif found is True:
        if tree_place == 'left':
            left_tree_children.append((node.id, node.symbol, node.rank))
        elif tree_place == 'right':
            right_tree_children.append((node.id, node.symbol, node.rank))

    delete_branch(node.left, swap_node_id, tree_place, found)
    delete_branch(node.right, swap_node_id, tree_place, found)

def get_branch(node, swap_id):
    if node is None:
        return
    if node.id == swap_id:
        return tuple((node, node))
    if node.left and node.left.id == swap_id:
        return tuple((node, node.left))
    if node.right and node.right.id == swap_id:
        return tuple((node, node.right))

    return get_branch(node.left, swap_id) or get_branch(node.right, swap_id)

def dfs_swap_branch(node, swap_id, parent, branch):
    if node is None:
        return

    if node.id == parent.id and node.rank == parent.rank:
        if node.left and node.left.id == branch.id:
            node.left = None
            node.left = copy.deepcopy(branch)
            return

    if node.id == parent.id and node.rank == parent.rank:
        if node.right and node.right.id == branch.id:
            node.right = None
            node.right = copy.deepcopy(branch)
            print("Here", node.right.rank)
            return

    dfs_swap_branch(node.left, swap_id, parent, branch)
    dfs_swap_branch(node.right, swap_id, parent, branch)


# swap different tree nodes and sets the swap_node as the root
# therefore, when doing dfs binary it starts at the root of the swap
def dfs_swap(node, swap_node_id, tree_place):
    global root_left_swap_node, root_right_swap_node
    if node is None:
        return
    if node.id == swap_node_id:
        left_val = tree_dictionary[swap_node_id][0]
        right_val = tree_dictionary[swap_node_id][1]
        if node.rank == left_val[0]:
            setattr(node, 'rank', right_val[0])
            setattr(node, 'symbol', right_val[1])
        else:
            setattr(node, 'rank', left_val[0])
            setattr(node, 'symbol', left_val[1])

        if tree_place == 'left':
            root_left_swap_node = node
        elif tree_place == 'right':
            root_right_swap_node = node
        return

    dfs_swap(node.left, swap_node_id, tree_place)
    dfs_swap(node.right, swap_node_id, tree_place)

def remake_branch(node, children):
    child_dir = False
    curr_node = node
    prev = ""
    while children:
        curr_val = children.pop(0)
        if curr_val is None:
            if prev is None:
                curr_node = node
                child_dir = True
                continue
            child_dir = not child_dir
            prev = None
            continue

        if child_dir is False:
            curr_node.left = TreeNode(curr_val[0], curr_val[1], curr_val[2])
            curr_node = curr_node.left
            child_dir=False

        elif child_dir is True:
            curr_node.right = TreeNode(curr_val[0], curr_val[1], curr_val[2])
            curr_node = curr_node.right
            child_dir =False
        prev = 1

for line in file.split('\n'):
    line = line.split(" ")
    if "SWAP" in line[0]:
        swap_id = line[1]
        print(swap_id)
        left_tree_children = []
        right_tree_children = []
        if get_branch(root_left_tree, swap_id) is None:
            swap_one_parent, swap_one_branch = get_same_branch(root_right_tree, swap_id, tree_dictionary[swap_id][0][0])
            swap_one_branch = copy.deepcopy(swap_one_branch)
            swap_two_parent, swap_two_branch = copy.deepcopy(get_same_branch(root_right_tree, swap_id, tree_dictionary[swap_id][1][0]))
            swap_two_branch = copy.deepcopy(swap_two_branch)
            same_tree_swap(root_right_tree, swap_id, swap_one_parent, swap_two_branch)
            same_tree_swap(root_right_tree, swap_id, swap_two_parent, swap_one_branch)
            continue

        elif  get_branch(root_right_tree, swap_id) is None:
            swap_one_parent, swap_one_branch = get_same_branch(root_left_tree, swap_id, tree_dictionary[swap_id][0][0])
            swap_one_branch = copy.deepcopy(swap_one_branch)
            swap_two_parent, swap_two_branch = copy.deepcopy(get_same_branch(root_left_tree, swap_id, tree_dictionary[swap_id][1][0]))
            swap_two_branch = copy.deepcopy(swap_two_branch)
            same_tree_swap(root_left_tree, swap_id, swap_one_parent, swap_two_branch)
            same_tree_swap(root_left_tree, swap_id, swap_two_parent, swap_one_branch)
            continue


        swap_branch_left_parent, swap_branch_left = get_branch(root_left_tree, swap_id)
        swap_branch_right_parent, swap_branch_right = get_branch(root_right_tree, swap_id)

        print("right", swap_branch_right.rank)

        if swap_branch_left_parent.rank == tree_dictionary[swap_id][0][0] or swap_branch_left_parent.rank == tree_dictionary[swap_id][1][0]:
            root_left_tree = None
            root_left_tree = copy.deepcopy(swap_branch_right)
            root_right_tree = None
            root_right_tree = copy.deepcopy(swap_branch_left)
            continue
        else:
            print('left tree:', swap_branch_left_parent.rank)
            print('right tree:', swap_branch_right_parent.rank)
            print('left tree:', swap_branch_left.rank)
            print('right tree:', swap_branch_right.rank)
            dfs_swap_branch(root_left_tree, swap_id, swap_branch_left_parent, copy.deepcopy(swap_branch_right))
            dfs_swap_branch(root_right_tree, swap_id, swap_branch_right_parent, copy.deepcopy(swap_branch_left))


        # if swap_branch_left is None:
        #     swap_one_parent, swap_one_branch = get_same_branch(root_right_tree, swap_id, tree_dictionary[swap_id][0][0])
        #     swap_one_branch = copy.deepcopy(swap_one_branch)
        #     swap_two_parent, swap_two_branch = copy.deepcopy(get_same_branch(root_right_tree, swap_id, tree_dictionary[swap_id][1][0]))
        #     swap_two_branch = copy.deepcopy(swap_two_branch)
        #     same_tree_swap(root_right_tree, swap_id, swap_one_parent, swap_two_branch)
        #     same_tree_swap(root_right_tree, swap_id, swap_two_parent, swap_one_branch)
        #     continue

        # elif swap_branch_right == "":
        #     swap_one_parent, swap_one_branch = get_same_branch(root_left_tree, swap_id, tree_dictionary[swap_id][0][0])
        #     swap_one_branch = copy.deepcopy(swap_one_branch)
        #     swap_two_parent, swap_two_branch = copy.deepcopy(get_same_branch(root_left_tree, swap_id, tree_dictionary[swap_id][1][0]))
        #     swap_two_branch = copy.deepcopy(swap_two_branch)
        #     same_tree_swap(root_left_tree, swap_id, swap_one_parent, swap_two_branch)
        #     same_tree_swap(root_left_tree, swap_id, swap_two_parent, swap_one_branch)
        #     continue

        # root_left_swap_node = ""
        # root_right_swap_node = ""
        # dfs_swap(root_left_tree, swap_id, "left")
        # dfs_swap(root_right_tree, swap_id, "right")

        # swap_branch_left.left = None
        # swap_branch_left.right = None
        # remake_branch(root_left_swap_node, right_tree_children)
        #
        # swap_branch_right.left = None
        # swap_branch_right.right = None
        # remake_branch(root_right_swap_node, left_tree_children)

        print(root_left_tree.inorder_traversal(root_left_tree, "root"))
        print()
        print(root_right_tree.inorder_traversal(root_right_tree, "root"))

        continue

    id = line[1][3:]
    comma = line[2].find(",")
    left_rank = int(line[2][6:comma])
    left_symbol = line[2][comma+1: len(line[2])-1]
    comma = line[3].find(",")
    right_rank = int(line[3][7:comma])
    right_symbol = line[3][comma+1:len(line[3])-1]
    # Every Node ID information
    tree_dictionary[id] = [[left_rank, left_symbol], [right_rank, right_symbol]]

    if not root_left_tree.symbol:
        root_left_tree = TreeNode(id, left_symbol, int(left_rank))
        root_right_tree = TreeNode(id, right_symbol, int(right_rank))
        continue
    dfs_binary(root_left_tree, id, int(left_rank), left_symbol)
    dfs_binary(root_right_tree, id, int(right_rank), right_symbol)


def bfs(root):
    dq = deque([root])
    max_length = 0
    max_string = ""
    n = 0
    add_string = False
    while dq:
        one_level_length = len(dq)
        if one_level_length > max_length:
            max_length = one_level_length
            max_string = ""
            add_string = True
        for _ in range(one_level_length):
            node = dq.popleft()
            if add_string:
                max_string += node.symbol
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        add_string = False

    return max_string

#
print(root_left_tree.inorder_traversal(root_left_tree, "root"))
print()
print(root_right_tree.inorder_traversal(root_right_tree, "root"))

print(bfs(root_left_tree) + bfs(root_right_tree))
