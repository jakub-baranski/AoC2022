import math
from queue import PriorityQueue

test_inp = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""



start = 'S'
end = 'E'


def get_value(letter: str) -> int:
    if letter == 'S':
        return get_value('a')
    if letter == 'E':
        return get_value('z')
    return ord(letter) - ord('a')


def dijkstra(rows: list[list[str]], source: tuple[int, int], end: tuple[int, int]):

    priority_queue = PriorityQueue()
    distances = {}
    previous = {}
    # items are tuple of (priority, item)

    distances[source] = 0

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if (i, j) != source:
                distances[(i, j)] = math.inf
                previous[(i, j)] = None
            priority_queue.put_nowait((math.inf, (i, j)))

    while not priority_queue.empty():
        _prio, best_vertex = priority_queue.get()
        if best_vertex == end:
            break
        potential_neighbours = [
            (best_vertex[0] + 1, best_vertex[1]),
            (best_vertex[0] - 1, best_vertex[1]),
            (best_vertex[0], best_vertex[1] + 1),
            (best_vertex[0], best_vertex[1] - 1),
        ]
        neighbours = []
        for n in potential_neighbours:
            if n[0] < 0 or n[1] < 0:
                continue
            try:
                n_value = get_value(rows[n[0]][n[1]])
                if n_value <= get_value(rows[best_vertex[0]][best_vertex[1]]) + 1:
                    neighbours.append(n)
            except IndexError:
                continue

        for neighbour in neighbours:
            try:
                alt = distances[best_vertex] + 1
                neighbour_distance = distances[neighbour]
            except KeyError:
                continue
            if alt < neighbour_distance:
                distances[neighbour] = alt
                previous[neighbour] = best_vertex
                priority_queue.put_nowait((alt, neighbour))
    return distances


def dijkstra_p2(rows: list[list[str]], source: tuple[int, int]):

    priority_queue = PriorityQueue()
    distances = {}
    previous = {}
    # items are tuple of (priority, item)

    distances[source] = 0

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if (i, j) != source:
                distances[(i, j)] = math.inf
                previous[(i, j)] = None
            priority_queue.put_nowait((math.inf, (i, j)))

    while not priority_queue.empty():
        _prio, best_vertex = priority_queue.get()
        potential_neighbours = [
            (best_vertex[0] + 1, best_vertex[1]),
            (best_vertex[0] - 1, best_vertex[1]),
            (best_vertex[0], best_vertex[1] + 1),
            (best_vertex[0], best_vertex[1] - 1),
        ]
        neighbours = []
        for n in potential_neighbours:
            if n[0] < 0 or n[1] < 0:
                continue
            try:
                n_value = get_value(rows[n[0]][n[1]])
                if n_value >= get_value(rows[best_vertex[0]][best_vertex[1]]) - 1:
                    neighbours.append(n)
            except IndexError:
                continue

        for neighbour in neighbours:
            try:
                alt = distances[best_vertex] + 1
                neighbour_distance = distances[neighbour]
            except KeyError:
                continue
            if alt < neighbour_distance:
                distances[neighbour] = alt
                previous[neighbour] = best_vertex
                priority_queue.put_nowait((alt, neighbour))

    return distances

def part_one():
    rows = test_inp.split("\n")
    rows = [
        [c for c in row] for row in rows
    ]
    # row, column
    start_coord = (0, 0)
    end_coord = (0, 0)
    for i, r in enumerate(rows):
        if start in r:
            start_coord = (i, r.index(start))
        if end in r:
            end_coord = (i, r.index(end))


    distances = dijkstra(rows, start_coord, end_coord)
    print(distances[end_coord])


def part_two():
    # make E the starting point, calculate distances to a.
    # Reverse condition, so that next node must be 1 LOWER

    rows = test_inp.split("\n")
    rows = [
        [c for c in row] for row in rows
    ]
    # row, column
    lowest_points = set()
    end_coord = (0, 0)
    for i, r in enumerate(rows):
        for j, letter in enumerate(r):
            if letter == 'a':
                lowest_points.add((i, j))
        if end in r:
            end_coord = (i, r.index(end))

    distances = dijkstra_p2(rows, end_coord)
    lowest_points_distances = [distance for coords, distance in distances.items() if coords in lowest_points]
    print(min(lowest_points_distances))


part_one()

part_two()
