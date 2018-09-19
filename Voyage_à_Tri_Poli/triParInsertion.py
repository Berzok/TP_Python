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
		tableau, unCompteur = triParInsertion(tableau)
		leCompteur += unCompteur
	return leCompteur



print "Taille limite du tableau ? Ou rien pour une taille aléatoire"
valeur = raw_input()
unCompteur = 0
tableau = alea_tableau(valeur)
print "Tableau de base:"
afficher_tableau(tableau)
tableau, unCompteur = triParInsertion(tableau)
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







