'''
미로 탈출
입력 예시 => 벽 : 0 / 길 : 1
5 6
101010
111111
000001
111111
111111

출력 : 10
'''
from collections import deque

# 입력 처리
n,m = map(int, input().split())
maps = [ list(map(int, input())) for _ in range(n) ]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x,y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if maps[nx][ny] == 0 :
                continue

            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))

    return maps[n-1][m-1]

print(bfs(0,0))