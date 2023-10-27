import random

def choixDujoueur():
	print("-------------------------")
	print("pierre - Choix A ")
	print("feuille - Choix B")
	print("ciseaux - Choix C")
	choix_du_jouer = input("Entrer la lettre associé à votre action : ")
	print("-------------------------")
	if choix_du_jouer=='A':
		joueur='pierre'
	elif choix_du_jouer=='B':
		joueur='feuille'
	else:
		joueur='ciseaux'
	return joueur

def randomOrdi():
	choix_de_lordi=random.randrange(1, 3)
	if choix_de_lordi==0:
		ordinateur='pierre'
	elif choix_de_lordi==1:
		ordinateur='feuille'
	else:
		ordinateur='ciseaux'
	return ordinateur

def gagnant(joueur, ordinateur):
	scoreHumain, scoreOrdinateur = 0, 0
	if joueur == ordinateur:
		print("Égalité !")	
	elif (joueur == 'pierre' and ordinateur == 'ciseaux') or \
			(joueur == 'papier' and ordinateur == 'pierre') or \
			(joueur == 'ciseaux' and ordinateur == 'papier'):
		print("Le joueur gagne !")
		scoreHumain += 1
	else:
		print("L'ordinateur gagne !")
		scoreOrdinateur += 1
		print("-------------------------")
	return scoreHumain, scoreOrdinateur

def shifoumi():
	score_joueur=0
	score_ordinateur=0

	continuer = ""
	while continuer != "N":
		joueur = choixDujoueur()
		ordinateur = randomOrdi()

		print(joueur,ordinateur)

		resh, reso = gagnant(joueur, ordinateur)
		score_joueur += resh
		score_ordinateur += reso
		print("Le score du joueur est : ", score_joueur, " |", "Le score de l'ordinateur est :",score_ordinateur)
		print("Voulez vous refaire une partie ? Oui (O)/ Non (N) ")
		continuer = str(input("Entrer la lettre O ou N : "))
