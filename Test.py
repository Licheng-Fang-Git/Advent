from collections import Counter
with open("input") as file:
    lines = file.readlines()

beam_counts = Counter({lines[0].index("S"): 1})

splitter_data = [{i for i, char in enumerate(row) if char == "^"} for row in lines[2::2]]
print(splitter_data)
for i, row in enumerate(splitter_data):
    updated = Counter()
    print(beam_counts)
    print(row)
    for column, count in beam_counts.items():
        print(column,count)
        if column in row:
            updated[column - 1] += count
            updated[column + 1] += count
        else:
            updated[column] += count
    beam_counts = updated
print(beam_counts)
print(sum(beam_counts.values()))