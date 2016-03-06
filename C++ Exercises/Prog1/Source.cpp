#define _CRT_SECURE_NO_WARNINGS 1 //Necesario para que el compilador MS Visual Studio pueda trabajar con ciertas funciones.

#include <conio.h>
#include <iostream>
#include "Header.h"

using namespace std;

int main(){

	int d, f;
	char Oracion[1000], Palabra[10], opcion='0';

	cout << "Ingrese un parrafo: " << endl;
	gets(Oracion);

	while (opcion != '7'){
		system("cls"); //Borra la pantalla
		cout << endl
			<< "1. Cuantas veces se encuentra una palabra en el parrafo." << endl
			<< "2. Cuantas palabras hay en el parrafo." << endl
			<< "3. Cuantos caracteres hay en el parrafo." << endl
			<< "4. Histograma de caracteres." << endl
			<< "5. Palabras en orden alfabetico." << endl
			<< "6. Palabras segun su tamano." << endl
			<< "7. Salir." << endl
			<< endl << "Eliga una opcion : ";
		cin >> opcion;

		switch (opcion){
		case '1':
			cout << endl << "Ingrese la palabra: ";
			cin >> Palabra;
			cout << endl << "La palabra se repite: " << buscarPalabra(Oracion,Palabra) << " veces" << endl;
			system("PAUSE"); //Pausa la ejecucion del programa
			break;
		case '2':
			f = contarPalabras(Oracion);
			cout << endl << "El numero de palabras en el parrafo es: " << f << endl;
			system("PAUSE");
			break;
		case '3':
			d = contarCaracteres(Oracion);
			cout << endl << "El numero de caracteres es: " << d << endl;
			system("PAUSE");
			break;
		case '4':
			cout << endl << "El Histograma es" << endl;
			histograma(Oracion);
			system("PAUSE");
			break;
		case '5':
			cout << endl;
			system("PAUSE");
			break;
		case '6':
			cout << endl;
			system("PAUSE");
			break;
		}
	}

	return 0;
}