#include <iostream>
using namespace std;

int main() {
    double a, b;
    char c;
    
    cin >> c >> a >> b;
    cout.precision(2);
    cout << c << endl;
    cout << fixed << a << endl << b;
    return 0;
}