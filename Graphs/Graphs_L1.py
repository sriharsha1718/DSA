#Adjacency Matrix and Adjacency Lists

############################################
#Representation of Graph in Adjacency Matrix
ipt = [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
#N must be 6 for this input
N = int(input("Enter no of nodes in the graph:"))
adj_matrix = []
for i in range(N):
    temp_list = []
    for j in range(N):
        temp_list.append(0)
    adj_matrix.append(temp_list)
print("The initialised adjacency matrix is:")
for item in adj_matrix:
    print(item)

#Altering the initialised matrix with given input
for (u,v) in ipt:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1
    
print("\nThe Final adjacency matrix is:")
for item in adj_matrix:
    print(item) 

##########################################
#Representation of Graph in Adjacency List
adj_list = {}
for i in range(N):
    adj_list[i] = []

print("\nThe initialised adjacency list is:")
for item in adj_list.items():
    print(item)

for (u,v) in ipt:
    adj_list[u].append(v)
    adj_list[v].append(u)

print("\nThe final adjacency list is:")
for item in adj_list.items():
    print(item)



##########################################
#Output
'''
Enter no of nodes in the graph:6
The initialised adjacency matrix is:
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]

The Final adjacency matrix is:
[0, 1, 1, 1, 1, 0]
[1, 0, 0, 1, 0, 0]
[1, 0, 0, 1, 1, 1]
[1, 1, 1, 0, 0, 1]
[1, 0, 1, 0, 0, 0]
[0, 0, 1, 1, 0, 0]

The initialised adjacency list is:
(0, [])
(1, [])
(2, [])
(3, [])
(4, [])
(5, [])

The final adjacency list is:
(0, [1, 2, 3, 4])
(1, [0, 3])
(2, [0, 3, 4, 5])
(3, [0, 1, 2, 5])
(4, [0, 2])
(5, [2, 3])
'''
