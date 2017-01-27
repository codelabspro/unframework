class Unbase:
	level = 0
	background = 'purple'
	points = 10

	def __init__(self, level = 1, background = 'green', points = 9):
		self.level = level
		self.background = background
		self.points = points

	def setup(self):
		return self.background