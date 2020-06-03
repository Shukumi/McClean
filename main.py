from level import Level
from room import Room
from robot import Robot
from tkinter import *
from random import getrandbits
from random import *
from time import sleep
from _thread import start_new_thread

roomList = []
LoW = []

LoWi = [False,False,False,False,False,False]

def generateLevel():
	for i in range (0,6):
		newRoom = Room(i+1,bool(getrandbits(1)),bool(getrandbits(1)),bool(getrandbits(1)),bool(getrandbits(1)))
		newRoom.itMustBeDirty()
		roomList.append(newRoom)
		newRoom.calWeight()

	global newLevel
	newLevel = Level(roomList)
	newLevel.ausgabe()
	
generateLevel()

newRobot = Robot("McClean")
newRobot.ausgabe()

root = Tk()
defaultbg = root.cget('bg')




def counter_label(label,typ,raumnr):
	def count():
		if typ== "desk":
			if newLevel.room[raumnr-1].desk == True:
				label.config(text="Sauber", fg="green")
				label.after(200, count)
			else:
				label.config(text="Dreckig", fg="red")
				label.after(200, count)
		elif typ =="floor":
			if newLevel.room[raumnr-1].floor == True:
				label.config(text="Sauber", fg="green")
				label.after(200, count)
			else:
				label.config(text="Dreckig", fg="red")
				label.after(200, count)
		elif typ=="trash":
			if newLevel.room[raumnr-1].trash == True:
				label.config(text="Sauber", fg="green")
				label.after(200, count)
			else:
				label.config(text="Dreckig", fg="red")
				label.after(200, count)
		
		elif typ=="window":
			if newLevel.room[raumnr-1].window == True:
				label.config(text="Sauber", fg="green")
				label.after(200, count)
			else:
				label.config(text="Dreckig", fg="red")
				label.after(200, count)
	count()	
	
root.title("RobotClean")
Titel1 = Label(root, text ="1. Raum", font = "Verdana 12 italic bold")
Titel1.grid(row=0,column=0)
Label(root, text ="Desk", font = "Verdana 10 italic").grid(row=1,column=0)
Label(root, text ="Floor", font = "Verdana 10 italic").grid(row=2,column=0)
Label(root, text ="Trash", font = "Verdana 10 italic").grid(row=3,column=0)
Label(root, text ="Window", font = "Verdana 10 italic").grid(row=4,column=0)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=1,column=1)
counter_label(cLabel,"desk",1)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=2,column=1)
counter_label(cLabel,"floor",1)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=3,column=1)
counter_label(cLabel,"trash",1)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=4,column=1)
counter_label(cLabel,"window",1)

Titel2 = Label(root, text ="2. Raum", font = "Verdana 12 italic bold")
Titel2.grid(row=0,column=2)
Label(root, text ="Desk", font = "Verdana 10 italic").grid(row=1,column=2)
Label(root, text ="Floor", font = "Verdana 10 italic").grid(row=2,column=2)
Label(root, text ="Trash", font = "Verdana 10 italic").grid(row=3,column=2)
Label(root, text ="Window", font = "Verdana 10 italic").grid(row=4,column=2)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=1,column=3)
counter_label(cLabel,"desk",2)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=2,column=3)
counter_label(cLabel,"floor",2)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=3,column=3)
counter_label(cLabel,"trash",2)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=4,column=3)
counter_label(cLabel,"window",2)

Titel3 = Label(root, text ="3. Raum", font = "Verdana 12 italic bold")
Titel3.grid(row=0,column=4)
Label(root, text ="Desk", font = "Verdana 10 italic").grid(row=1,column=4)
Label(root, text ="Floor", font = "Verdana 10 italic").grid(row=2,column=4)
Label(root, text ="Trash", font = "Verdana 10 italic").grid(row=3,column=4)
Label(root, text ="Window", font = "Verdana 10 italic").grid(row=4,column=4)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=1,column=5)
counter_label(cLabel,"desk",3)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=2,column=5)
counter_label(cLabel,"floor",3)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=3,column=5)
counter_label(cLabel,"trash",3)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=4,column=5)
counter_label(cLabel,"window",3)

Titel4 = Label(root, text ="4. Raum", font = "Verdana 12 italic bold")
Titel4.grid(row=0,column=6)
Label(root, text ="Desk", font = "Verdana 10 italic").grid(row=1,column=6)
Label(root, text ="Floor", font = "Verdana 10 italic").grid(row=2,column=6)
Label(root, text ="Trash", font = "Verdana 10 italic").grid(row=3,column=6)
Label(root, text ="Window", font = "Verdana 10 italic").grid(row=4,column=6)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=1,column=7)
counter_label(cLabel,"desk",4)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=2,column=7)
counter_label(cLabel,"floor",4)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=3,column=7)
counter_label(cLabel,"trash",4)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=4,column=7)
counter_label(cLabel,"window",4)

Titel5 = Label(root, text ="5. Raum", font = "Verdana 12 italic bold")
Titel5.grid(row=0,column=8)
Label(root, text ="Desk", font = "Verdana 10 italic").grid(row=1,column=8)
Label(root, text ="Floor", font = "Verdana 10 italic").grid(row=2,column=8)
Label(root, text ="Trash", font = "Verdana 10 italic").grid(row=3,column=8)
Label(root, text ="Window", font = "Verdana 10 italic").grid(row=4,column=8)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=1,column=9)
counter_label(cLabel,"desk",5)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=2,column=9)
counter_label(cLabel,"floor",5)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=3,column=9)
counter_label(cLabel,"trash",5)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=4,column=9)
counter_label(cLabel,"window",5)

