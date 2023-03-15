##########################################
#Connected Components in Graph
edges = [['A','C'],['A','D'],['A','B'],['D','E'],['B','E'],['F','H'],['F','G'],['I','J']]
nodes = ['A','B','C','D','E','F','G','H','I','J','K']


##########################################
#DFS function to find connected components
def dfs(graph,node,visited):
    print(node,end=" ")
    visited.add(node)
    sm = 0
    for child in graph[node]:
        if child not in visited:
            sm+=dfs(graph,child,visited)
    return sm+1


###########################################
#Representation of given graph in adjacency list
graph = {}
for i in nodes:
    graph[i] = []

for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)

print("Adjacency list representation of given graph")
for item in graph.items():
    print(item)

visited = set()
c = 0
print("\nThe Connected components in the graph are:\n")
for i in nodes:
    if i not in visited:
        print("Connected Component {}:".format(c+1),end=" ")
        print("\nNo of nodes in connected component{}:".format(c+1),dfs(graph, i ,visited))
        c=c+1
        print()
print("\nTotal no of connected Components in the graph are: {}".format(c))




#######################################
#Output
'''
Adjacency list representation of given graph
('A', ['C', 'D', 'B'])
('B', ['A', 'E'])
('C', ['A'])
('D', ['A', 'E'])
('E', ['D', 'B'])
('F', ['H', 'G'])
('G', ['F'])
('H', ['F'])
('I', ['J'])
('J', ['I'])
('K', [])

The Connected components in the graph are:

Connected Component 1: A C D E B 
No of nodes in connected component1: 5

Connected Component 2: F H G 
No of nodes in connected component2: 3

Connected Component 3: I J 
No of nodes in connected component3: 2

Connected Component 4: K 
No of nodes in connected component4: 1


Total no of connected Components in the graph are: 4
'''
