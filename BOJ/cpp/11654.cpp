#include <iostream>
using namespace std;
/*
문제
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
입력
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
출력
입력으로 주어진 글자의 아스키 코드 값을 출력한다.
*/

// 문자의 아스키코드 값을 알고싶다면 그냥 int로 변환하면 됨

int main() {
    char input;
    int inputInt;
    
    cin >> input;
    inputInt = (int)input;
    
    cout << inputInt << endl;
}
