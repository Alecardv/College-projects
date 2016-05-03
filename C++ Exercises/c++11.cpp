/* Desarrollado por: Jose Alejandro Cardona Valdes
 * NOTA: Unicamente compatible con el estandar C++11
 * para compilar en linux use: $g++ -std=c++11 p1.cpp
 */

//Taller de recursividad

#include <iostream>
#include <functional>
#include <stack>

using namespace std;

//1. Calculo del factorial
long factorial(int i)
{
	return (i == 1) ? 1 : i*factorial(i-1);
}

//2. Calculo de pontencias
int expt(int NUM, int exp)
{
	int result = 1;
	//Declaracion de funcion lambda
	std::function<int()> lambda = [&lambda, &exp, NUM, &result] ()
	{
		result = NUM*result;
		if (exp == 0) return 1;
		else if (exp == 1) return result;
		else
		{
			exp = exp-1;
			return lambda();
		}
	};
		return lambda();
}
	
//3. Secuencia del 2
void secuencia(int N)
{
	int count = 0;
	std::function<void ()> sec = [&sec, N, &count] ()
	{
		if (N == count) cout << "2^" << count << "=" << expt(2,count) << endl;
		else{
			cout << "2^" << count << "=" << expt(2,count) << " + ";
			count++;
			sec();
		}
	};
	sec();
}

//4. Sumar dos numeros recursivamente
// ¿Como? jaja

//5. Multiplicar dos numeros recursivamente
int multiplicar(int a, int b)
{
	int result = b;
	std::function<int ()> mult = [&mult, &a, b, &result] ()
	{
		if ((a == 0) || (b == 0)) return 0;
		else if (a == 1) return result;
		else{
			result = result + b;
			a--;
			mult();
		}
	};
	return mult();
}


//6. Serie fibonacci
int fibonacci(int n)
{
   	if (n<2) return n;
   	else return fibonacci(n-1) + fibonacci(n-2);
}

//7. Sumar desde 1 hasta n
int sum1(int result, int n)
{
	if (n == 0) return result;
	else sum1(result+n, n-1);
}

void sumarHasta(int n)
{
	int result = sum1(0,n);
	std::function<void (int)> print = [&, n, result] (int i)
	{
		if (i == n) cout << n << " = " << result << endl;
		else{
			cout << i << "+";
			print(i+1);
		}
	};
	print(1);
}

//8. Division de enteros mediante restas sucesivas
int division(int a, int b) {
	int cont = 1;
	int div = b;
	std::function <int ()> divSub = [&divSub, &b, &cont, a, div] ()
	{
		if (b >= a) return (b == a) ? cont : cont-1;
		else{
			b = b + div;
			cont++;
			divSub();
		}	
	};
	return divSub();
}

//9. Maximo comun divisor
long gcd(long a, long b)
{
	if (b == 0)	return a;
	return gcd(b, a % b);
}

//10. Convertir de base 10 a binario
void decToBin(int a)
{
	stack<int> pila;
	int div = a;
	
	std::function <void ()> recursion = [&recursion, &div, &pila] ()
	{
		div = div/2;
		if (div == 1) pila.push(1);
		else {
			if (div == 0) pila.push(0);
			else {
				if ((div % 2) == 0) {
					pila.push(0);
					recursion();
				}
				else {
					pila.push(1);
					recursion();
				}
			}
		}
	};
	recursion();
	while (!pila.empty())
	{
		cout << pila.top();
		pila.pop();
	}
}

int main(int argc, char const *argv[]){
	
	cout << endl;
	//cout << expt(2,3) << endl;
	//cout << factorial(10) << endl;
	//secuencia(10);
	//cout << multiplicar(183,99) << endl;
	//cout << fibonacci(5) << endl;
	//sumarHasta(5);
	//cout << division(20,3) << endl;
	//cout << gcd(20,8) << endl;
	//decToBin(64);
	cout << endl;

	return 0;
}