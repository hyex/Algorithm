#include <iostream>
using namespace std;

int main(){
    int A, B;
    while(cin >> A >> B){ // 입력이 없을 때 끝나도록.
        if (A < 1 || B > 9) return -1;
        cout << A+B << endl;
    }
    return 0;
}
