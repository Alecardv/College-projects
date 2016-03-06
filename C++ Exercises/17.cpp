#include <cstdlib>
#include <iostream>

//Leer 10 numeros enteros, almacenarlos en un vector y terminar si la 
//semisuma entera entre el valor mayor y el valor menor es un numero par.

using namespace std;

int main(int argc, char *argv[])
{
	int vec[10], n=0, mayor=0, menor=0, i = 0;
	cout << "Ingrese 10 valores para el vector: " << endl;

	while (n < 10){
		cin >> vec[n];
		n++;
	}

	//mayor:
	while (i < 10)
	{
		if (mayor > vec[i])
			i++;
		else{
			mayor = vec[i];
			i++;
		}
	}
	//menor
	i = 0;
	menor = vec[0];
	while (i < 10)
	{
		if (menor < vec[i])
			i++;
		else{
			menor = vec[i];
			i++;
		}
	}

	//semisuma
	int semisuma = (mayor + menor) / 2;
	cout << "La semisuma entre el mayor y el menor es: " << semisuma << endl;
	system("PAUSE");
}