#include <cstdlib>
#include <iostream>

//Capturar dos vectores de n elementos, generar otro vector con la suma de
//los anteriores mostrar en pantalla el vector resultado

using namespace std;

int main(int argc, char *argv[]) {

	int vec1[10], vec2[10], vec3[10];
	int n = 0, i = 0, j = 0;

	cout << "Recibiendo el primer vector (10 elementos): " << endl;
	while (n < 10) {
		cin >> vec1[n];
		n++;
	}

	cout << "Recibiendo el segundo vector (10 elementos): " << endl;
	while (i < 10) {
		cin >> vec2[i];
		i++;
	}

	while (j < 10) {
		vec3[j] = vec1[j]+vec2[j];
		j++;
	}
	
	cout << "El vector suma resultante es: ";
	n = 0;
	while (n < 10) {
		cout << vec3[n] << " ";
		n++;
	}
	cout << endl;
	system("PAUSE");
		
}