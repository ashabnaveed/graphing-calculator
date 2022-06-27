from numpy import *
import matplotlib.pyplot as plt

def Calculation():
	print("Operations/Calculations")
	prob = ""
	while prob != "q":
		try:
			print("Enter problem")
			prob = input()
			print(eval(bytes([ord(p) for p in prob])))
		except:
			if prob != "q":
				print("Invalid input")


def Graphing():
	print("Graphing")
	eq, r1, r2 = "", 0, 0
	while eq != "q":
		try:
			print("Enter equation")
			eq = input()
			if eq == "q":
				break
			print("Enter range 1")
			r1 = input()
			if r1 == "q":
				break
			else:
				r1 = int(r1)
			print("Enter range 2")
			r2 = input()
			if r2 == "q":
				break
			else:
				r2 = int(r2)
			x = array(range(int(r1), int(r2)))
			y = eval(bytes([ord(p) for p in eq]))
			plt.plot(x, y)
			plt.show()
		except:
			if eq != "q":
				print("Invalid input")

mode = ""

while mode != "q":
	print(""" 
		1. c (Calculator)
		2. g (Graphing)
		3. q (Quit)
		""")
	mode = input().lower()
	if mode == "c":
		Calculation()
	if mode == "g":
		Graphing()
