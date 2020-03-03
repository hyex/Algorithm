"""
문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
"""

a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
# python은 나눌 때 int형이더라도 나머지가 발생하면 float형으로 출력한다. 따라서 int형으로 변환을 하던가, // 을 사용해야한다.
print(a//b)
print(a%b)
