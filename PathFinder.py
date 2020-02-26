"""
This project implements the A* Algorithm to find the shortest path between two nodes
in an N x N grid. Boards on the node can be closed, preventing the path from using 
that node. 

Classes:
	board: This class implements a N x N board by creating a list of lists containing 
	       node objects. It takes in a tuple containing the coordinates of the
	       start and end nodes.  
	node: This class allows for the creation of node objects, which are selected by
		  the path-finding algorithm. Nodes can either be the start, end, open, or 
		  closed. 
"""

class Board:
	def __init__(self, size, start, end)
		self.size = size
		self.start = start
		self.end = end
		self.board = []

		for x in range(N): 
			self.board.extend([])

		for i in range(N):
			for j in range(N):
				if i == start(0) and j == start(1):
					self.board[i][j] = Node.__init__(False, True, False, i, j)
				elif i == end(0) and j == end(1):
					self.board[i][j] = Node.__init__(False, False, True, i, j)
				else
					self.board[i][j] = Node.__init__(False, False, False, i, j)

	def close(self, x, y)
		self.board[x][y].isOpen = False



class Node: 
	def __init__(self, isOpen, isStart, isEnd, x, y)
		self.isOpen = isOpen
		self.isStart = isStart
		self.isEnd = isEnd

