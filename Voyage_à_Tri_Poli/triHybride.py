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

def afficher_tableau(leTableau):
	tableau = leTableau
	print ""
	for i in tableau:
		if i is tableau[0]:
			print "["+str(i)+",",
			continue
		if i is tableau[len(tableau)-1]:
			print str(i)+"]"
			break
		print str(i)+",",



###########################################################################################
###############              TRI RAPIDE           ####################################################

def tri_rapide(tableau, gauche, droite, leCompteur=0, r=5):
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


def triParInsertion(tableau):
	i = 0
	j = 0
	leCompteur = 0
	for i in range(1, len(tableau)):
		j = i-1
		laValeur = tableau[i]
		while tableau[j] > laValeur:
			leCompteur += 1
			tableau[j+1] = tableau[j]
			j -= 1
		tableau[j+1] = laValeur
	leCompteur += 1
	tableau.reverse()
	tableau.reverse()
	return tableau, leCompteur

def avgComparaisons(n, p):
	leCompteur = 0
	for i in range(p):
		tableau = alea_tableau(n)
		unCompteur = 0
		tableau, unCompteur = tri_hybride(tableau, 0, len(tableau)-1)
		leCompteur += unCompteur
	return leCompteur

##############################################################################################
##############                 TRI HYBDRIDE                              ##########################################

def tri_hybride(tableau, gauche, droite, r=2):
	"""tri rapide de sous tableaux de taille r au plus, dont les elements
	doivent etre inferieurs aux elements du sous tableau suivant le tableau
	intermediaire est ensuite trie par insertion"""
	leCompteur = unCompteur = 0
	if r <= 0:
		return tableau
	tableau, leCompteur = tri_rapide(tableau, gauche, droite, r)
	tableau, unCompteur = triParInsertion(tableau)
	return tableau, (leCompteur + unCompteur)




print "Taille limite du tableau ? Ou rien pour une taille aléatoire"
valeur = raw_input()
unCompteur = 0
tableau = alea_tableau(valeur)
print "Tableau de base:"
afficher_tableau(tableau)
print "\nValeur limite du triage?"
r = int(input())
tableau, unCompteur = tri_hybride(tableau, 0, len(tableau)-1, r)
print ""
print "Tableau trié, et ceci en " + str(unCompteur) + " comparaisons.",
afficher_tableau(tableau)

print "##########################################################################"
print "Sélectionnez une taille de tableau:"
n = int(input())
print "Sélectionnez maintenant un nombre de tableaux:"
p = int(input())

lesComparaisons = avgComparaisons(n, p)
print ""
print "Pour " + str(p) + " tableaux de taille " +str(n) + ", on aura effectué " + str(lesComparaisons) + " comparaisons."
print "Soit une moyenne de " + str(lesComparaisons/p) + " comparaisons par tableau."







