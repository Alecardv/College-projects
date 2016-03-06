#include <cstdlib>
#include <iostream>
#include <string>

//Una empresa desea procesar las ventas realizadas mes a mes con el fin de obtener la siguiente informacion anual:
//Mes en el que se obtuvo la mejor venta
//El Monto de la venta maxima obtenida
//Total de las ventas
//Promedio de las ventas

using namespace std;

int main(int argc, char *argv[])
{
	int Ventas[12][10];
	int n=0, temp, mestemp, i=0;

	while (n < 12)
	{ 
		while (i < 10)
		{
			Ventas[n][i] = NULL;
			i++;
		}
		n++;
	}

	string op = "s";
	i = 0;
	while (op != "n")
	{
		system("CLS");
		cout << "Ingrese cantidad vendida: ";
		cin >> temp;
		cout << "Ingrese el numero del mes: ";
		cin >> mestemp;
		Ventas[mestemp - 1][i] = temp;
		cout << "Correcto! Continuar ingresando? (s/n): ";
		cin >> op;
	}

	n = 0; i = 0; int mayor = 0, mayormes = 0, mayor1 = 0;
	cout << "Mes en el que se obtuvo la mejor venta: ";
	while (n < 12)
	{
		while (i < 10)
		{
			if (mayor > Ventas[n][i])
			{
				i++;
			}
			else
			{
				mayor = Ventas[n][i];
				i++;
			}
			mayor1 = mayor;
		}
		
		if (mayormes = n)
		n++;
	}

	return 0;
}