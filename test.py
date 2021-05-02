from collections import deque
import sys
input = sys.stdin.readline


INF = sys.maxsize
W = int(input())
C, R = [int(x) for x in input().split(' ')]
arr = [None for _ in range(R)]
memo = [[[INF for _ in range(W + 1)] for _ in range(C)] for _ in range(R)]
dists = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dists2 = [(1, 2), (1, -2), (-1, 2), (-1, -2),
          (2, 1), (2, -1), (-2, 1), (-2, -1)]
result = INF


def init():
    for r in range(R):
        arr[r] = [int(x) for x in input().split(' ')]


def logic():
    q = deque()
    q.append((0, 0, 0))
    memo[0][0][0] = 0
    while q:
        tr, tc, tw = q.popleft()
        if tr == R - 1 and tc == C - 1:
            break
        for dr, dc in dists:
            nr, nc, nw = tr + dr, tc + dc, tw
            if 0 <= nr <= R - 1 and\
                    0 <= nc <= C - 1 and\
                    arr[nr][nc] != 1 and\
                    memo[nr][nc][nw] == INF:
                memo[nr][nc][nw] = memo[tr][tc][tw] + 1
                q.append((nr, nc, nw))
        if tw + 1 <= W:
            for dr, dc in dists2:
                nr, nc, nw = tr + dr, tc + dc, tw + 1
                if 0 <= nr <= R - 1 and\
                        0 <= nc <= C - 1 and\
                        arr[nr][nc] != 1 and\
                        memo[nr][nc][nw] == INF:
                    memo[nr][nc][nw] = memo[tr][tc][tw] + 1
                    q.append((nr, nc, nw))


def output():
    global result
    for w in range(W + 1):
        result = result if result < memo[R - 1][C - 1][w] else memo[R - 1][C - 1][w]
    if result == INF:
        result = -1
    print(result)


init()
logic()
output()
