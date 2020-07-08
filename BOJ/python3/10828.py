
# 10828 15:01 - 12 (11m)
import sys


def push(arr, num):
    arr.append(int(num))


def pop(arr):
    length = len(arr)
    if length > 0:
        print(arr[length-1])
        del arr[length-1]
    else:
        print('-1')


def size(arr):
    print(len(arr))


def empty(arr):
    if len(arr) > 0:
        print('0')
    else:
        print('1')


def top(arr):
    if len(arr) > 0:
        print(arr[len(arr)-1])
    else:
        print('-1')


N = int(sys.stdin.readline())
inp = []

for _ in range(N):
    x = list(sys.stdin.readline().split())

    if x[0] == 'push':
        push(inp, x[1])
    elif x[0] == 'pop':
        pop(inp)
    elif x[0] == 'size':
        size(inp)
    elif x[0] == 'empty':
        empty(inp)
    elif x[0] == 'top':
        top(inp)
