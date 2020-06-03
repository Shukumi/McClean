from room import Room
from random import getrandbits
class Level(object):
	def __init__(self,room): 
		self.room = room
	def ausgabe(self):
		x = 1
		#print("Rooms: " + room.ausgabe())
		for i in self.room:
			print ("Room " + str(x) + ": ")
			i.ausgabe()
			x +=1
	def randomLevel(self):
		for ro in self.room:
			ro.desk = bool(getrandbits(1))
			ro.floor = bool(getrandbits(1))
			ro.trash = bool(getrandbits(1))
			ro.window = bool(getrandbits(1))
			ro.calWeight()
		
		
