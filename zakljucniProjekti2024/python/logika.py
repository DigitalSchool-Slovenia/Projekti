#zaslon 5x5
import os
os.system("pip install colorama")
from colorama import *
init(autoreset=True)
def IzpisiZaslon(zaslon):
	for vrstica in zaslon:
		for stolpec in vrstica:
			print(f"|{Fore.GREEN}{stolpec}{Fore.WHITE}",end="")#vsak 
		print("|")



def zmagovalec(zaslon):
	stevec = 0
	for znak in ("X","O"):
		for vrstica in zaslon:
			for stolpec in vrstica:
				if stolpec !=" ":
					if stolpec == znak:
						stevec+=1
						if stevec >= 4:
							return (True,znak)
							#ce nekdo zmaga
		stevec = 0
	return (False,False)
def igralec(zaslon):
	while True:
		for znak in ("X","O"):
			
			IzpisiZaslon(zaslon)
			pozicija = int(input(f"napisite x coordinat({znak}): "))-1
			#if pozicija =="1":
			#	zaslon[-1][0] = "X"
			#IzpisiZaslon(zaslon)	
			najnizjaVrstica =0
			print(najnizjaVrstica)
			for index_vrstica,element_vrstica in enumerate(zaslon):
				if zaslon[index_vrstica][pozicija] ==" " and index_vrstica<len(zaslon)-1 and zaslon[index_vrstica+1][pozicija] not in ("X","O") :
					najnizjaVrstica+=1
			print(najnizjaVrstica)
			if zaslon[najnizjaVrstica][pozicija]==" ":
				zaslon[najnizjaVrstica][pozicija] = znak
			print(najnizjaVrstica)
			preverjanjeZmagovalca =zmagovalec(zaslon)
			zmagovalecGor = zmagovalecVertikalno(zaslon)
			if preverjanjeZmagovalca[0]:
				IzpisiZaslon(zaslon)
				print(f"Zmagovalec je {preverjanjeZmagovalca[1]}!")
				return
			
			elif zmagovalecGor[0]:
				IzpisiZaslon(zaslon)
				print(f"Zmagovalec je {zmagovalecGor[1]}!")
				return

def zmagovalecVertikalno(zaslon):
	stolpci = []
	for dolzinaZaslona in zaslon:
		stolpci.append([])
	for index_vrstica,vrstica in enumerate(zaslon):
		for  stolpec_index,stolpec in enumerate(vrstica):
			stolpci[stolpec_index].append(stolpec)
	stolpciStringVSeznamu=[]
	for stolpec in stolpci:
		stolpecString = ""
		for stolpec2 in stolpec:
			stolpecString+=stolpec2
		stolpciStringVSeznamu.append(stolpecString)
	
	for stolpciString in stolpciStringVSeznamu:
		for znak in ("X","O"):
			if znak*4 in stolpciString:
				return (True,znak)
	return (False,False)







zaslon = [
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "]
]
try:
	igralec(zaslon)
except KeyboardInterrupt:
	pass
except:
	raise