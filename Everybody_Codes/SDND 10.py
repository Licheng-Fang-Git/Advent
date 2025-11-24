import functools

file = open("../input").read().split("\n")
chess_board = []
moves = set()
sheep_loc = tuple((i,j) for i in range(len(file)) for j in range(len(file[i])) if file[i][j] == "S")
protect_pos = set()
start = tuple()
for i in range(len(file)):
    one_row = []
    for j in range(len(file[i])):
        one_row.append(file[i][j])
        if file[i][j] == "D":
            moves.add((i,j))
            start = (i,j)
        # elif file[i][j] == "S":
        #     sheep_loc.append((i,j))
        elif file[i][j] == "#":
            protect_pos.add((i,j))
    chess_board.append(one_row)
ROW = len(chess_board)

def get_dragon_locations(x,y):
    locations = []
    for nm in ["U", "D", "L", "R"]:
        if nm == "U":
            nx, ny = x, y-2
            if ny < 0 or ny >= len(chess_board[0]): continue
            if 0 <= nx - 1 < len(chess_board):
                locations.append((nx - 1, ny))
            if nx + 1 < 0 or nx + 1 >= len(chess_board): continue
            locations.append((nx+1, ny))
            moves.add((nx-1, ny))
            moves.add((nx+1, ny))
        elif nm == "D":
            nx,ny = x,y+2
            if ny < 0 or ny >= len(chess_board[0]): continue
            if 0 <= nx-1 < len(chess_board):
                locations.append((nx - 1, ny))
            if nx + 1 < 0 or nx + 1 >= len(chess_board): continue
            locations.append((nx+1, ny))
            moves.add((nx-1, ny))
            moves.add((nx+1, ny))
        elif nm == "L":
            nx,ny = x-2,y
            if nx < 0  or nx >= len(chess_board): continue
            if 0 <= ny+1 < len(chess_board[0]):
                locations.append((nx, ny + 1))
            if ny - 1 < 0 or ny - 1 >= len(chess_board[0]): continue
            locations.append((nx, ny-1))
            moves.add((nx, ny+1))
            moves.add((nx, ny-1))
        elif nm == "R":
            nx,ny = x+2, y
            if nx < 0 or nx >= len(chess_board): continue
            if 0 <= ny+1 < len(chess_board[0]):
                locations.append((nx, ny + 1))
            if ny - 1 < 0 or ny - 1 >= len(chess_board[0]): continue
            locations.append((nx, ny-1))
            moves.add((nx, ny+1))
            moves.add((nx, ny-1))
    print(locations)
    return locations

def part_one(sheep_pos):
    curr_pos = moves.copy()
    moves.remove(start)
    ans = 0
    for i in range(20):
        one_place_new = set()
        for r,c in curr_pos:
            for si,sj in get_dragon_locations(r,c):
                one_place_new.add((si,sj))
        curr_pos = one_place_new

        turn = 0
        new_sheep_pos = set()
        for r, c in sheep_pos:
            if (r,c) in protect_pos:
                new_sheep_pos.add((r, c))
                continue
            if (r,c) in curr_pos:
                turn += 1
                continue
            new_sheep_pos.add((r, c))

        sheep_pos = new_sheep_pos.copy()
        new_sheep_pos = set()
        for r,c in sheep_pos:
            if r + 1 >= len(chess_board):
                continue
            if (r+1,c) in protect_pos:
                new_sheep_pos.add((r+1, c))
                continue
            if (r+1,c) in curr_pos:
                turn += 1
                continue
            new_sheep_pos.add((r+1,c))
        sheep_pos = new_sheep_pos.copy()
        ans += turn

    # part_one
    # ans = 0
    # for i,j in sheep_pos:
    #     if (i,j) in moves:
    #             ans += 1
    print(ans)
    return ans

# part_one(sheep_loc.copy())

@functools.cache
def count(sheep, dragon, turn="sheep"):
    if turn == "sheep":
        if len(sheep) == 0: return 1
        total = 0
        move = 0
        for i, (r,c) in enumerate(sheep):
            if r + 1 >= ROW:
                move += 1
            elif chess_board[r+1][c] == "#" or (r+1,c) != dragon:
                move += 1
                total += count((*sheep[:i], (r+1,c), *sheep[i+1:]),dragon, turn="dragon")
        if move == 0:
            return count(sheep, dragon, turn = "dragon")
        return total

    if turn == "dragon":
        total = 0
        for r,c in get_dragon_locations(dragon[0], dragon[1]):
            total += count(tuple((sr,sc) for sr, sc in sheep if (sr,sc) in protect_pos or (sr,sc) != (r,c))  , (r,c), turn="sheep" )
        return total


print(count(sheep_loc, start))



