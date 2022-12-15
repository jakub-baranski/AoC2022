package main

import (
	"errors"
	"math"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

var inp = `Sensor at x=2, y=18: closest beacon is at x=-2, y=15
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
Sensor at x=20, y=1: closest beacon is at x=15, y=3`

type Point struct {
	x int
	y int
}

func manhattanDistance(sensor *Point, beacon *Point) int {
	return int(math.Abs(float64(sensor.x-beacon.x)) + math.Abs(float64(sensor.y-beacon.y)))
}

type rangeComparator [][2]int

func (r rangeComparator) Len() int {
	return len(r)
}

func (r rangeComparator) Less(i, j int) bool {
	return r[i][0] < r[j][0]
}

func (r rangeComparator) Swap(i, j int) {
	r[i], r[j] = r[j], r[i]
}

func joinRanges(ranges [][2]int) ([2]int, error) {
	sort.Sort(rangeComparator(ranges))

	currentRange := ranges[0]

	for i := 1; i < len(ranges); i++ {
		nextRange := ranges[i]
		if nextRange[0] >= currentRange[0] && nextRange[0] <= currentRange[1] && nextRange[1] <= currentRange[1] && nextRange[1] >= currentRange[0] {
			continue
		} else if nextRange[0] >= currentRange[0] && nextRange[0] <= currentRange[1] && nextRange[1] >= currentRange[1] {
			currentRange = [2]int{currentRange[0], nextRange[1]}
		} else {
			return [2]int{}, errors.New(strconv.Itoa(nextRange[0] - 1))
		}

	}
	return currentRange, nil
}

func main() {

	partOneLine := 10
	partTwoLimit := 20

	lineRanges := make(map[int][][2]int)
	lineBeacon := make(map[int]map[int]bool)

	for _, line := range strings.Split(inp, "\n") {
		r, _ := regexp.Compile("-?[0-9]+")
		points := r.FindAllString(line, 4)
		pointsInt := [4]int{}
		for i, p := range points {
			pInt, _ := strconv.Atoi(p)
			pointsInt[i] = pInt
		}
		sensor := Point{pointsInt[0], pointsInt[1]}
		beacon := Point{pointsInt[2], pointsInt[3]}

		_, ok := lineBeacon[beacon.y]
		if ok {
			lineBeacon[beacon.y][beacon.x] = true
		} else {
			lineBeacon[beacon.y] = map[int]bool{beacon.x: true}
		}

		distance := manhattanDistance(&sensor, &beacon)

		for y := 0; y < distance+1; y++ {
			pointsInRow := (distance*2 + 1) - y*2
			pointsToSide := (pointsInRow - 1) / 2
			xPoints := [2]int{sensor.x - pointsToSide, sensor.x + pointsToSide + 1}
			lineRanges[sensor.y+y] = append(lineRanges[sensor.y+y], xPoints)
			lineRanges[sensor.y-y] = append(lineRanges[sensor.y-y], xPoints)

		}
	}

	println("PART ONE\n")

	r, _ := joinRanges(lineRanges[partOneLine])

	impossiblePoints := int(math.Abs(float64(r[0]))+math.Abs(float64(r[1]))) - len(lineBeacon[partOneLine])

	println("PART ONE ", impossiblePoints)

	// PART TWO

	for y, ranges := range lineRanges {
		if y > 0 && y < partTwoLimit {
			_, err := joinRanges(ranges)
			if err != nil {
				errValue, _ := strconv.Atoi(err.Error())
				println("PART TWO ", strconv.Itoa(errValue*4000000+y))
				break
			}

		}
	}

}
