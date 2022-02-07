#pragma once
// Point: A class to handle operations involving geometric points

class Point {
private:
	double x, y;
public:
	Point(double xVal = 0, double yVal = 0) : x(xVal), y(yVal) {}
	void set(double xVal, double yVal);
	double getX() { return x; }
	double getY() { return y; }

	bool equals(const Point& other);
	void translate(double dx, double dy);

	// TODO: Write their definitions
	Point operator+(const Point& b); // componentwise addition
	Point operator*(const int& s); // scalar multiplication
	Point operator-(const Point& b); // distance
};