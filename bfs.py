import collections

class SimpleGraph:
	def __init__(self):
		self.edges = {}
	def neighbors(self,id):
		print("HERE")
		return self.edges[id]

class Queue:
	def __init__(self):
		self.elements = collections.deque()
	def empty(self):
		return len(self.elements)==0
	def put(self,n):
		self.elements.append(n)
	def get(self):
		self.elements.pop()

graph = SimpleGraph()
graph.edges = {
				1:[2],
				2:[1,3,4],
				3:[1],
				4:[1,5],
				5:[2]
			}






