#pragma once
// String: An attempt to reinvent the wheel
// and get some functionality of STL strings
// TODO: Add logic to the stubs!

class String {
private:
	char* str;
public:
	String();
	String(const char* s);
	String(const String& s2);
	~String();

	void cat(const char* s);
	void cpy(const char* s);

	operator char*() { return str; }
	String& operator=(const String& s);
	String& operator=(const char* s);
	String operator+(const char* s);
	bool operator==(const String& s2);
	bool operator<(const String& s2);
	bool operator>(const String& s2);
};