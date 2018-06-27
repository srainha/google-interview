from LinkedList import *

def findCenter(linkedList):
	node = linkedList.head
	if (head is None):
		return head
	slow = node
	fast = node.next
	while(fast is not None and fast.next is not None):
		slow = slow.next
		fast = fast.next.next
	return slow