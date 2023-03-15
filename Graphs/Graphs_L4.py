#Single Source Shortest Path
edges = [['A','B'],['A','C'],['B','D'],['D','G'],['G','H'],['G','I'],['C','E'],['C','F']]
nodes = ['A','B','C','D','E','F','G','H','I']

#Single Source Shortest Path Function.
def sssP(graph,node,d,distance,parent):
    distance[node]=d
    for child in graph[node]:
        if child != parent:
            sssP(graph,child,distance[node]+1,distance,node)
    

#Adjacency List representation of graph
graph = {}
distance = {}
for key in nodes:
    graph[key] = []
    distance[key] = None

for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)
    
print("Adjacency List representation of graph:")
for item in graph.items():
    print(item)

start = 'A'
print("\nThe Source node is {}.".format(start))
distance[start] = 0
sssP(graph,start,0,distance,-1)

print("\nThe distance of each node from source node is:")
for item in distance.items():
    print(item)


############################################
#Output
'''
Adjacency List representation of graph:
('A', ['B', 'C'])
('B', ['A', 'D'])
('C', ['A', 'E', 'F'])
('D', ['B', 'G'])
('E', ['C'])
('F', ['C'])
('G', ['D', 'H', 'I'])
('H', ['G'])
('I', ['G'])

The Source node is A.

The distance of each node from source node is:
('A', 0)
('B', 1)
('C', 1)
('D', 2)
('E', 2)
('F', 2)
('G', 3)
('H', 4)
('I', 4)
'''

