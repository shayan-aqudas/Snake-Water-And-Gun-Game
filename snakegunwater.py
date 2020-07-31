import random
import datetime

def gettime():
	return datetime.datetime.now()

chance = 10
com = 0
your = 0
name = input("Enter Your Name :")
while (chance>1):
	lst = ["S", "G", "W"]
	rand = random.choice(lst)
	chance = chance-1
	print("[S] Snack [G] Gun and [W] Water")
	inp = input("Enter Here :").capitalize()	
	if rand==inp:
		print(f"You Guess {inp} and Computer {rand}\n")
		print("Both are wins!\n")
		your = your+1
		com = com+1
		print(f"Your point {your} computer point {com}\n")
		print("Left",chance, "out of 10\n")
	elif rand==lst[0] and inp==lst[1]:
		print(f"You Guess {inp} and Computer {rand}\n")
		print("You Win\n")
		your = your + 1
		print(f"Your point {your} computer point {com}\n")
		print("Left",chance, "out of 10\n")
	elif rand==lst[1] and inp==lst[0]:
		print(f"You Guess {inp} and Computer {rand}\n")
		print("Opponent Win\n")
		com = com+1
		print(f"Your point {your} computer point {com}\n")
		print("Left",chance, "out of 10\n")
	elif rand==lst[2] and inp==lst[1]:
		print(f"You Guess {inp} and Computer {rand}\n")
		print("Opponent Win\n")
		com = com+1
		print(f"Your point {your} computer point {com}\n")
		print("Left",chance, "out of 10\n")
	elif rand==lst[0] and inp==lst[2]:
		print(f"You Guess {inp} and Computer {rand}\n")
		print("Opponent Win\n")
		com = com+1
		print(f"Your point {your} computer point {com}\n")
		print("Left",chance, "out of 10\n")
	elif rand==lst[1] and inp==lst[2]:
		print(f"You Guess {inp} and Computer {rand}\n")
		print("You Win\n")
		your = your+1
		print(f"Your point {your} computer point {com}\n")
		print("Left",chance, "out of 10\n")
	elif rand==lst[2] and inp==lst[0]:
		print(f"You Guess {inp} and Computer {rand}\n")
		print("You Win\n")
		your = your+1
		print(f"Your point {your} computer point {com}\n")
		print("Left",chance, "out of 10\n")
	else:
		chance = chance+1
		print("Left",chance, "out of 10\n")
		print("Invalid Word")
		
if com>your:
	print("Your Total Point =", your)
	print("Computer Total Point =", com)
	print("Computer Win and You Lose")
elif com<your:
	print("Your Total Point =", your)
	print("Computer Total Point =", com)
	print("Congretulation You Win and Computer Lose")
f = open("sgw.txt", "a")
f.write(name+"\n"+"Your Total Point ="+str(your)+"\n"+"Computer Total Point ="+str(com))
