import json
from functools import cmp_to_key

inp = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def compare_lists(l1, l2) -> int:

    for i in range(max([len(l1), len(l2)])):
        try:
            left = l1[i]
        except IndexError:
            return 1
        try:
            right = l2[i]
        except IndexError:
            return -1
        result = compare(left, right)
        if result == 0:
            continue
        return result
    return 0


def compare_ints(i1, i2) -> int:
    if i1 == i2:
        return 0
    if i1 < i2:
        return 1
    return -1


def resolve_mixed_types(left, right) -> tuple:
    if isinstance(left, int):
        return [left], right
    else:
        return left, [right]


def compare(left, right) -> int:
    if type(left) != type(right):
        left, right = resolve_mixed_types(left, right)
    if isinstance(left, int):
        return compare_ints(left, right)
    else:
        return compare_lists(left, right)


def part_one():
    pairs = inp.split('\n\n')
    ordered = []
    for i, pair in enumerate(pairs):
        left, right = pair.split('\n')
        left, right = json.loads(left), json.loads(right)
        result = compare(left, right)
        if result in [1, 0]:
            ordered.append(i + 1)

    print(sum(ordered))


def part_two():
    pairs = inp.replace('\n\n', '\n').split('\n')
    pairs = [json.loads(p) for p in pairs]
    pairs += [ [[2]], [[6]] ]
    result = sorted(pairs, key=cmp_to_key(compare), reverse=True)
    print((result.index([[2]]) + 1) * (result.index([[6]]) + 1))


part_one()
part_two()
