class LinkedListNode():

	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = LinkedListNode()
		self.tail = self.head

	def add(self, data):
		self.addToTail(data)

	def addToFront(self, data):
		if (self.head.data is None):
			self.head = LinkedListNode(data)
			self.tail = self.head
		else:
			tempNode = LinkedListNode(data)
			tempNode.next = self.head
			self.head = tempNode

	def addToTail(self, data):
		if (self.head.data is None):
			self.head = LinkedListNode(data)
			self.tail = self.head
		else:
			self.tail.next = LinkedListNode(data)
			self.tail = self.tail.next

	def delete(self, data):
		if (self.head.data == data):
			self.head = self.head.next
		else:
			self._delete(data, self.head)

	def _delete(self, data, node):
		while (node.next is not None):
			if (node.next.data == data):
				node.next = node.next.next
				return
			else:
				node = node.next

	def contains(self, data):
		node = self.head
		while (node.next is not None):
			if (node.data == data):
				return True
			else:
				node = node.next
		if (node.data == data):
			return True
		return False

	def index(self, data):
		pass


class DubLinkedListNode():

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DubLinkedList():
	def __init__(self):
		pass

	def add(self, data):
		pass

	def delete(self, data):
		pass

	def contains(self, data):
		pass

	def index(self, data):
		pass

