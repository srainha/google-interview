import re

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

def reverseString(s):
	pass

def reverseSentence(s):
	pass

def reverseSentenceCasing(s):
	pass

def capSentence(s):
	pass

def allPermutations(s):
	pass

def regexDecimal(line):
	pattern = '^[+-]?(([0-9]+)|([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+))([Ee][+-]?[0-9]+)?$'
	return (re.match(pattern, line) is not None)

def regexURL(line):
	pass
