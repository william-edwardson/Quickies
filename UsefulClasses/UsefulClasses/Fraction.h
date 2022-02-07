#pragma once
// Fraction: A class to handle operations involving fractions
// TODO: TEST!!!
// And maybe refactor...
#include <iostream>

class Fraction {
private:
	// numerator and denominator
	int n, d;

	// Helper functions
	void normalise();
	int gcf(int a, int b);
	int lcm(int a, int b);

	// Arithmetic logic
	Fraction add(const Fraction& b);
	Fraction sub(const Fraction& b);
	Fraction mult(const Fraction& b);
	Fraction div(const Fraction& b);
public:
	// Constructors
	Fraction(int nVal = 0, int dVal = 1) {
		set(nVal, dVal);
	}
	Fraction(const Fraction& b) {
		n = b.n; d = b.d;
	};
	Fraction(char* s);

	// Setters
	void set(int nVal, int dVal) {
		n = nVal; d = dVal; normalise();
	}
	void setN(int nVal) {
		n = nVal;
	}
	void setD(int dVal) {
		d = dVal;
	}
	// Getters
	int getN() { return n; }
	int getD() { return d; }

	// Operators
	Fraction operator+(const Fraction& b) { return add(b); };
	Fraction operator-(const Fraction& b) { return sub(b); };
	Fraction operator*(const Fraction& b) { return mult(b); };
	Fraction operator/(const Fraction& b) { return div(b); };
	Fraction& operator=(const Fraction& b) { set(b.n, b.d); return *this; }
	bool operator==(const Fraction& b) { return (n == b.n && d == b.d); }
	friend std::ostream& operator<<(std::ostream& o, Fraction& f);
	// TODO: Definitions
	bool operator<(const Fraction& b);
	bool operator>(const Fraction& b);
};