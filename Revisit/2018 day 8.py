file = open("aoc_input").read()

data = iter(list(map(int,file.split(" "))))

total_meta_num = 0
root_child = {}
next_child_node = 0
def traverse():
    global total_meta_num, next_child_node
    curr_child_node = next_child_node
    next_child_node += 1
    child_num = next(data)
    meta_num = next(data)
    children_ids = []
    for _ in range(child_num):
        children_ids.append(traverse())
    meta_ids = []
    for _ in range(meta_num):
        meta_ids.append(next(data))

    root_child[curr_child_node] = {
        "children_id" : children_ids,
        "meta_id" : meta_ids
    }

    return curr_child_node



traverse()

def solve_two(node):
    total = 0
    node_data = root_child[node]
    print(node, node_data)
    if not node_data["children_id"]:
       total += sum(node_data["meta_id"])
    else:
        for meta_data in node_data["meta_id"]:
            if meta_data > len(node_data["children_id"]):
                print(True)
                continue
            else:
                total += solve_two(node_data["children_id"][meta_data-1])

    return total


print(root_child)
print(solve_two(0))
