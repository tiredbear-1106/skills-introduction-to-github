#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout.precision(2);
    cout << fixed << (double)(a+b)/(a-b);
    return 0;
}