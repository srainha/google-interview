class Graph(object):

# A basic directed graph class based on adjacency list

	def __init__(self):
		self.nodes = set()
		self.graph = {}

	def addNode(self, data):
		self.nodes.add(data)
		if (data not in self.graph):
			self.graph[data] = set()

	def addEdge(self, fromNode, toNode):
		self.nodes.add(fromNode)
		self.nodes.add(toNode)
		if (fromNode not in self.graph):
			self.graph[fromNode] = set()
		if (toNode not in self.graph):
			self.graph[toNode] = set()
		self.graph[fromNode].add(toNode)

	def deleteNode(self, data):
		self.nodes.remove(data)
		del self.graph[data]
		for key, value in self.graph.items():
			if data in value:
				value.remove(data)

	def deleteEdge(self, fromNode, toNode):
		if (fromNode in self.graph and toNode in self.graph):
			self.graph[fromNode].remove(toNode)

	def containsNode(self, data):
		return data in self.nodes

	def containsEdge(self, fromNode, toNode):
		return toNode in self.graph[fromNode]


class UdGraph(Graph):

	def addEdge(self, fromNode, toNode):
		super(UdGraph, self).addEdge(fromNode, toNode)
		self.graph[toNode].add(fromNode)

	def deleteEdge(Self, fromNode, toNode):
		super(UdGraph, self).deleteEdge(fromNode, toNode)
		self.graph[toNode].remove(fromNode)
