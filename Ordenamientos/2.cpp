#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

void insSort(int *vector, int n)
{
	for (int i=1; i<n; i++){
		int j = i-1;
		int key = vector[i];
		while ( j >= 0 && vector[j]>key ) {
			vector[j+1] = vector[j];
			j--;
		}
		vector[j+1] = key;
	}
}

int main ()
{
	int n;
	cout << "Type the size of the vector: ";
	cin >> n;
	int* vector = new int[n];
	cout << "Insert all the values: ";
	for (int i = 0; i<n; i++){
		cin >> vector[i];
	}
	insSort(vector, n);
	cout << "Sorted values: ";
	for (int i=0; i<n; i++){
		cout << vector[i] << " ";
	}
	cout << endl;
	delete [] vector;
}