class LinkedListNode():
	# A basic unidirectional node

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
		else:

		if (self.next is None):
			self.next = LinkedListNode(data)
		else:
			self.next.add(data)

	def addToTail(self, data):
		if (self.head is None):
			self.head = LinkedListNode(data)
		else:
			pass

	def delete(self, data):
		pass

	def contains(self, data):
		pass

	def index(self, data):
		pass


class DubLinkedListNode():
	# A basic doubly linked node

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

