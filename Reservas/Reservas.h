#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>


using namespace std;

void clearscreen(){
#ifdef WINDOWS
    system("cls");
#else
    system("clear");
#endif
}

// Cuenta las lineas del archivo de reservas.
int countlines() {
	ifstream file("reservas.txt");
	int count = 0;
	string line;
	while (getline(file, line)) {
		count++;
	}
	file.close();
	return count;
}

// Escribe una reserva en el archivo de reservas y le asigna un ID
void reservar(string ori, string dest, string dateout, string dateback, string code) {
	fstream fs;
	fs.open("reservas.txt", fstream::in | fstream::out | fstream::app);
	int pos = countlines();
	string id = std::to_string(pos + 1) + std::to_string(rand() % 100);
	fs << id + " " << ori + " " << dest + " " << dateout + " " << dateback + " " << code + " " << endl;
}

// Lee el archivo de promociones y las muestra en pantalla
void mostrarPromociones() {
	clearscreen();
	ifstream fs("promociones.txt");
	string dest, cod;
	while (fs >> dest >> cod) {
		cout << "Codigo: " << cod << "    Destino: " << dest << endl;
	}
}

// Lee el archivo de reservas y las muestra en pantalla
void mostrarReservas() {
	ifstream fs("reservas.txt");
	string id, ori, dest, dateout, dateback, code;
	while (fs >> id >> ori >> dest >> dateout >> dateback >> code) {
		cout << ori + " " << dest + " " << dateout + " " << dateback + " " << code << endl;
	}
}

bool buscarCodigo(string dest, string code) {
	ifstream fs("promociones.txt");
	string file_dest, file_code;
	while (fs >> file_dest >> file_code) {
		if (file_code == code && file_dest == dest) return true;
	}
	return false;
}
