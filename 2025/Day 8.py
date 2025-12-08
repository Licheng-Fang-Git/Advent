import math

file = open("../input").read().split("\n")
box_distances = {}
for i in range(len(file)):
    x1, y1, z1 = map(int, file[i].split(","))
    for j in range(i + 1, len(file)):
        x2, y2, z2 = map(int, file[j].split(","))
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        box_distances[(x1, y1, z1), (x2, y2, z2)] = distance


sorted_box_distances = sorted(box_distances.items(), key=lambda item: item[1])

visited = set()
def dfs(node, all_connections, total_circuits):
    count = 0
    for connect in total_circuits[node]:
        if connect in visited: continue
        count += 1
        visited.add(connect)
        count += dfs(connect, all_connections, total_circuits)
    return count

def dfs_get_length(node, total_circuits, seen):
    count = 0
    for connect in total_circuits[node]:
        if connect in seen: continue
        count += 1
        seen.add(connect)
        count += dfs_get_length(connect,total_circuits, seen)
    return count
# My plan for part 1 is to make my boxes connected and dfs each circuit to get the length
def solve_one():
    total_circuits = {}
    for i in range(1000):
        junction_box1 = sorted_box_distances[i][0][0]
        junction_box2 = sorted_box_distances[i][0][1]
        if junction_box1 in total_circuits:
            total_circuits[junction_box1].add(junction_box2)
        else:
            total_circuits[junction_box1] = {junction_box1, junction_box2}

        if junction_box2 in total_circuits:
            total_circuits[junction_box2].add(junction_box1)
        else:
            total_circuits[junction_box2] = {junction_box2, junction_box1}

    max_circuits = []
    for circuit in total_circuits:
        if circuit in visited:
            continue
        visited.add(circuit)
        max_circuits.append(dfs(circuit, total_circuits[circuit], total_circuits)+1)

    circuit_lengths = sorted(max_circuits)
    total = 1
    for i in range(len(circuit_lengths) - 1, len(circuit_lengths) - 4, -1):
        print(circuit_lengths[i])
        total *= circuit_lengths[i]
    print(total)

# My plan for part two is to get the lengths of all the circuits, and it should have all have 1000.
def solve_two():
    total_circuits = {}
    print(len(sorted_box_distances))
    circuit_lens = []
    not_full_circuit = True
    i = 0
    while not_full_circuit:
        not_full_circuit = False
        circuit_lens = []
        junction_box1 = sorted_box_distances[i][0][0]
        junction_box2 = sorted_box_distances[i][0][1]

        if junction_box1 in total_circuits:
            total_circuits[junction_box1].add(junction_box2)
        else:
            total_circuits[junction_box1] = {junction_box1, junction_box2}

        if junction_box2 in total_circuits:
            total_circuits[junction_box2].add(junction_box1)
        else:
            total_circuits[junction_box2] = {junction_box2, junction_box1}

        for circuit in total_circuits:
            c_len = dfs_get_length(circuit, total_circuits, set(circuit))
            if c_len < 1000:
                not_full_circuit = True
                break
            else:
                circuit_lens.append(c_len)

        for num in circuit_lens:
            if num != 1000:
                not_full_circuit = True
                break
        i += 1
        print(circuit_lens)
#6588 (27558, 61383, 12726) (42727, 57753, 11997)
#6587 (37565, 7239, 99565) (39240, 1604, 85100)

solve_two()
