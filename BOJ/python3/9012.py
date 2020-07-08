# 9012

T = int(input())

for _ in range(T):
    cnt = 0
    answer = "YES"
    inp = list(input())

    for i in range(len(inp)):
        if inp[i] == '(':
            cnt += 1
        elif inp[i] == ')':
            if cnt > 0:
                cnt -= 1
            else:
                answer = "NO"
                break
        # print(inp[i], cnt)
    if cnt != 0:
        answer = "NO"
    print(answer)
