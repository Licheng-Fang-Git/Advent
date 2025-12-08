import time

file = open("../input").read().split("\n")
H,W = 103, 101
class Robot:
    def __init__(self, p_x, p_y, v_x, v_y):
        self.p_x = p_x
        self.p_y = p_y
        self.v_x = v_x
        self.v_y = v_y

    def move(self, h, w):
        self.p_x = (self.p_x + self.v_x) % w
        self.p_y = (self.p_y + self.v_y) % h

    def display_position(self):
        #row, column
        return self.p_y, self.p_x

grid = [["." for j in range(W)]for i in range(H)]
robots = []
for i, line in enumerate(file):
    position, velocity = line.split(" ")
    pos_x, pos_y = int(position.split(",")[0][2:]), int(position.split(",")[1])
    velocity_x, velocity_y = int(velocity.split(",")[0][2:]), int(velocity.split(",")[1])
    robots.append(Robot(pos_x, pos_y, velocity_x, velocity_y))
def solve_one():
    horizontal_split = H // 2
    vertical_split = W // 2
    print(horizontal_split, vertical_split)
    for i in range(100):
        for r in robots:
            r.move(H,W)
    quad_1, quad_2, quad_3, quad_4 = 0, 0, 0, 0
    for robot in robots:
        r,c = robot.display_position()
        if 0 <= r < horizontal_split and 0 <= c < vertical_split:
            quad_1 += 1
        elif 0 <= r < horizontal_split and vertical_split < c < W:
            quad_2 += 1
        elif horizontal_split < r < H and 0 <= c < vertical_split:
            quad_3 += 1
        elif horizontal_split < r < H and vertical_split < c < W:
            quad_4 += 1

    return quad_1 * quad_2 * quad_3 * quad_4

def solve_two():
    for i in range(100):
        print("Seconds:", i)
        for r in robots:
            r.move(H,W)
            r,c = r.display_position()
            grid[r][c] = "*"

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j + 1 == len(grid[i]):
                    print(grid[i][j], end="\n")
                else:
                    print(grid[i][j], end="")
        print()
        for r in robots:
            r,c = r.display_position()
            grid[r][c] = "."

        time.sleep(0.5)

# solve_one()
solve_two()

