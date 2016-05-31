#include <string>
#include <iostream>
#include <fstream>
#include "Reservas.h"

using namespace std;



int menuPrincipal() {
	int option;
	clearscreen();
	cout << " +-------------- Menu Principal --------------+" << endl;
	cout << " | 1. Inicio                                  |" << endl;
	cout << " | 2. Promociones                             |" << endl;
	cout << " | 3. Consultar reservas                      |" << endl;
	cout << " |                                            |" << endl;
	cout << " | 0. Terminar                                |" << endl;
	cout << " +--------------------------------------------+" << endl;
	cout << "  Seleccione una opcion: ";
	cin >> option;
	return option;
}

// Toma un string, le agrega una palabra ingresada por el usuario
// y rellena con espacios en blanco hasta alcanzar el tamano indicado
void getLine(string &in, int size) {
	string out;
	getline(cin, in);
	for (unsigned int i = 0; i <= size - in.length(); i++) {
		out += " ";
	}
	in = out + in;
}

// Esta funcion recibe un numero y devuelve un string de esa longitud
// lleno de espacios en blanco.
string strFormat(int size) {
	string out;
	for (int i = 0; i <= size; i++) {
		out += " ";
	}
	return out;
}

// Elimina espacios en blanco al comienzo y final de un string
string trim(string& str) {
	size_t first = str.find_first_not_of(' ');
	size_t last = str.find_last_not_of(' ');
	return str.substr(first, (last - first + 1));
}

// Imprime el menu de inicio con un formato agradable
void prettyPrintInicio(bool regreso, string ori, string dest, string dateout, string dateback, string code) {
	clearscreen();
	cout << " +-------------- INICIO --------------+" << endl;
	cout << " | Origen: " << ori + " |" << endl;
	cout << " | Destino: " << dest + " |" << endl;
	cout << " | Fecha Salida: " << dateout + " |" << endl;
	if (regreso) {
		cout << " | Fecha Regreso: " << dateback + " |" << endl;
	}
	cout << " | Cod. Descuento: " << code + " |" << endl;
	cout << " +------------------------------------+" << endl;
}

// Administra todo lo concerniente al menu inicio
bool menuInicio() {
	string ori = strFormat(25), dest = strFormat(24), dateout = strFormat(19), dateback = strFormat(18), code = strFormat(17);

	cin.ignore();

	int opt;
	bool regreso = true;

	clearscreen();
	cout << "1. Ida y regreso." << endl;
	cout << "2. Solo ida." << endl;
	cin >> opt;

	switch (opt) {
		case 1: regreso = true; break;
		case 2: regreso = false; break;
		default: break;
	}

	cin.ignore();

	prettyPrintInicio(regreso, ori, dest, dateout, dateback, code);
	cout << "Ingrese Origen: ";
	getLine(ori, 25);

	prettyPrintInicio(regreso, ori, dest, dateout, dateback, code);
	cout << "Ingrese Destino: ";
	getLine(dest, 24);

	prettyPrintInicio(regreso, ori, dest, dateout, dateback, code);
	cout << "Ingrese Fecha de Salida: ";
	getLine(dateout, 19);

	if (regreso) {
		prettyPrintInicio(regreso, ori, dest, dateout, dateback, code);
		cout << "Ingrese Fecha de Regreso: ";
		getLine(dateback, 18);
	}

	prettyPrintInicio(regreso, ori, dest, dateout, dateback, code);
	cout << "Ingrese Cod. de descuento (0: Ninguno): ";
	getLine(code, 17);

	while (trim(code) != "0") {
		prettyPrintInicio(regreso, ori, dest, dateout, dateback, code);
		if (!buscarCodigo(trim(dest), trim(code))) {
			cout << "Ese codigo/ciudad de destino no coinciden o el codigo no existe" << endl;
			cout << "Ingrese Cod. de descuento (0: Ninguno): ";
			getLine(code, 17);
		} else {
			break;
		}
	}
	prettyPrintInicio(regreso, ori, dest, dateout, dateback, code);
	cout << " | 1. Reservar                        |" << endl;
	cout << " | 2. Ignorar y Volver                |" << endl;
	cout << " | 0. Salir                           |" << endl;
	cout << " +------------------------------------+" << endl;

	if (!regreso) { dateback = "_"; }

	cin >> opt;
	switch (opt) {
		case 1: reservar(trim(ori), trim(dest), trim(dateout), trim(dateback), trim(code)); return true;
		case 2: return true;
		case 0:	return false;
		default: break;
	}
	return false;
}

bool menuPromociones() {
	int opt;
	clearscreen();
	cout << "-------------- PROMOCIONES --------------" << endl;
	mostrarPromociones();
	cout << endl;
	cout << " 1. Volver" << endl;
	cout << " 0. Terminar" << endl;
	cin >> opt;
	switch (opt) {
		case 1: return true;
		case 0:	return false;
		default: break;
	}
	return false;
}

bool menuConsultar() {
	int opt;
	clearscreen();
	cout << "-------------- CONSULTAR --------------" << endl;
	mostrarReservas();
	cout << endl;
	cout << " 1. Volver" << endl;
	cout << " 0. Terminar" << endl;
	cin >> opt;
	switch (opt) {
		case 1:	return true;
		case 0:	return false;
		default: break;
	}
	return false;
}

int main() {
	bool opt = true;
	while (opt) {
		switch (menuPrincipal()) {
			case 1:	opt = menuInicio();	break;
			case 2:	opt = menuPromociones(); break;
			case 3:	opt = menuConsultar(); break;
			default: opt = false; break;
		}
	}
	cout << "  Gracias por su visita" << endl;
	cout << " +--------------------------------------------+" << endl;
    cout << " Presione una tecla para continuar . . . ";
    cin.get();
}
