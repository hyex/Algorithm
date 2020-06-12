inp = input()

lines = len(inp)

for line in range(0, lines, 10):
    print(inp[line: line+10])

if len(inp) > lines*10:
    print(inp[lines*10:])
