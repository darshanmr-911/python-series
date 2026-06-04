from os import path
from sys import maxsize
from itertools import permutations
V=4
s=0
vertex=[]
def tsp(graph,s):
    for i in range(V):
        if i!=s:
            vertex.append(i)
    min_size=maxsize
    perm=permutations(vertex)
    for i in perm:
        k=s
        path_cost=0
        for j in i:
            path_cost+=graph[k][j]
            k=j
        path_cost+=graph[k][s]
        min_size=min(min_size,path_cost)
    return min_size
if __name__ == "__main__":
    graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    print(tsp(graph,s))
