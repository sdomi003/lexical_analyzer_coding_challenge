sample = "C11111AA111BB111AA111111BB111111AA111BB111111AA11D"






class Interpret:
	def __init__(self):
		self.state = 1
		self.sample = "" 
		self.i = 0
		self.L1 = ""
		self.L2 = ""
		self.L3 = ""
		self.L4 = "" 	
		self.L1i = -1
		self.L2i = -1 
		self.L3i = -1
		self.L4i = -1
	def callState(self, fn):
		if (fn == 1):
			self.one()
		elif(fn == 2):
			self.two()
		elif(fn == 3):
			self.three()
		elif(fn == 4):
			self.four()
		elif(fn == 5):
			self.five()
		elif(fn == 6):
			self.six()
		elif(fn == 7):
			self.seven()
		else:
			self.eight()	
	def interpretString(self, sample):
		self.sample = sample	 
		while (self.i < len(self.sample)):
			self.callState(self.state)
			self.i += 1	

	def read_in(self):
		return self.sample[self.i], self.i

	def one(self):
		val, i = self.read_in()
		if (not val.isnumeric()):
			self.L1 = val
			self.L1i = i
			self.state = 2

	def two(self):
		val, i = self.read_in()
		if (val.isnumeric()):
			self.state = 1
			return
		else:
			self.state = 3
			self.L2 = val				
			self.L2i = i

	def three(self):
		val, i = self.read_in()
		if (val.isnumeric()):
			self.state = 4
			return
		else:
			self.L1 = self.L2
			self.L1i = self.L2i
			self.L2 = val		
			self.L2i = i


	def four(self):
		val, i = self.read_in()
		if (val.isnumeric()):
			self.state = 5
		else:
			self.state = 1
				

	def five(self):
		val, i = self.read_in()
		if (val.isnumeric()):
			self.state = 6
		else:
			self.state = 1
				
	def six(self):
		val, i = self.read_in()
		if (val.isnumeric()):
			self.state = 1
		else:
			self.state = 7
			self.L3 = val
			self.L3i = i


	def seven(self):
		val, i = self.read_in()
		if (val.isnumeric()):
			self.state = 1
		else:
			self.state = 8
			self.L4 = val
			self.L4i = i

	def eight(self):
		print("Letters ", self.L1, "and", self.L2)
		print("at positions", self.L1i, "and", self.L2i)
		print("match with letters ", self.L3, "and", self.L4)
		print("at positions", self.L3i, "and", self.L4i)
		print("\n\n")

		val, i = self.read_in()
		if (val.isnumeric()):
			self.state = 4
			self.L1 = self.L3
			self.L2 = self.L4
			self.L1i = self.L3i
			self.L2i = self.L4i
		else:
			self.L1 = self.L2
			self.L1i = self.L2i
			self.L2 = val
			self.L2i = i

	
			


interpreter = Interpret()
interpreter.interpretString(sample)





