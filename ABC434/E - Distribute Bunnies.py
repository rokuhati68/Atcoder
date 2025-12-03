from atcoder.maxflow import MFGraph
import sys
input = sys.stdin.readline
N = int(input())
s = set()
l = []

for i in range(N):
    x,r = map(int,input().split())
    s.add(x - r)
    s.add(x + r)
    l.append((x,r))

s = list(s)
_len = len(s)
graph = MFGraph(N + _len + 2)
start = N + _len
goal = start + 1

dic = {}
for i,value in enumerate(s):
    dic[value] = N + i
    graph.add_edge(N + i,goal,1)
    
for i in range(N):
    graph.add_edge(start,i,1)
    
for i in range(N):
    x,r = l[i]
    graph.add_edge(i,dic[x + r],1)
    graph.add_edge(i,dic[x - r],1)
    
    

max_flow = graph.flow(start,goal)
print(max_flow)