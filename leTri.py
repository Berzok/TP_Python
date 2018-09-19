#coding: utf-8
import os
import random

os.system('clear')



def alea_tableau(*n):
	tableau = []
	try:
		n = int(n[0])
		taille = n
		for i in range(taille):
			tableau.append(random.randint(-999, 1000))
		tableau.append(max(tableau)+(random.randint(0, 413)))
		return tableau
	except:
		taille = random.randint(1, 1000)
		for i in range(taille):
			tableau.append(random.randint(-999, 1000))
		tableau.append(max(tableau)+(random.randint(0, 413)))
		return tableau


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



def tri_rapide(tableau, gauche, droite, leCompteur=0):
	leCompteur = 0 + leCompteur
	k = 0
	if gauche < droite:
		tableau, k, leCompteur = placer_dans_tableau(tableau, gauche, droite, leCompteur)
		tableau, leCompteur = tri_rapide(tableau, gauche, k-1, leCompteur)
		tableau, leCompteur = tri_rapide(tableau, k+1, droite, leCompteur)
	return tableau, leCompteur

def placer_dans_tableau(tableau, gauche, droite, leCompteur):
	bas = gauche+1
	haut = droite
	while bas <= haut:
		while tableau[bas] <= tableau[gauche]:
			bas += 1
			leCompteur += 1
		while tableau[haut] > tableau[gauche]:
			haut -= 1
			leCompteur += 1
		if bas < haut:
			echanger_elements(tableau, bas, haut)
			bas += 1
			haut -= 1
		leCompteur += 1
	echanger_elements(tableau, gauche, haut)
	k = haut
	return tableau, k, leCompteur

def echanger_elements(tableau, a, b):
	leTemporaire = tableau[a]
	tableau[a] = tableau[b]
	tableau[b] = leTemporaire


def avgComparaisons(n, p):
	leCompteur = 0
	for i in range(p):
		tableau = alea_tableau(n)
		unCompteur = 0
		tableau, unCompteur = tri_rapide(tableau, 0, len(tableau)-1, 0)
		leCompteur += unCompteur
	return leCompteur


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






print "Taille limite du tableau ? Ou rien pour une taille aléatoire"
valeur = raw_input()
unCompteur = 0
tableau = alea_tableau(valeur)
afficher_tableau(tableau)

tableau, unCompteur = tri_rapide(tableau, 0, len(tableau)-1, 0)
afficher_tableau(tableau)
print "Il y a eu "+str(unCompteur)+" comparaisons."
print ""

print "##########################################################################"
print "Sélectionnez une taille de tableau:"
n = int(input())
print "Sélectionnez maintenant un nombre de tableaux:"
p = int(input())

lesComparaisons = avgComparaisons(n, p)
print ""
print "Pour " + str(p) + " tableaux de taille " +str(n) + ", on aura effectué " + str(lesComparaisons) + " comparaisons."

