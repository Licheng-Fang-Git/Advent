class Segment:
    def __init__(self, middle):
        self.mid = middle
        self.left = None
        self.right = None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_mid(self):
        return self.mid

    def print_segment(self):
        # if self.left:
        #     print("left:", self.left)
        if self.mid:
            print(self.mid, end="")
        # if self.right:
        #     print("right:", self.right)

file = open("../input").read().split("\n")

def find_fish_bone(seg):
    armor = []
    for i in seg:
        if not armor:
            armor.append(Segment(i))
            continue
        for j in range(len(armor)):
            if armor[j].mid > i:
                if armor[j].get_left() is not None and j == len(armor)-1:
                    armor.append(Segment(i))
                elif armor[j].get_left() is not None:
                    continue
                else:
                    armor[j].set_left(i)
                    break

            elif armor[j].mid < i:
                if armor[j].get_right() is not None and j == len(armor)-1:
                    armor.append(Segment(i))
                elif armor[j].get_right() is not None:
                    continue
                else:
                    armor[j].set_right(i)
                    break
            elif armor[j].mid == i and j == len(armor)-1:
                armor.append(Segment(i))
                break
    s = ""
    for bone in armor:
        s += str(bone.get_mid())
    return s

swords = []
for sword in file:
    sword = sword.split(":")
    sword = list(map(int,sword[1].split(",")))
    print(sword)
    print(find_fish_bone(sword))
    # swords.append(find_fish_bone(sword))

swords = list(map(int,swords))

# strongest_s = max(swords)
# weakest_s = min(swords)
# print(strongest_s - weakest_s)

