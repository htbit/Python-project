import random

def flip():
	flip = random.random()
	if (flip>=.5):
		return True
	else:
		return False

def main(num):
	heads = 0
	tails = 0
	resultString = ""

	for i in range(int(num)):
		if (flip()):
			heads+=1
			resultString += "О "
		else:
			tails+=1
			resultString += "Р "
	
	print ("Выпало орел: %i" % (heads))
	print ("Выпало решка: %i" % (tails))
	print (resultString)

userInput = input("Сколько раз подпросить монету: ")
main(userInput)