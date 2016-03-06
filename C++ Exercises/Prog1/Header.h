#include <conio.h>
#include <iostream>
#include <string>

using namespace std;

int contarCaracteres(char A[]){
	int k, es = 0, c;
	for (k = 0; A[k] != '\0'; k++){
		if (A[k] == ' '){
			es++;
		}
	}
	c = k - es;
	return c;
}

void histograma(char A[]){
	int a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0, i = 0, j = 0, k = 0, l = 0, m = 0, n = 0, o = 0, p = 0, q = 0, r = 0, s = 0, t = 0, u = 0, v = 0, w = 0, x = 0, y = 0, z = 0, cd;
	for (k = 0; A[k] != '\0'; k++){
		if (A[k] == 'a') a++;
		if (A[k] == 'b') b++;
		if (A[k] == 'c') c++;
		if (A[k] == 'd') d++;
		if (A[k] == 'e') e++;
		if (A[k] == 'f') f++;
		if (A[k] == 'g') g++;
		if (A[k] == 'h') h++;
		if (A[k] == 'i') i++;
		if (A[k] == 'j') j++;
		if (A[k] == 'k') k++;
		if (A[k] == 'l') l++;
		if (A[k] == 'm') m++;
		if (A[k] == 'n') n++;
		if (A[k] == 'o') o++;
		if (A[k] == 'p') p++;
		if (A[k] == 'q') q++;
		if (A[k] == 'r') r++;
		if (A[k] == 's') s++;
		if (A[k] == 't') t++;
		if (A[k] == 'u') u++;
		if (A[k] == 'v') v++;
		if (A[k] == 'w') w++;
		if (A[k] == 'x') x++;
		if (A[k] == 'y') y++;
		if (A[k] == 'z') z++;
	}
	cout << "a "; for (cd = 1; cd <= a; cd++){ cout << "* "; }cout << "\n";
	cout << "b "; for (cd = 1; cd <= b; cd++){ cout << "* "; }cout << "\n";
	cout << "c "; for (cd = 1; cd <= c; cd++){ cout << "* "; }cout << "\n";
	cout << "d "; for (cd = 1; cd <= d; cd++){ cout << "* "; }cout << "\n";
	cout << "e "; for (cd = 1; cd <= e; cd++){ cout << "* "; }cout << "\n";
	cout << "f "; for (cd = 1; cd <= f; cd++){ cout << "* "; }cout << "\n";
	cout << "g "; for (cd = 1; cd <= g; cd++){ cout << "* "; }cout << "\n";
	cout << "h "; for (cd = 1; cd <= h; cd++){ cout << "* "; }cout << "\n";
	cout << "i "; for (cd = 1; cd <= i; cd++){ cout << "* "; }cout << "\n";
	cout << "j "; for (cd = 1; cd <= j; cd++){ cout << "* "; }cout << "\n";
	cout << "k "; for (cd = 1; cd <= k; cd++){ cout << "* "; }cout << "\n";
	cout << "l "; for (cd = 1; cd <= l; cd++){ cout << "* "; }cout << "\n";
	cout << "m "; for (cd = 1; cd <= m; cd++){ cout << "* "; }cout << "\n";
	cout << "n "; for (cd = 1; cd <= n; cd++){ cout << "* "; }cout << "\n";
	cout << "o "; for (cd = 1; cd <= o; cd++){ cout << "* "; }cout << "\n";
	cout << "p "; for (cd = 1; cd <= p; cd++){ cout << "* "; }cout << "\n";
	cout << "q "; for (cd = 1; cd <= q; cd++){ cout << "* "; }cout << "\n";
	cout << "r "; for (cd = 1; cd <= r; cd++){ cout << "* "; }cout << "\n";
	cout << "s "; for (cd = 1; cd <= s; cd++){ cout << "* "; }cout << "\n";
	cout << "t "; for (cd = 1; cd <= t; cd++){ cout << "* "; }cout << "\n";
	cout << "u "; for (cd = 1; cd <= u; cd++){ cout << "* "; }cout << "\n";
	cout << "v "; for (cd = 1; cd <= v; cd++){ cout << "* "; }cout << "\n";
	cout << "w "; for (cd = 1; cd <= w; cd++){ cout << "* "; }cout << "\n";
	cout << "x "; for (cd = 1; cd <= x; cd++){ cout << "* "; }cout << "\n";
	cout << "y "; for (cd = 1; cd <= y; cd++){ cout << "* "; }cout << "\n";
	cout << "z "; for (cd = 1; cd <= z; cd++){ cout << "* "; }cout << "\n";
}

int contarPalabras(char A[]){
	int k, es = 0, d;
	for (k = 0; A[k] != '\0'; k++)
	{
		if (A[k] == ' ') es++;
	}
	d = es + 1;
	return d;
}

int buscarPalabra(char A[], char P[]){
	int k, i, d, c, z = 0;
	for (k = 0; A[k] != '\0'; k++)
	{
		c = k;
	}
	for (i = 0; P[i] != '\0'; i++)
	{
		d = i;
	}
	k = 0;
	while (k < c){
		i = 0;
		while (i <= d){
			if (P[i] == A[k])
			{
				i++;
				k++;
			}
			else
				k++;
		}
		if (i = d + 1) z++;
		k++;
	}
	return z;
}

void palabrasSegunTamano(char Oracion[]){
	int n=0, Long[100], cont = 0, numPalabras = contarPalabras(Oracion), i = 0;
	
	string Ordenado[100], palabra;
	while (n != 101) Ordenado[n] = " ";

	n = 0;
	while (Oracion[n] != '\0'){
		if (Oracion[n] != ' '){
			palabra += Oracion[n];
			n++;
		}
		else{
			Ordenado[i] = palabra;
			i++;
			n++;
		}
	}
	i = 0;
	n = 0;

	while (numPalabras != cont){
		while (Ordenado[n] != " "){
			if (Ordenado[i].length() < Ordenado[n].length())
				n++;
			else i = n;
		}
		cout << Ordenado[i];
		n = 0;
		while (n != numPalabras)


		cont++;
	}
}