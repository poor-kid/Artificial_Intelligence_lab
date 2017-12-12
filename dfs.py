
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start, goal):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex == goal:
            	return visited
            print(visited)
            for neighbor in graph[vertex]:
            	stack.append(neighbor)
            #stack.extend(graph[vertex] - visited)
    return visited

print(dfs(graph, 'A', 'D'))

def bfs(graph, start, goal):
    visited, queue = [], [start]
    path = []
    while queue:
        vertex = queue.pop(0)
        #print("o"+vertex)
        if vertex not in visited:
            visited.append(vertex)
            if vertex == goal:
            	break
            print(visited)
            for neighbor in graph[vertex]:
            	queue.append(neighbor)
            #queue.extend(graph[vertex] - visited)
            
            #print(queue.pop(0))
    return visited

print(bfs(graph, 'A', 'D'))
print("BFS :\n")
#print(bfs(graph,'A'))