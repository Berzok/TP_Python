#coding: utf-8

from affiche_arbre import * 
from saisie import * 


################################################################################


def entrer_Arbre():
		"""let the user input the values for A A"""
		A = Arbre(None, None, None)
		inp = raw_input("Value : ")
		if inp != "":
			A.val = inp
			inp = raw_input("Value : ")
			while inp != "":
				addLeaf(A, inp)
				inp = raw_input("Value : ")
		return A


def recherche(A, x):
	"""Recherche x dans A, de manière récursive"""
	if A:
		if A.val == x:
			return A
		if A.val < x:
			return recherche(A.D, x)
		else:
			return recherche(A.G, x)

def recherche_iter(A, x):
	"""Recherche x dans A, de manière itérative"""
	if A:
		




def addLeaf(A, x):
	if A == None:
		return create_leaf(x)
	else:
		if A.val >= x:
			A.G = addLeaf(A.G, x)
		else:
			A.D = addLeaf(A.D, x)
	return A


def create_leaf(x):
	return Arbre(x, None, None)


def parcours_prefixe(A):
	"""parcours d'un arbre en ordre prefixe"""
	if A != None:
		print A.val,
		parcours_prefixe(A.G)
		parcours_prefixe(A.D)


def parcours_ascendant(A):
	"""Valeur de A dans l'ordre ascendant'"""
	if A:
		parcours_ascendant(A.G)
		print A.val
		parcours_ascendant(A.D)


def second_key(A):
	"""Deuxième + grande clef d'un ARBR'"""
	if A:
		if A.D:
			if A.D.D == None:
				if A.D.G == None:
					return A.val
			return second_key(A.D)
		elif A.G:
			if A.G.G == None:
				if A.G.D == None:
					return A.G.val
			return second_key(A.G)
		return A.val

def bruler(A, x):
	"""Brûle la feuille X de l'arbre A'"""
	if A == None:
		return A
	if A.val == x:
		return deraciner(A)
	else:
		if A.val > x:
			A.G = bruler(A.G, x)
		else:
			A.D = bruler(A.D, x)
		return A


def deraciner(A):
	if A.G == None:
		A = A.D
	else:
		if A.D == None:
			A = A.G
		else:
			b = A.G
			if b.D == None:
				A.val = b.val
				A.G = b.G
			else:
				temp = b.D
			while temp.D != None:
				b = temp
				temp = temp.D
			A.val = temp.val
			b.D = temp.G
	return A





treeDrawer = TreeDrawer()
cerisier = entrer_Arbre()
#parcours_prefixe(A)
treeDrawer.dessiner_arbre(cerisier)
search(cerisier, 2)
parcours_ascendant(cerisier)
#print "SECONDE CLEF PLUS GRANDE : ", second_key(cerisier)
#cerisier = addLeaf(cerisier, raw_input("ENTER A NUMBER : "))
#treeDrawer.dessiner_arbre(cerisier)
#cerisier = delete(cerisier, raw_input("ENTER A NUMBER : "))
#treeDrawer.dessiner_arbre(cerisier)
treeDrawer.wait()





