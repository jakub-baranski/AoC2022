package main

import (
	"math"
	"strconv"
	"strings"
)

var inp = `498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9`

type Point struct {
	x int
	y int
}

func getPointsBetween(point1 *Point, point2 *Point) map[Point]bool {
	points := make(map[Point]bool)
	if point1.x == point2.x {

		for y := math.Min(float64(point1.y), float64(point2.y)); y < math.Max(float64(point1.y), float64(point2.y))+1; y++ {
			points[Point{point1.x, int(y)}] = true
		}
	} else {
		for x := math.Min(float64(point1.x), float64(point2.x)); x < math.Max(float64(point1.x), float64(point2.x))+1; x++ {
			points[Point{int(x), point1.y}] = true
		}
	}
	return points
}

func main() {

	inpList := strings.Split(inp, "\n")

	rocks := make(map[Point]bool)
	sand := make(map[Point]bool)

	highestY := 0
	lowestY := 0
	highestX := 500
	lowestX := 500

	for _, line := range inpList {
		coords := strings.Split(line, " -> ")
		for i := 0; i < len(coords)-1; i++ {

			point1 := coords[i]
			point1Coords := strings.Split(point1, ",")
			p1X, _ := strconv.Atoi(point1Coords[0])
			p1Y, _ := strconv.Atoi(point1Coords[1])
			p1 := Point{int(p1X), int(p1Y)}

			point2 := coords[i+1]
			point2Coords := strings.Split(point2, ",")
			p2X, _ := strconv.Atoi(point2Coords[0])
			p2Y, _ := strconv.Atoi(point2Coords[1])
			p2 := Point{int(p2X), int(p2Y)}

			for _, p := range [2]Point{p1, p2} {
				if p.y > highestY {
					highestY = p.y
				}
				if p.x > highestX {
					highestX = p.x
				}
				if p.y < lowestY {
					lowestY = p.y
				}
				if p.x < lowestX {
					lowestX = p.x
				}
			}

			for rock, _ := range getPointsBetween(&p1, &p2) {
				rocks[rock] = true
			}
		}

	}

	// COMMENT FOR PART ONE
	partTwoLine := getPointsBetween(&Point{lowestX - 5000, highestY + 2}, &Point{highestX + 5000, highestY + 2})
	for p, _ := range partTwoLine {
		rocks[p] = true
	}

	// END COMMENT

	sandPosition := Point{500, 0}

	for {
		expectedPoint := Point{sandPosition.x, sandPosition.y + 1}
		// COMMENT FOR PART 2
		//if expectedPoint.y > highestY {
		//	break
		//}
		// END

		_, inRock := rocks[expectedPoint]
		_, inSand := sand[expectedPoint]
		if !inRock && !inSand {
			sandPosition = expectedPoint
			continue
		}

		leftPoint := Point{expectedPoint.x - 1, expectedPoint.y}
		_, inRock = rocks[leftPoint]
		_, inSand = sand[leftPoint]

		if !inSand && !inRock {
			sandPosition = Point{sandPosition.x - 1, sandPosition.y}
			continue
		} else {
			rightPoint := Point{expectedPoint.x + 1, expectedPoint.y}
			_, inRock = rocks[rightPoint]
			_, inSand = sand[rightPoint]
			if !inRock && !inSand {
				sandPosition = Point{sandPosition.x + 1, sandPosition.y}
				continue
			}
		}
		sand[sandPosition] = true

		// Part 2 break. Doesn't break part 1 so it's cool
		_, startInSand := sand[Point{500, 0}]
		if startInSand {
			break
		}

		sandPosition = Point{500, 0}

	}
	println(len(sand))

	// Visualization...

	//for y := lowestY - 5; y < highestY+5; y++ {
	//
	//	for x := lowestX - 105; x < highestX+105; x++ {
	//		_, isRock := rocks[Point{x, y}]
	//		_, isSand := sand[Point{x, y}]
	//		if isRock {
	//			print("#")
	//		} else if isSand {
	//			print("o")
	//		} else {
	//			print(".")
	//		}
	//
	//	}
	//	print("\n")
	//
	//}
}
