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
	score_joueur=int()
	score_ordinateur=int()

	while True:
		print("-------------------------")
		print("pierre - Choix A ")
		print("feuille - Choix B")
		print("ciseaux - Choix C")
		joueur=str()
		ordinateur=str()
		Choix_du_jouer = str(input("Entrer la lettre associé à votre action : "))
		print("-------------------------")
		if Choix_du_jouer=='A':
			joueur='pierre'
		elif Choix_du_jouer=='B':
			joueur='feuille'
		else:
			joueur='ciseaux'
		Choix_de_lordi=random.randrange(1, 3)
		

		if Choix_de_lordi==0:
			ordinateur='pierre'
		elif Choix_de_lordi==1:
			ordinateur='feuille'
		else:
			ordinateur='ciseaux'
		print(joueur,ordinateur)
		if joueur == ordinateur:
			print("Égalité !")
			
		elif (joueur == 'pierre' and ordinateur == 'ciseaux') or \
			(joueur == 'papier' and ordinateur == 'pierre') or \
			(joueur == 'ciseaux' and ordinateur == 'papier'):
				print("Le joueur gagne !")
				score_joueur += 1
		else:
				print("L'ordinateur gagne !")
				score_ordinateur += 1
				print("-------------------------")
		print("Le score du joueur est : ", score_joueur, " |", "Le score de l'ordinateur est :",score_ordinateur)
		print("Voulez vous refaire une partie ? Oui (O)/ Non (N) ")
		continuer = str(input("Entrer la lettre O ou N : "))
		if continuer == 'N':
			break


if __name__ == '__main__':
	Numero_de_selection=main()
	if Numero_de_selection==2:
		shifoumi()


