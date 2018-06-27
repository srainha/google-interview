from LinkedList import *
from LinkedListAlgorithms import *

linkedList = LinkedList()
print(findCenter(linkedList).data, None)
linkedList.addToTail(1)
print(findCenter(linkedList).data, 1)
linkedList.addToTail(2)
print(findCenter(linkedList).data, 1)
linkedList.addToTail(3)
print(findCenter(linkedList).data, 2)
linkedList.addToTail(4)
linkedList.addToTail(5)
linkedList.addToTail(6)
linkedList.addToTail(7)
linkedList.addToTail(8)
print(findCenter(linkedList).data, 4)
linkedList.addToTail(9)
print(findCenter(linkedList).data, 5)

# 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9 > None

