#define _CRT_SECURE_NO_WARNINGS 1

#include <cstdlib>
#include <iostream>
#include <string>

//Dado un vector de n elementos realizar un programa que permita
//determinar la suma de los elementos en posicion par

using namespace std;

int main(int argc, char *argv[])
{
	int Vect[100], n = 0, i = 0, sum = 0;
	while (i < 100) { Vect[i] = NULL; i++;	}
	string op="s";
	
	while (op == "s"){
		cout << "Ingrese un elemento: ";
		cin >> Vect[n];
		n++;
		//fflush(stdin);
		cout << "seguir ingresando? (s/n):  ";
		cin >> (op);
	}

	n = 1; i = 0;

	while (n < 100)
	{
		sum += Vect[n];
		n += 2;
	}
	cout << "La suma de los numeros en posicion par es: " << sum << endl;
	
	system("PAUSE");
	return 0;
}