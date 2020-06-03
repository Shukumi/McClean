class Room(object):
	def __init__(self,raumnr,desk,floor,trash,window): 
		self.raumnr = raumnr
		self.desk = desk
		self.floor = floor
		self.trash = trash
		self.window = window
		self.weight = 0
	def ausgabe(self):
		#print("Raumnummer:" + str(self.raumnr))
		print("Desk: " +str(self.desk))
		print("Floor: " + str(self.floor))
		print("Trash: " + str(self.trash))
		print("Window: " + str(self.window))
		print("Weight: " + str( self.weight))
	def calWeight(self):
		self.weight = 0
		if self.desk == False:
			self.weight +=1
		if self.floor == False:
			self.weight +=1
		if self.trash == False:
			self.weight +=1
		if self.window == False:
			self.weight +=1
	def itMustBeDirty(self):
		if self.desk and self.floor and self.trash and self.window:
			print ("LUL")
			self.window = False
	def incWeight(self):
		self.weight+=1

		

		
		
