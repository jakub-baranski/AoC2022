# https://adventofcode.com/2022/day/8

test = """30373
25512
65332
33549
35390"""

rows = [[int(a) for a in line.strip()] for line in test.split('\n')]


def get_directions(x, y):
    column = [r[x] for r in rows]
    row = rows[y]
    left, right = row[:x][::-1], row[x + 1:]
    top, bottom = column[:y][::-1], column[y + 1:]
    return left, right, top, bottom


def check_row_visible(x, y) -> bool:
    element = rows[y][x]
    left, right, top, bottom = get_directions(x, y)
    try:
        for direction in [left, right, top, bottom]:
            next(r for r in direction if r >= element)
    except StopIteration:
        return True
    return False


def get_scenic_rating(x, y) -> int:
    rating = 0
    element = rows[y][x]
    left, right, top, bottom = get_directions(x, y)
    for direction in [left, right, top, bottom]:
        dir_rating = 0
        for r in direction:
            if r < element:
                dir_rating += 1
            else:
                dir_rating += 1
                break
        rating = dir_rating if not rating else rating * dir_rating
    return rating


def part_one():
    counter = 0
    for x in range(1, len(rows[0]) - 1):
        for y in range(1, len(rows) - 1):
            if check_row_visible(x, y):
                counter += 1
    return counter + (len(rows) - 1 + len(rows[0]) - 1) * 2


def part_two():
    ratings = []
    for x in range(1, len(rows[0]) - 1):
        for y in range(1, len(rows) - 1):
            ratings.append(get_scenic_rating(x, y))
    return max(ratings)


print(part_one())
print(part_two())
