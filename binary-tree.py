import random

class BinaryTree:
	root = None

	class Node:

		def __init__(self, data, left=None, right=None):
			self.data = data
			self.left = left
			self.right = right

	def search_node(self, data, node):
		if data == node.data:
			return "node is existing"
		elif data > node.data:
			if node.right:
				self.search_node(data, node.right)
			else:
				node.right = self.Node(data)
		elif data < node.data:
			if node.left:
				self.search_node(data, node.left)
			else:
				node.left = self.Node(data)

	def add(self, data):
		if self.root:
			self.search_node(data, self.root)
		else:
			self.root = self.Node(data)

	def out(self):
		nodes, height = [self.root], 100
		while nodes:
			for node in nodes:
				if node:
					if node == "S":
						print(end=" ")
					else:
						print(" "*height, node.data, end=" "*height)
				else:
					print(" "*height, "N", end=" "*height)
			print("\n")
			for elt in range(0, len(nodes)):
				node = nodes.pop(0)
				if node:
					if node == "S":
						nodes.append("S")
						nodes.append("S")
						if len(nodes) == nodes.count(nodes[0]):
							nodes = []
							break
					else:
						nodes.append(node.left)
						nodes.append(node.right)
				else:
					nodes.append("S")
					nodes.append("S")
			height //= 2

def main():
	tree = BinaryTree()
	add_elt = [20, 12, 15, 8, 23, 45, 24, 61, 32, 4, 1, 0, 43, 38, 9, 7, 18, 99, 69]
	if add_elt:
		for elt in add_elt:
			tree.add(elt)
	else:
		add_elt = [random.randint(10, 100) for elt in range(0, 101)]
		for elt in add_elt:
			tree.add(elt)
	tree.out()

if __name__ == "__main__":
	main()