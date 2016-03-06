#include <iostream>

using namespace std;

int main() {
	int n, a, b;
	int i = 1;

	cin >> n;
	while (i <= n) {
		cin >> a;
		cin >> b;
		cout << "Case " << i << ": " << a+b << endl;
		i++;
	}
	return 0;
}
