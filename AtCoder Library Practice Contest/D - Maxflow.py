from atcoder.maxflow import MFGraph

N,M = map(int,input().split())
edge = [list(input())for _ in range(N)]

graph = MFGraph(N * M + 2)
S = N * M
T = N * M + 1

def index(i,j):
    return i * M + j

dxy = [(0,1),(1,0),(0,-1),(-1,0)]
for ny in range(N):
    for nx in range(M):
        if(ny + nx) % 2 == 0:
            for dx, dy in dxy:
                ty = ny + dy
                tx = nx + dx
                if 0 <= ty < N and 0 <= tx < M:
                    if edge[ny][nx] == "." and edge[ty][tx] == ".":
                        graph.add_edge(index(ny,nx),index(ty,tx),1)

        if (ny + nx) % 2 == 0 and edge[ny][nx] == ".":
            graph.add_edge(S,(index(ny,nx)),1)
        if (ny + nx) % 2 == 1 and edge[ny][nx] == ".":
            graph.add_edge((index(ny,nx)),T,1)

max_flow = graph.flow(S,T)
edges = graph.edges()
vector_dic = {
    (1, 0): 'v',
    (0, 1): '>',
    (-1, 0): '^',
    (0, -1): '<'
}
for ed in edges:
    flow = ed.flow
    start = ed.src
    goal = ed.dst
    if flow != 0 and start != S and goal != T:
        sy,sx = divmod(start,M)
        gy,gx = divmod(goal,M)
        edge[sy][sx] = vector_dic[(gy-sy),(gx - sx)]
        edge[gy][gx] = vector_dic[(sy-gy),(sx - gx)]
    
for i in edge:
    print("".join(i))