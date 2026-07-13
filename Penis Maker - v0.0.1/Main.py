class Penis:
	#If length is 0, Draw Beautiful
	_OFFSET = 1
	_BLOCK_LIST = ["", " "]
	
	def __init__(self, length: int = 10, letter: str = "#"):
		#Letter check
		if letter.strip() in self._BLOCK_LIST or len(letter) > 1 or not letter.isprintable():
			raise ValueError("Your symbol is incorrect")
		self.letter = letter
		
		#Negative Length Check
		if length < 0:
			raise ValueError("Length cannot be negative")
		self.length = length
			
	def _draw(self):
		#Penis Art
		return f"{self.letter}\n{self.letter * (self.length + self._OFFSET)}\n{self.letter}"
	
	def __str__(self):
		return f"{self._draw()}\n\n{self.length} cm"
		
#Guide
my_dick = Penis()
print(my_dick)
