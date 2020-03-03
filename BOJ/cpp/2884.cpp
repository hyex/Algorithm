#include <iostream>
using namespace std;

/*
입력한 시간, 분보다 45분 빠른 시간을 출력한다.
첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
그리고 이것은 현재 상근이가 맞춰놓은 알람 시간 H시 M분을 의미한다.
24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.
시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
출력
첫째 줄에 상근이가 창영이의 방법을 사용할 때, 맞춰야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)
*/

// 문제가 쉬워서 여러 가지 풀이가 있겠지만 가장 효율적인 풀이 방법이 무엇인지 궁금

int main() {
    int hour, minute;
    cin >> hour >> minute;
    
    if (minute < 45){
        if (hour == 0) hour = 23;
        else hour = hour - 1;
        minute = minute + 15; // + 60 - 45
    } else {
        minute = minute - 45;
    }
    cout << hour << " " << minute << endl;
}
