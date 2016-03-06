#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	vector<int> v;
	cout << "Insert the values to sort (To finish CTRL + D):\n";
	int x;
	while (cin >> x) {
		v.push_back(x);
	}
	sort(v.begin(), v.end());
	cout << "Sorted vector: ";
	for (int i=0; i<v.size(); i++){
		cout << v[i] << " ";
	}
	cout << endl;
}