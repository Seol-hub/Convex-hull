import sys
from math import sqrt

def CCW(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

# 입력받은 배열을 정렬해서 가장 왼쪽 아래에 있는 점을 기준점으로 함
N = int(sys.stdin.readline())
A = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
A.sort() # 기준점 : A[0]

# 점들마다 기준점과의 기울기, 거리를 계산해서 기울기가 작으면서 가까운 점들 순서가 되도록 정렬
inclines = []
for i in range(1, N):
    if A[i][1] == A[0][1]: 
        incline = 0
    elif A[i][0] == A[0][0]:
        incline = float('inf')
    else: 
        incline = (A[i][1] - A[0][1])/(A[i][0] - A[0][0])

    distance = sqrt((A[i][0] - A[0][0])**2 + (A[i][1] - A[0][1])**2)
    inclines.append((incline, distance, i))

inclines.sort()

stack = [0] # 초기값은 기준점
for i in range(len(inclines)):
    v = inclines[i][2]
    while len(stack) > 1:
        a, b = stack[-1], stack[-2]
        x1, y1, x2, y2, x3, y3 = A[b][0], A[b][1], A[a][0], A[a][1], A[v][0], A[v][1]
        res = CCW(x1, y1, x2, y2, x3, y3)
        if res > 0:
            break
        else:
            stack.pop()
    stack.append(v)

print(len(stack))