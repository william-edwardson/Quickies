#include <iostream>
#include <cstdlib>
#include <cstring>
#include "Fraction.h"

void Fraction::normalise() {
	// Handling 0s
	if (d == 0 || n == 0) {
		n = 0; d = 1; // 0/1
	}

	// Negative sign on the numerator
	if (d < 0) {
		n *= -1; d *= -1;
	}

	// Reduce to lowest form
	int g = gcf(n, d);
	n /= g; d /= g;
}

// Greatest common factor
int Fraction::gcf(int a, int b) {
	if (b == 0)
		return abs(a);
	else
		return gcf(b, a % b);
}

// Least common multiple
int Fraction::lcm(int a, int b) {
	int g = gcf(a, b);
	return a * b / g;
}

Fraction::Fraction(char* s) {
	int n = 0, d = 1;

	// Get the parts before and after the /
	char* p1 = strtok(s, "/, ");
	char* p2 = strtok(NULL, "/, ");
	
	if (p1)
		n = atoi(p1);
	if (p2)
		d = atoi(p2);

	normalise();
}

// Addition: A/B + C/D = (A(L/B) + C(L/D))/L
Fraction Fraction::add(const Fraction& b) {
	int l = lcm(d, b.d);
	int q1 = l / d; int q2 = l / b.d;
	return Fraction(n * q1 + b.n * q2, l);
}

// Just add -1 * the other fraction
Fraction Fraction::sub(const Fraction& b) {
	b.n *= -1;
	return this->add(b);
}

// Multiplication: A/B * C/D = AC/BD
Fraction Fraction::mult(const Fraction& b) {
	return Fraction(n * b.n, d * b.d);
}

// Division: Multiplication by 1/b
Fraction Fraction::div(const Fraction& b) {
	if (b.n == 0) {
		std::cout << "Error: Can't divide by 0!\n";
		return;
	}
	return this->mult(Fraction(b.d, b.n));
	//... Or just use std::swap on b.n & b.d
}

// String output
std::ostream& operator<<(std::ostream& o, Fraction& f) {
	o << f.n << "/" << f.d;
	return o;
}
