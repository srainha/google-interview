class LinkedListNode():

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = None
		self.last = None

	def addToFront(self, data):
		if (self.head is None):
			self.head = LinkedListNode(data)
			self.last = self.head
		else:
			tempNode = LinkedListNode(data)
			tempNode.next = self.head
			self.head = tempNode

	def addToTail(self, data):
		if (self.head is None):
			self.head = LinkedListNode(data)
		else:
			pass

	def delete(self, data):
		if (self.head.data == data):
			self.head = self.head.next
		else:
			self._

	def contains(self, data):
		pass

	def index(self, data):
		pass


class DubLinkedListNode():

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DubLinkedList():
	def __init__

	def add(self, data):
		pass

	def delete(self, data):
		pass

	def contains(self, data):
		pass

	def index(self, data):
		pass

