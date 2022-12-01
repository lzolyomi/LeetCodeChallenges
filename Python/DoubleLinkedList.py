
def special_list( values, print_backwards ) :
	####### DO NOT MODIFY BELOW #######
	d = MySpecialList()

	for value in values:
		d.append(value)
	return d.print_backwards() if print_backwards else d.print_forward()
	####### DO NOT MODIFY ABOVE #######

class Node():
		def __init__(self, data, prev, next):
			self.data = data
			self.prev = prev
			self.next = next


class MySpecialList():
	def __init__(self):
		self.head = None # head of linked list 
		self.tail = None
	def append(self, data):
		if not self.head: # if first element
			self.head = Node(data, None, None)
			self.tail = self.head
		else: # if there is an element already
			newElem = Node(data, self.tail, None)
			self.tail.next = newElem
			self.tail = newElem
                

	def print_forward(self):
		nextElem = self.head
		print(self.head.data)
		retList = []
		while nextElem.next: #until there is a next element
			retList.append(nextElem.data)
			nextElem = nextElem.next
		return retList

	def print_backwards(self):
		nextElem = self.tail
		retList = []
		while nextElem.prev: #until there is a next element
			retList.append(nextElem.data)
			nextElem = nextElem.prev
		return retList

if __name__ == "__main__":
	test = [1,2,3,4]

	print(special_list(test, False))