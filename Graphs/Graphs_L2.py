#Depth First Search (DFS) Traversal
def dfs(graph, node, visited=set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if len(visited)== N:
            break
        else:
            if child not in visited:
                dfs(graph,child,visited)


ipt = [[1,2],[1,5],[2,3],[2,4],[2,5],[3,4],[3,6],[4,5],[4,6],[5,6]]
#print(ipt)

graph = {}
N=6
for i in range(1,7):
    graph[i] = []

for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)

print("The adjacency list representation of Graph is:")
for item in graph.items():
    print(item)

print("\nDFS traversal of given graph is:")
dfs(graph, 1)


########################################
#Output
'''
The adjacency list representation of Graph is:
(1, [2, 5])
(2, [1, 3, 4, 5])
(3, [2, 4, 6])
(4, [2, 3, 5, 6])
(5, [1, 2, 4, 6])
(6, [3, 4, 5])

DFS traversal of given graph is:
1
2
3
4
5
6
'''
