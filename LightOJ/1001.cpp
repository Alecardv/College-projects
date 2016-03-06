#include <iostream>

using namespace std;

int main() {
	int n,a,b;
	int i = 1;
	
	cin >> n;
	while (i <= n) {
		cin >> a;
		cout << a/2 << " " << a-(a/2) << endl;
		i++;
	}
	return 0;
}
