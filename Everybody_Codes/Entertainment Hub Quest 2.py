file = open('../input').readline().strip()

balloons = list(file)
def part_one():
    fluff_bolt_seq = ['R', 'G', 'B']
    bolt_num = 0
    balloon_idx = 0
    while balloon_idx < len(balloons):
        while balloon_idx<len(balloons) and  balloons[balloon_idx] == fluff_bolt_seq[bolt_num%len(fluff_bolt_seq)]:
            balloon_idx += 1
        else:
            balloon_idx += 1
        bolt_num += 1
    return bolt_num

def part_two():
    global balloons
    fluff_bolt_seq = ['R', 'G', 'B']
    original_balloons = balloons.copy()
    balloons = balloons * 99000
    bolt_num = 0
    while balloons:
        length_balloons = len(balloons)
        first_balloon = balloons.pop(0)
        if fluff_bolt_seq[bolt_num%len(fluff_bolt_seq)] == first_balloon and length_balloons%2 == 0:
            balloons.pop(int(length_balloons/2)-1)
        bolt_num += 1
    return bolt_num






print(part_two())