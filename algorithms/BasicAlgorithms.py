# from dataStructures.trees.Tree import *

# ========= Miscallaneous =========

def fizzBuzz(n):
	print('Starting fizz buzz')
	for i in range(1, n+1):
		if (i % 3 == 0 and i % 5 == 0):
			print ('fizz buzz')
		elif (i % 3 == 0):
			print('fizz')
		elif (i % 5 == 0):
			print('buzz')
		else:
			print(i)

def isPermutationString(aString, bString):
	if (len(aString) != len(bString)):
		return False
	aDict = {}
	bDict = {}
	for c in range(len(aString)):
		if (aString[c] in aDict): 
			aDict[aString[c]] += 1
		else:
			aDict[aString[c]] = 1
		if (bString[c] in bDict):
			bDict[bString[c]] += 1
		else:
			bDict[bString[c]] = 1 
	return aDict == bDict

def isPalindromeString(a, b):
	if (len(a) != len(b)):
		return False
	for i in range(len(a)):
		if (a[i] != b[-i -1]):
			return False
	return True

def windowAverages(arr, windowSize):
	pass

def fibonacci(n):
	pass

# ========= Searching and Sorting =========

def linearSearch(arr, val):
	for a in range(len(arr)):
		if (arr[a] == val):
			return a
	return -1

def binarySearchIt(arr, val):
	low = 0
	high = len(arr) - 1
	while (low <= high):
		mid = low + ((high - low) // 2)
		midValue = arr[mid]
		if (val == midValue):
			return mid
		elif (midValue < val):
			low = mid + 1
		else:
			high = mid - 1
	return -1

def quickSort(arr):
	less = []
	equal = []
	greater = []

	if (len(arr) <= 1): return arr
	pivot = arr[0]
	for x in arr:
		if x < pivot:
			less.append(x)
		elif pivot < x:
			greater.append(x)
		else:
			equal.append(x)
	return quickSort(less) + equal + quickSort(greater)


# top down
# average=O(nlogn)
def mergeSort(arr):
	if (len(arr) <= 1):
		return arr
	left = arr[:int(len(arr)/2)]
	right = arr[int(len(arr)/2):]
	left = mergeSort(left)
	right = mergeSort(right)
	return merge(left, right)

def merge(left, right):
	result = []
	while (left != [] and right != []):
		if (left[0] < right[0]):
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while (left != []):
		result.append(left.pop(0))
	while (right != []):
		result.append(right.pop(0))
	return result

# ========= Tree Operations =========

def preOrder(treeNode):
	# Root, left, right
	if (treeNode is not None):
		print(treeNode.data)
	else:
		return
	preOrder(treeNode.left)
	preOrder(treeNode.right)


def postOrder(treeNode):
	# Left, right, root
	if (treeNode is None):
		return
	else:
		postOrder(treeNode.left)
		postOrder(treeNode.right)
		print(treeNode.data)

def inOrder(treeNode):
	# Left, root, right
	if (treeNode is None):
		return
	else:
		inOrder(treeNode.left)
		print(treeNode.data)
		inOrder(treeNode.right)

def levelOrder(treeNode):
	unexplored = [tree.root]
	while (unexplored != []):
		node = unexplored.pop(0)
		print(node.data)
		if (node.left is not None):
			unexplored.append(node.left)
		if (node.right is not None):
			unexplored.append(node.right)

def bfsIt(tree, val):
	unexplored = [tree.root]
	while (unexplored != []):
		node = unexplored.pop(0)
		print('BFS at: ' + str(node.data))
		if (node.data == val):
			print ('BFS found value: ' + str(val))
			return node
		if (node.left is not None):
			unexplored.append(node.left)
		if (node.right is not None):
			unexplored.append(node.right)

def bfsRec(treeNode, val):
	# Not useful or easy, but maybe a fun exercise 
	pass

def dfsIt(tree, val):
	unexplored = [tree.root]
	while (unexplored != []):
		node = unexplored.pop(-1)
		print('DFS-It at: ' + str(node.data))
		if (node.data == val):
			print ('DFS-It found value: ' + str(val))
			return node
		if (node.left is not None):
			unexplored.append(node.left)
		if (node.right is not None):
			unexplored.append(node.right)

def dfsRec(treeNode, val):
	print('DFS at: ' + str(treeNode.data))
	if (treeNode.data == val):
		print('DFS found value: ' + str(val))
		return treeNode
	if (treeNode.left is not None):
		node = dfsRec(treeNode.left, val)
		if (node is not None):
			return node
	if (treeNode.right is not None):
		node = dfsRec(treeNode.right, val)
		if (node is not None):
			return node
	return None
