# -*- coding: utf-8 -*-

### Interface de saisie : Pierre Lartigau, automne 2016  ###

class Arbre:
	""" Implémentation des Arbres binaires ( D = droite; G = gauche)"""
	
	val = None	#valeur du noeud
	G = None		#sous arbre Gauche
	D = None		#sous arbre Droit
	
	def __init__(self, valeur, aG, aD):
		self.val = valeur
		self.G = aG
		self.D = aD
	
	def ajouterFils(self, a, cote):
		if cote == "G":
			self.G = a
		elif cote == "D":
			self.D = a


def entrerArbre(p):
	print "    "*(p-1),
	valeur = raw_input("Valeur : ")
	if valeur == "":
		return None
	else:
		return Arbre(valeur, entrerArbre(p+1), entrerArbre(p+1))
