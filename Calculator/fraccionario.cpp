#include "fraccionario.h"
#include "iostream"

using namespace std;

fraccionario::fraccionario()
{
	numerador = 0;
	denominador = 1;
}

fraccionario::fraccionario(long a, long b)
{
	numerador = a;
	denominador = b;
}

fraccionario::~fraccionario()
{
}

long fraccionario::gcd(long a, long b)
{
	if (b == 0)
		return a;
	return gcd(b, a % b);
}

void fraccionario::simplificar()
{
	long c = gcd(numerador, denominador);
	numerador = numerador/c;
	denominador = denominador/c;
}

fraccionario fraccionario::operator+(fraccionario b)
{
	fraccionario result;
	result.numerador = (numerador * b.denominador) + (denominador * b.numerador);
	result.denominador = (denominador * b.denominador);
	result.simplificar();
	return result;
}

fraccionario fraccionario::operator-(fraccionario b)
{
	fraccionario result;
	result.numerador = ((numerador * b.denominador) - (denominador * b.numerador));
	result.denominador = (denominador * b.denominador);
	result.simplificar();
	return result;
}

fraccionario fraccionario::operator*(fraccionario b)
{
	fraccionario result;
	result.numerador = numerador * b.numerador;
	result.denominador = denominador * b.denominador;
	result.simplificar();
	return result;
}

fraccionario fraccionario::operator/(fraccionario b)
{
	fraccionario result;
	result.numerador = numerador * b.denominador;
	result.denominador = denominador * b.numerador;
	result.simplificar();
	return result;
}

void fraccionario::display()
{
	printf("%i / %i \n", numerador, denominador);
}

int main()
{
	
	fraccionario a = fraccionario(3,2);
	fraccionario b = fraccionario(1,2);
	fraccionario c = a + b;
	c.display();
	//c.simplificar();
	//c.display();
	system("PAUSE");
	return 0;
}