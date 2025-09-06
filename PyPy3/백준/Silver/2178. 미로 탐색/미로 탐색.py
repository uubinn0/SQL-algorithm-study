import sys
from collections import deque

dyx = [(-1,0), (0,1), (1,0), (0,-1)]


def search(iy,ix,c,b_list):
    deq = deque()
    deq.append((iy,ix, c+1))
    b_list[iy][ix] = 0  # 방문 처리

    while deq:
        y, x, m_cnt = deq.popleft()

        # 도착지인지 확인
        if y == N-1 and x == M-1:
            return m_cnt

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            # 범위 체크
            if not (0<= ny < N and 0 <= nx < M): continue

            # 벽인지 체크
            if b_list[ny][nx] == 0: continue

            deq.append((ny, nx, m_cnt+1))
            b_list[ny][nx] = 0    # 방문 처리

    return -1


N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
cnt = 0
# print(board)

if board[0][0] == 0 :
    quit()
else:
    result = search(0,0,cnt, board)

print(result)