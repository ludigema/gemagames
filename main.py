
from chifoumy import shifoumi

def menu():
	print("-------------------------")
	print("A quel jeu voulez-jouer : ?")
	print("Entrez 1 pour le Morpion")
	print("Entrez 2 pour le ShifouMi")
	print("-------------------------")
	# print des jeux avec leur numéro
	user_input = int(input("Entrer le numéro du jeu : "))
	return user_input

def main():
	continuer = ""
	while continuer != "N" :
		numero_de_selection=menu()
		if numero_de_selection==2:
			shifoumi()

		print("Voulez vous refaire une partie ? Oui (O)/ Non (N) ")
		continuer = str(input("Entrer la lettre O ou N : "))


if __name__ == '__main__':
	main()

