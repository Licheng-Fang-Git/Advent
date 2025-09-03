import re
from collections import deque

file = open("../input").read()
players = int(re.findall("\d+", file.split(";")[0])[0])
last_points = int(re.findall("\d+", file.split(";")[1])[0])
print(players, last_points)
player_turns = [ply for ply in range(1, players + 1)]
def solve_one():
    player_turns_idx = 0
    curr_marble, curr_idx = 1, 1
    marble_game = [0,1]
    highest_points = 0
    while curr_marble < last_points:
        player_turns_idx = (player_turns_idx + 1) % len(player_turns)
        player = player_turns[player_turns_idx]
        curr_marble += 1
        if curr_marble % 23 == 0:
            place_idx = (curr_idx - 7) % len(marble_game)
            replace = marble_game.pop(place_idx)
            curr_idx = place_idx
            players_score[player] += curr_marble + replace
            highest_points = max(players_score[player], highest_points)

        else:
            place_idx = (curr_idx + 2)%len(marble_game)
            curr_idx = place_idx
            marble_game.insert(place_idx, curr_marble)

    return highest_points

players_score = {ply : 0 for ply in range(1,players+1)}

def solve_two():
    curr_marble = 0
    dq = deque([0])
    player = 0
    player_idx = 0
    while curr_marble < last_points:
        player_idx = (player_idx +1)%len(player_turns)
        player = player_turns[player_idx]
        curr_marble += 1
        if curr_marble % 23 == 0:
            pass
        else:
            dq.rotate(-1)
            dq.append(curr_marble)
        print(dq)


solve_two()


