from collections import namedtuple
from dataclasses import dataclass

inp = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')


Point = namedtuple('Point', ['x', 'y'])

def get_points_between(point1: Point, point2: Point) -> list[Point]:
    if point1.x == point2.x:
        return [Point(point1.x, y) for y in range(min(point1.y, point2.y), max(point1.y, point2.y) + 1)]
    if point1.y == point2.y:
        return [Point(x, point1.y) for x in range(min(point1.x, point2.x), max(point1.x, point2.x) + 1)]


def part_two():

    rocks = set()
    sand = set()
    highest_y = 0
    lowest_y = 0
    highest_x = 500
    lowest_x = 500

    for line in inp:
        points = [Point(int(x), int(y)) for x, y in map(lambda pnt: pnt.split(','), line.split(' -> '))]
        for p1, p2 in zip(points, points[1:]):
            if p1.y > highest_y:
                highest_y = p1.y
            if p1.y < lowest_y:
                lowest_y = p1.y
            if p1.x > highest_x:
                highest_x = p1.x
            if p1.x < lowest_x:
                lowest_x = p1.x
            for p in get_points_between(p1, p2):
                rocks.add(p)

    part_two_line = get_points_between(Point(lowest_x - 5000, highest_y + 2), Point(highest_x + 5000, highest_y + 2))
    for p in part_two_line:
        rocks.add(p)

    sand_position = Point(500, 0)

    while True:
        expected_point = Point(sand_position.x, sand_position.y + 1)

        if expected_point.y > 10000:
            print("FUCK")
            break

        # # part 1 condition
        # if expected_point.y > highest_y:
        #     break

        if expected_point not in rocks and expected_point not in sand:
            sand_position = expected_point
            continue

        else:

            left_point = Point(expected_point.x - 1, expected_point.y)
            if left_point not in rocks and left_point not in sand:
                sand_position = Point(sand_position.x - 1, sand_position.y)
                continue
            else:
                right_point = Point(expected_point.x + 1, expected_point.y)
            if right_point not in rocks and right_point not in sand:
                sand_position = Point(sand_position.x + 1, sand_position.y)
                continue
            sand.add(sand_position)

            # part 2 condition:
            if Point(500, 0) in sand:
                break

            sand_position = Point(500, 0)

    print(len(sand))


# And one inside with small modifications...
part_two()
