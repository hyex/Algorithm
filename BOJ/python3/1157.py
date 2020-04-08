# 문제는 쉬운데, ASCII 문제는 항상 함수가 

word = input()
word = list(word.upper())
alphabet = [0 for _ in range(26)]

for i in range(len(word)):
    test = ord(word[i]) - ord("A")
    alphabet[test] += 1

maxValue = max(alphabet)
maxIndex = ""

for i in range(len(alphabet)):
    if alphabet[i] == maxValue:
        if maxIndex == "":
            maxIndex = chr(i + ord('A'))
        else:
            maxIndex = "?"
            break

print(maxIndex)

