from room import Room
from time import sleep
class Robot(object):
	def __init__(self,name): 
		self.name = name
		self.standort = 1
		self.batterylevel = 100
	def ausgabe(self):
		print("Hallo, mein Name ist : " + self.name)
		print("Ich befinde mich in Raum: " + str(self.standort))
		print ("Mein Batterielevel beträgt momentan" + str(self.batterylevel) + "Prozent")
	def goToRoom(self,room):
		self.standort = room.raumnr
		print("Gehe zu Raum " + str(self.standort))
	def clean(self,room):
		self.goToRoom(room)
		sleep(1)
		if room.desk == False:
			print ("Raum: " + str(room.raumnr) + " Tisch dreckig.. bzzz.. Säubere Tisch..")
			room.desk = True
			sleep(1)
		if room.floor == False:
			print ("Raum: " + str(room.raumnr) + " Boden dreckig.. bzzz.. Säubere Boden..")
			room.floor = True
			sleep(1)
		if room.trash == False:
			print ("Raum: " + str(room.raumnr) + " Müll dreckig.. bzzz.. Säubere Müll..")
			room.trash = True
			sleep(1)
		if room.window == False:
			print ("Raum: " + str(room.raumnr) + " Fenster dreckig.. bzzz.. Säubere Fenster..")
			room.window = True
			#sleep(1)


		
			
		
		

		
		
