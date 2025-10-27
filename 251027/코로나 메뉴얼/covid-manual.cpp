#include <iostream>
using namespace std;

int main() {
    int count = 0;
    for (int i = 0; i<3; i++) {
        char a;
        int n;
        cin >> a >> n;
        if ((a == 'Y') && (n>=37)) count++;
    }
    cout << (count>=2 ? 'E' : 'N');
    return 0;
}