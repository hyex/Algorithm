# 문자열을 뒤집을 때는 [::-1]
# 숫자를 뒤집고 싶을때도, 문자열로 바꾸고 다시 숫자로 바꾸면 되겠

num1, num2 = input().split()

num1 = num1[::-1]
num2 = num2[::-1]

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(num1)
else:
    print(num2)