Titel6 = Label(root, text ="6. Raum", font = "Verdana 12 italic bold")
Titel6.grid(row=0,column=10)
Label(root, text ="Desk", font = "Verdana 10 italic").grid(row=1,column=10)
Label(root, text ="Floor", font = "Verdana 10 italic").grid(row=2,column=10)
Label(root, text ="Trash", font = "Verdana 10 italic").grid(row=3,column=10)
Label(root, text ="Window", font = "Verdana 10 italic").grid(row=4,column=10)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=1,column=11)
counter_label(cLabel,"desk",6)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=2,column=11)
counter_label(cLabel,"floor",6)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=3,column=11)
counter_label(cLabel,"trash",6)
cLabel = Label(root, text ="Clean", font = "Verdana 10 italic")
cLabel.grid(row=4,column=11)
counter_label(cLabel,"window",6)

def counter_label2(label,raumnr):
	def count():
		if LoWi[raumnr-1]:
			label.config(text="Wichtig", fg="red")
			label.after(200, count)
			newLevel.room[raumnr-1].weight += 5
			
		else:
			label.config(text="Nicht wichtig", fg="green")
			label.after(200, count)
	count()	

cLabel = Label(root, text ="Nicht wichtig", font = "Verdana 10 italic")
cLabel.grid(row=5,column=0)
counter_label2(cLabel,1)
cLabel = Label(root, text ="Nicht wichtig", font = "Verdana 10 italic")
cLabel.grid(row=5,column=2)
counter_label2(cLabel,2)
cLabel = Label(root, text ="Nicht wichtig", font = "Verdana 10 italic")
cLabel.grid(row=5,column=4)
counter_label2(cLabel,3)
cLabel = Label(root, text ="Nicht wichtig", font = "Verdana 10 italic")
cLabel.grid(row=5,column=6)
counter_label2(cLabel,4)
cLabel = Label(root, text ="Nicht wichtig", font = "Verdana 10 italic")
cLabel.grid(row=5,column=8)
counter_label2(cLabel,5)
cLabel = Label(root, text ="Nicht wichtig", font = "Verdana 10 italic")
cLabel.grid(row=5,column=10)
counter_label2(cLabel,6)
def markiereRaum(i):
	if i == 0:
		Titel1.config(fg="lightblue", bg="darkblue")
	elif i == 1:
		Titel2.config(fg="lightblue", bg="darkblue")
	elif i == 2:
		Titel3.config(fg="lightblue", bg="darkblue")
	elif i == 3:
		Titel4.config(fg="lightblue", bg="darkblue")
	elif i == 4:
		Titel5.config(fg="lightblue", bg="darkblue")
	elif i == 5:
		Titel6.config(fg="lightblue", bg="darkblue")
def entmarkiereRaum(i):
	if i == 0:
		Titel1.config(fg="black", bg=defaultbg)
	elif i == 1:
		Titel2.config(fg="black", bg=defaultbg)
	elif i == 2:
		Titel3.config(fg="black", bg=defaultbg)
	elif i == 3:
		Titel4.config(fg="black", bg=defaultbg)
	elif i == 4:
		Titel5.config(fg="black", bg=defaultbg)
	elif i == 5:
		Titel6.config(fg="black", bg=defaultbg)

		
def startCleaning():
	start_new_thread(startCleaning2,())
	start_new_thread(makeImportant, ())
	

def makeDirty(room):
	sleep(6)
	room.desk = bool(getrandbits(1))
	room.floor = bool(getrandbits(1))
	room.trash = bool(getrandbits(1))
	room.window = bool(getrandbits(1))
	room.itMustBeDirty()
	room.calWeight()
	
def makeImportant():
	global LoWi
	sleep(20)
	LoWi = [bool(getrandbits(1)),bool(getrandbits(1)),bool(getrandbits(1)),bool(getrandbits(1)),bool(getrandbits(1)),bool(getrandbits(1))]
	makeImportant()
	
	
			
		
def startCleaning2():
	zwischen = 5
	counter = 0
	while True:
		LoW = []
		indices = []
		for room in newLevel.room:
			LoW.append(room.weight)
			#print (LoW)
			zwischen = max(LoW)
			indices = [i for i, x in enumerate(LoW) if x == zwischen]
		#print (indices)

		markiereRaum(indices[0])
		newRobot.clean(newLevel.room[indices[0]])
		start_new_thread(makeDirty,(newLevel.room[indices[0]],))
		newLevel.room[indices[0]].calWeight()
		LoWi[newLevel.room[indices[0]].raumnr-1] = False
		counter+=1
		
		sleep(1)
		entmarkiereRaum(indices[0])

		for room in newLevel.room:
			room.incWeight()
		if counter == 15:
			print ("Stopped because Max Iterations are reached")
			break
		
		


startbutton = Button(root, text="Start", command=startCleaning, bg="lightblue").grid(row=6,column=5)
closebutton = Button(root, text="Close", command=quit, bg="lightblue").grid(row=6,column=6)

root.mainloop()


