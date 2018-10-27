"""
Author: Enes Uysal
28.10.2018
"""
class tree(object):
	def __init__(self, ch, freq, right=None, left=None):
		super(tree, self).__init__()
		self.ch = ch
		self.freq = freq
		self.right = right
		self.left = left
		
bl = []
freq = []
head = None

def swap(i1, i2):
	tmp = bl[i1]
	bl[i1] = bl[i2]
	bl[i2] = tmp

	tmp = freq[i1]
	freq[i1] = freq[i2]
	freq[i2] = tmp



def sort():
	for i, x in enumerate(freq):
		for y in range(i, len(freq)):
			if(x>freq[y]):
				swap(i, y)


def getIndex(ch, arr):
	for i, x in enumerate(arr):
		if(x==ch):
			return i
	return -1

def count(str):
	global bl, freq
	for x in str:
		if(x not in bl):
			bl.append(x)
			freq.append(1)
		else:
			index = getIndex(x, bl)
			freq[index] += 1

	sort()

def printTree(head, sayac):
	if(len(head.ch)>1):
		tmp = sayac[:]
		sayac.append("0")
		printTree(head.left, sayac)
		tmp.append("1")
		printTree(head.right, tmp)

	if(len(head.ch)==1):
		print head.ch+": ",
		for x in sayac:
			print x,
		print "\n",


def createNode():
	global bl
	global freq
	tmp = []
	tmp2 = []
	if(len(bl)>1):
		for x in range(2):
			if(type(bl[x])==tree):
				tmp.append(bl[x].ch)
				tmp2.append(bl[x].freq)

			else:
				tmp.append(bl[x])
				tmp2.append(freq[x])

	if(type(bl[0])!=tree):
		new = tree(tmp[0], tmp2[0])
	else:
		new = bl[0]
	
	if(type(bl[1])!=tree):
		new2 = tree(tmp[1], tmp2[1])
	else:
		new2 = bl[1]
	
	node = tree(tmp[0]+tmp[1], tmp2[0]+tmp2[1], new, new2)
	
	del bl[0]
	del freq[0]
	del bl[0]
	del freq[0]


	bl.append(node)
	freq.append(node.freq)

	sort()


text = raw_input("Please enter a text: ")

count(str(text))

while len(bl)>1:
	createNode()

sayac = []

printTree(bl[0], sayac)

 
