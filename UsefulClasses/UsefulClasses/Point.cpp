#include "Point.h"

void Point::set(double xVal, double yVal) {
	x = xVal; y = yVal;
}

bool Point::equals(const Point& other) {
	return (x == other.x && y == other.y);
}

void Point::translate(double dx, double dy) {
	x += dx;
	y += dy;
}
