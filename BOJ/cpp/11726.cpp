// BOJ 11726

#include <iostream>
using namespace std;

int main(){
    
    int tile[1001]{0};
    int N;
    cin >> N;
    
    tile[0] = 1;
    tile[1] = 1;
    for (int i = 2 ; i <= N ; i++){
        tile[i] = (tile[i-2] + tile[i-1])% 10007; // 포인트 : 연산 중에 값을 나눠줘야 자료형의 크기를 넘지 않음.
    }
    cout << tile[N]  << endl ;

    return 0;
}
