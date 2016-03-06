#include <sstream>
#include <iostream>
#include "BigNum.h"

using namespace std;

BigNum factorial(BigNum n) {
	BigNum uno = 1, cero = 0;
	if (n == cero) return uno;
	else return n*factorial(n-uno);
}

BigNum fib(BigNum n) {
	BigNum uno = 1;
	BigNum pp = 0, p = 1;
	for (BigNum i=2; i<n; i++)
	{
		BigNum op = p;
		p = p + pp;
		pp = op;
	}
	return p + pp;
}

int main(int argc, char const *argv[]){
	
	BigNum a = "1500", b;
	b = fib(a);
	
	b.print();

	return 0;
}