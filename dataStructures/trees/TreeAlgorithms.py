from Tree import *


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


def lowest_common_ancestor(treeNode, node_1, node_2):
    if (treeNode is None):
        return None
    if (treeNode.data < node_1.data and treeNode.data < node_2.data):
        return lowest_common_ancestor(tree_node.right, node_1, node_2)
    elif (node_1.data < tree_node.data and node_2 < treeNode.data):
        return lowest_common_ancestor(tree_node.left, node_1, node_2)
    else:
        return treeNode
