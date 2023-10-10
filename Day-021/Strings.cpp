#include <iostream>
#include <string>
using namespace std;

int main() {
	string a,b;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    cout<< a + b << endl;
    string temp = a;
    a[0] = b[0];
    b[0] = temp[0];
    cout<< a << " " << b;
    return 0;
}
