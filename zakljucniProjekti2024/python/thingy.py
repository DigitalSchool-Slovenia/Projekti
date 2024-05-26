import random
money = 10000
bet = int(input("Koliko boš stavil: "))
vprašanje = input("Choose color (black, red, green): ")
stvar = random.randint(0,36)
black = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
red = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green = [0]
roulette = [black, red, green]
if vprašanje == "black":
	if stvar in black:
		print("Uganil si. Dobil si", bet)
		print("Imaš še", moeny + bet)
	else:
		print("izgubil si. izgubil si", bet)
		print("Imaš še", money - bet)
elif vprašanje == "red":
	if stvar in red:
		print("uganil si. Dobil si", bet)
		print("Imaš še", moeny + bet)
	else:
		print("izgubil si. izgubil si", bet)
		print("Imaš še", money - bet)
elif vprašanje == "green":
	if stvar in green:
		print("uganil si. Dobil si", bet)
		print("Imaš še", moeny + bet)
	else:
		print("izgubil si. izgubil si", bet)
		print("Imaš še", money - bet)

if stvar in red:
	print("izžrebana številka je" , stvar, "ki je rdeča")
elif stvar in black:
	print("izžrebana številka je" , stvar, "ki je črna")
else:
	print("izžrebana številka je" , stvar, "ki je zelena")

