
// BOJ 1463
// 참고 https://blockdmask.tistory.com/254

#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    
    // 문제에서 N의 범위가 100000 까지
    int dp[1000001]{0};
    int N;
    cin >> N;
    
    dp[1] = 0; // 1일 때는 0번
    
    // bottom up
    // 규칙3번(1을 뺀다) 가 가장 작은 연산으로 가장 큰 값을 저장할 것이므로 규칙 3번 -> 2번 -> 1번 순으로 계산, 비교
    for(int i = 2; i <= N ; i++){
        dp[i] = dp[i-1] + 1; // 규칙 3번, 연산을 한 번 더 하니까 +1
        if (i % 2 == 0)
            dp[i] = min(dp[i], dp[i/2] + 1); // 규칙 2번
        if (i % 3 == 0)
            dp[i] = min(dp[i], dp[i/3] + 1); // 규척 1번
    }
    
    cout << dp[N];

    return 0;
}
