from copy import copy
m,n,h = map(int,input().split())
g = []
q = set()
time =0
swap_q = set()
tomatoes = 0
for i in range(h):
    lst = []
    for j in range(n):
        a = list(map(int,input().split()))
        lst.append(a)
        for k in range(m):
            if a[k] == 1:
                q.add((k,j,i))
            if a[k] == 0:
                tomatoes += 1
    g.append(lst)
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dz = [1,-1]
while q:
    for (x,y,z) in q:
        for i in range(2):
            nz = z+dz[i]
            if not (0<=nz<h):
                continue
            if g[nz][y][x] == 0:
                g[nz][y][x] = 1
                swap_q.add((x,y,nz))
                tomatoes -= 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not (0<= nx < m and 0 <= ny < n):
                continue
            if g[z][ny][nx] == 0:
                g[z][ny][nx] = 1
                swap_q.add((nx,ny,z))
                tomatoes -= 1
    if swap_q:
        time += 1
    q = copy(swap_q)
    swap_q = set()
if tomatoes == 0:
    print(time)
else:
    print(-1)

