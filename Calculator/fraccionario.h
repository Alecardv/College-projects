#pragma once
class fraccionario
{
public:
	fraccionario();
	fraccionario(long, long);
	~fraccionario();
	long gcd(long, long);
	void simplificar();
	fraccionario operator +(fraccionario b);
	fraccionario operator -(fraccionario b);
	fraccionario operator *(fraccionario b);
	fraccionario operator /(fraccionario b);
	void display();

private:
	long numerador;
	long denominador;
};

