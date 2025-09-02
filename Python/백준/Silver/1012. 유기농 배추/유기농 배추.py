from collections import deque

T = int(input())

dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for tc in range(T):
    M, N, K = map(int, input().split())
    bc_pos = list(tuple(map(int, input().split())) for _ in range(K))
    total_bunch = 0

    while bc_pos :

        deq = deque()
        deq.append(bc_pos[0])

        while deq:
            x, y = deq.popleft()
            bc_pos.remove((x, y))   # 방문 체크 겸 제거

            # 4방향 돌면서 옆에 배추가 있는지 확인
            for dy, dx in dyx:
                ny, nx = y+dy, x+dx

                # 범위를 벗어난 경우 다음 방향
                if not (0 <= ny < N and 0 <= nx < M): continue

                # 배추가 없거나 이미 방문한 위치라면 넘어가기
                if (nx, ny) not in bc_pos: continue

                # 배추가 있는 경우 큐에 넣기
                if (nx, ny) in bc_pos:
                    # 큐에 있는지 한번 더 검사
                    if (nx, ny) not in deq:
                        deq.append((nx, ny))
        total_bunch += 1


    print(total_bunch)