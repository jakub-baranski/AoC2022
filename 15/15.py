import re
from collections import namedtuple, defaultdict

inp = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

Point = namedtuple('Point', ['x', 'y'])


def _manhattan_distance(node1: Point, node2: Point) -> int:
    return int(abs(node1[0] - node2[0]) + abs(node1[1] - node2[1]))


def _find_element_not_in_ranges(ranges: list[list[int]]):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    current_range = range(sorted_ranges[0][0], sorted_ranges[0][1] + 1)
    for i in range(1, len(ranges)):
        next_range = sorted_ranges[i]
        if next_range[0] in current_range and next_range[1] in current_range:
            continue
        if next_range[0] in current_range and next_range[1] >= current_range.stop:
            current_range = range(current_range[0], next_range[1] + 1)
        else:
            return next_range[0] - 1


def solution():

    line_ranges: dict[int, list[list[int]]] = defaultdict(list)
    line_beacon: dict[int, set[Point]] = defaultdict(set)

    for line in inp.split('\n'):
        points = list(map(int, re.findall(r'-?[0-9]+', line)))
        sensor = Point(points[0], points[1])
        beacon = Point(points[2], points[3])
        line_beacon[beacon.y].add(beacon)
        distance = _manhattan_distance(sensor, beacon)

        for y in range(distance + 1):
            points_in_row = (distance * 2 + 1) - y * 2
            points_to_side = int((points_in_row - 1) / 2)
            line_ranges[sensor.y + y].append([sensor.x - points_to_side, sensor.x + points_to_side + 1])
            line_ranges[sensor.y - y].append([sensor.x - points_to_side, sensor.x + points_to_side + 1])

    line = 10
    points_set = set()
    for r in line_ranges[line]:
        points_set.update({x for x in range(r[0], r[1])})
    print(len(points_set) - len(line_beacon[line]))

    # part two

    for y, ranges in line_ranges.items():
        if 0 < y < 20:
            res = _find_element_not_in_ranges(ranges)
            if res:
                print(res, y)
                print('Frequency: ', y + res * 4000000)

solution()
