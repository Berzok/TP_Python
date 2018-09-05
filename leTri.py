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


def placer_dans_tableau(tableau):
	indice = 0
	droite = len(tableau)-1
	bas = indice+1
	haut = droite
	while bas <= haut:
		while tableau[bas] <= tableau[gauche]:
			bas += 1
		while tableau[haut] > tableau[gauche]:
			haut += 1
		if bas < haut:
			echanger_elements(bas, haut)
	echanger_ele



def alea_tableau(*n):
	tableau = []
	if not n:
		taille = random.randint(1, 100)
	else:
		n = int(n[0])
		taille = n
	for i in range(taille):
		tableau.append(random.randint(-100, 100))
	return tableau


def afficher_tableau(tab):
	for i in tab:
		if i is tab[0]:
			print "["+str(i)+",",
			continue
		if i is tab[len(tab)-1]:
			print str(i)+"]"
			break
		print str(i)+",",


def verification_tri_rapide(tab):
	for j in range(len(tab)-1):
		print oui


def tri_rapide(tab):
	pivot = tab[0]
	bas = tab[1]
	haut = tab[len(tab)-1]
	for i in tab[1::]:
		for j in reversed(tab):
			print i, j

print "Taille limite du tableau ? Ou rien pour une taille aléatoire"
valeur = raw_input()
if valeur == "" or valeur == " ":
	tableau = alea_tableau()
else:
	tableau = alea_tableau(valeur)
afficher_tableau(tableau)

tri_rapide(tableau)

