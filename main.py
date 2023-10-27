import random

def main():
	print("-------------------------")
	print("A quel jeu voulez-jouer : ?")
	print("Entrez 1 pour le Morpion")
	print("Entrez 2 pour le ShifouMi")
	print("-------------------------")
	# print des jeux avec leur numéro
	user_input = int(input("Entrer le numéro du jeu : "))
	return user_input

def shifoumi():
	score=0
	print("-------------------------")
	print("pierre - Choix A ")
	print("feuille - Choix B")
	print("ciseaux - Choix C")
	joueur=str()
	Choix_du_jouer = str(input("Entrer la lettre associé à votre action : "))
	print("-------------------------")
	if Choix_du_jouer=='A':
		joueur=='pierre'
	elif Choix_du_jouer=='B':
		joueur=='feuille'
	else:
		joueur=='ciseaux'
	Choix_de_lordi=random.randrange(1, 3)
	if Choix_de_lordi==1:
		joueur=='pierre'
	elif Choix_de_lordi==2:
		joueur=='feuille'
	else:
		joueur=='ciseaux'


if __name__ == '__main__':
	Numero_de_selection=main()
	if Numero_de_selection==2:
		shifoumi()


# Choix pierre feuille
# Random de la machine

