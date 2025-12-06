file = open("../input").read().split("\n")
def part_one():
    equations = []
    for line in file:
        line = [s for s in line.split(" ") if s != "" ]
        for i in range(len(line)):
            try:
                equations[i].append((line[i]))
            except IndexError:
                equations.append([line[i]])

    total = 0
    for problem in equations:
        symbol = problem[-1]
        one_problem = problem[0]
        for num in problem[1:len(problem)-1]:
            expression = str(num) + symbol + str(one_problem)
            one_problem = eval(expression)
        total += one_problem
    return total

# Requires me to move the arithmetic operation to the top
def part_two():
    equations = {}
    symbol_line = file[0]
    space_count = 0
    total = 0
    # getting the number of spaces for format
    for i in range(len(symbol_line)):
        if symbol_line[i] == "+" or symbol_line[i] == "*" or symbol_line[i] == ";":
            if equations:
                equations[list(equations.keys())[-1]][0] = space_count
            equations[i] = [0, symbol_line[i]]
            space_count = 0
        else:
            space_count += 1
    # equations = 0 : [3, "+"]

    for line in file[1:]:
        for i in range(len(line)):
            if i in equations and equations[i] != []:
                num = line[i: i + equations[i][0]]
                equations[i].append(num)

    # equations = 0 : [3, "+", "123", "45", "6"]

    for key in equations:
        if not equations[key]: continue
        if equations[key][1] == "*": one_prob_total = 1
        else: one_prob_total = 0
        for place_val in range(equations[key][0]):
            num = ""
            for nums in equations[key][2:]:
                num += nums[place_val]
            expression = str(num) + equations[key][1] + str(one_prob_total)
            one_prob_total = eval(expression)
        total += one_prob_total

    print(total)

part_one()
part_two()

