#coding: utf-8
import os
import random

os.system('clear')

def creer_tableau():
	tab = []
	print "Entrez une valeur à ajouter à la liste à trier, ou rien pour arrêter"
	while True:
		valeur = raw_input()
		if valeur == " " or valeur == "":
			break
		tab.append(valeur)
		afficher_tableau(tab)
	return tab


def echanger_elements(tableau, a, b):
	leTemporaire = tableau[a]
	tableau[a] = tableau[b]
	tableau[b] = leTemporaire


def placer_dans_tableau(tableau, gauche, droite):
	bas = gauche+1
	haut = droite
	while bas <= haut:
		while tableau[bas] <= tableau[gauche]:
			bas += 1
		while tableau[haut] > tableau[gauche]:
			haut -= 1
		if bas < haut:
			echanger_elements(tableau, bas, haut)
			bas += 1
			haut -= 1
	echanger_elements(tableau, gauche, haut)
	k = haut
	return tableau, k



def alea_tableau(*n):
	tableau = []
	try:
		n = int(n[0])
		taille = n
	except:
		taille = random.randint(1, 1000)
	for i in range(taille):
		tableau.append(random.randint(-999, 1000))
	tableau.append(max(tableau)+(random.randint(0, 413)))
	return tableau


def afficher_tableau(tab):
	print ""
	for i in tab:
		if i is tab[0]:
			print "["+str(i)+",",
			continue
		if i is tab[len(tab)-1]:
			print str(i)+"]"
			break
		print str(i)+",",




def tri_rapide(tableau, gauche, droite):
	k = 0
	if gauche < droite:
		tableau, k = placer_dans_tableau(tableau, gauche, droite)
		tableau = tri_rapide(tableau, gauche, k-1)
		tableau = tri_rapide(tableau, k+1, droite)
	return tableau

print "Taille limite du tableau ? Ou rien pour une taille aléatoire"
valeur = raw_input()
tableau = alea_tableau()

tableau = tri_rapide(tableau, 0, len(tableau)-1)
afficher_tableau(tableau)

