import heapq
file = open("../input").read().split("\n")

def bfs(node, cur_light):
    hq = [(1, node, cur_light, set())]
    count = 0
    while hq:
        press, button_info, cur_light, visited = heapq.heappop(hq)
        new_cur_light = list(cur_light)
        visited.add(node)
        for one_press in button_info:
            if new_cur_light[one_press] == "#":
                new_cur_light[one_press] = "."
            else:
                new_cur_light[one_press] = "#"
        if new_cur_light == indicator_lights:
            return press
        for one_b in buttons:
            if one_b in visited:
                continue
            visited.add(one_b)
            heapq.heappush(hq, (press + 1, one_b, new_cur_light, visited.copy()))
        count += 1

total = 0
for machine in file:
    print(machine)
    curly_braces, end_bracket, opening_paren = machine.find("{"), machine.find("]"), machine.find("(")
    indicator_lights = list(machine[1:opening_paren - 2])
    buttons = []
    one_button = []
    for b in machine[opening_paren:curly_braces - 1]:
        if b == "(" and one_button != []:
            buttons.append(one_button)
            one_button = []
        if b.isdigit():
            one_button.append(int(b))
    buttons.append(one_button)
    buttons = {tuple(b) for b in buttons}
    minimum_buttons = float("inf")
    for b in buttons:
        # test_press = dfs(b, "." * len(indicator_lights), 0)
        test_press = bfs(b, "." * len(indicator_lights))
        if test_press is not None:
            minimum_buttons = min(minimum_buttons, test_press)
    total += minimum_buttons
    print(minimum_buttons)
    joltages = machine[curly_braces:]

print(total)



#51


