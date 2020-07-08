text = ['   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ']

inp = []

for i in text:
    noBlank = i.strip().replace(' ', '').replace('+', '1').replace('-', '0')
    # strip() : 양 끝의 공백 제거.
    inp.append(chr(int(noBlank, 2)))  # 2진법인 noBlank 를 10진법으로 바꿈.

print(''.join(inp))  # 리스트의 모든 원소를 한 줄로 출력.

# list comprehension (1)
print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))

# list comprehension (2)
# f :
# 앞에 있는 for 문 = 한 줄에 하나씩 썼다면 더 위에 있는 for 문
print([f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)])

# zfill : 자리수 맞춰주는 func
print('111'.zfill(10))

# lambda : 한 줄 함수
s = [i.strip().replace(' ', '').replace('+', '1').replace('-', '0') for i in text]
print(list(map(lambda x: chr(int(x, 2)), s)))

# zip : 두 개의 List를 하나의 연관된 리스트로 만들어 주는 것
Number = [1, 2, 3, 4]
Name = ['hong', 'gil', 'dong', 'nim']
dic = {}
for number, name in zip(Number, Name):
    dic[number] = name
print(dic)
'''
결과 : {1 : 'hong' , 2 : 'gil' , 3 : 'dong' , 4 : 'nim'}
'''
