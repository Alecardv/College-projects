#include <cstdlib>
#include <iostream>

//Realizar un programa que muestre los numeros primos comprendidos entre 100 y 300

using namespace std;

int main(int argc, char *argv[])
{
	int num = 100, i, a;

	while (num <= 300)
	{
		a = 0;
		for (i = 1; i <= num; i++)
		{
			if (num%i == 0)	a++;
		}

		if (a == 2){
			cout << num << " es primo" << endl;
			num++;
		}
		else{
			num++;
		}
	}

	system("PAUSE");
}