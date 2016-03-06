#include <cstdlib>
#include <iostream>
#include <string>

//Capturar un vector de n elementos, luego ingresar un numero entero por teclado
//validar si hace parte del vector, imprimir el numero de veces que se encuentre y su posicion

using namespace std;

int main(int argc, char *argv[])
{
	int vect[100], n = 0, i = 0, pertenece = 0;
	while (i < 100) { vect[i] = NULL; i++;	}
	string op="s";
		
	while (op == "s"){
		cout << "ingrese un elemento: ";
		cin >> vect[n];
		n++;
		//fflush(stdin);
		cout << "seguir ingresando? (s/n):  ";
		cin >> (op);
	}

	cout << "Que numero desea buscar?: ";
	cin >> i;
	n = 0;
	while (n < 100)
	{
		if (vect[n] == i)
		{
			pertenece++;
			n++;
		}
		else n++;
	}

	cout << "El numero " << i << " se encuentra " << pertenece << " veces." << endl;

	system("PAUSE");
}