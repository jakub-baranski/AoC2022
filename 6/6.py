# https://adventofcode.com/2022/day/6

test = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def part_one(marker_len: int):
    last_4 = []
    for i, c in enumerate(test):
        last_4 = (last_4[1:] if len(last_4) > marker_len - 1 else last_4) + [c]
        if len(set(last_4)) == marker_len:
            return i + 1


print(part_one(4))
print(part_one(14))  # part two actually

