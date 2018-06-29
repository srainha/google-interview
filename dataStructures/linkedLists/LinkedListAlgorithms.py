from LinkedList import *

def findCenter(linkedList):
	node = linkedList.head
	if (node.data is None):
		return node
	slow = node
	fast = node.next
	while(fast is not None and fast.next is not None):
		slow = slow.next
		fast = fast.next.next
	return slow

def detectCycle(linkedList):
	node = linkedList.head
	if (node.data is None or node.next is None):
		return False
	slow = node
	fast = node.next
	while (fast is not None and fast.next is not None):
		slow = slow.next
		fast = fast.next.next
		if (fast == slow):
			return True
	return False

def reverse_linked_list(linked_list_node):
    front = linked_list_node
    prev_front = linked_list_node
    while (prev_front.next is not None):
        next_node = prev_front.next
        prev_front.next = next_node.next
        next_node.next = front  
        front = next_node
    return front
