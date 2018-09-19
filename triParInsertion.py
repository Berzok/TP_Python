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
		tableau.append(min(tableau)-(random.randint(0, 413)))
		tableau.reverse()
		return tableau
	except:
		taille = random.randint(1, 1000)
		for i in range(taille):
			tableau.append(random.randint(-999, 1000))
		tableau.append(min(tableau)-(random.randint(0, 413)))
		tableau.reverse()
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


def triParInsertion(tableau):
	i = 0
	j = 0
	for i in range(2, len(tableau)-1):
		j = i-1
		laValeur = tableau[i]
		while tableau[j] > laValeur:
			tableau[j+1] = tableau[j]
			j -= 1
		tableau[j+1] = laValeur
	tableau.reverse()
	tableau.reverse()
	return tableau



print "Taille limite du tableau ? Ou rien pour une taille aléatoire"
valeur = raw_input()
unCompteur = 0
tableau = alea_tableau(valeur)
afficher_tableau(tableau)
tableau = triParInsertion(tableau)
afficher_tableau(tableau)







