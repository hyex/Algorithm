n = int(input())
inp = []
result = []
for i in range(n):
    inp.append((list(input())))

for i in range(n):
    for j in range(n):
        if inp[i][j] == '1':
            neighborhood = [[i, j]]
            inp[i][j] = '0'
            count = 0
            while neighborhood:
                one, two = neighborhood.pop()
                # inp[one][two] = '0'
                # print(one, two, end=" & ")
                count += 1
                if one != 0 and inp[one-1][two] == '1': # up
                    neighborhood.append([one-1, two])
                    inp[one-1][two] = '0'
                if one != n-1 and inp[one+1][two] == '1': # down
                    neighborhood.append([one + 1, two])
                    inp[one + 1][two] = '0'
                if two != 0 and inp[one][two - 1] == '1': # left
                    neighborhood.append([one, two - 1])
                    inp[one][two - 1] = '0'
                if two != n-1 and inp[one][two + 1] == '1': # right
                    neighborhood.append([one, two + 1])
                    inp[one][two + 1] = '0'
            # print()
            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i)
