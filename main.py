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