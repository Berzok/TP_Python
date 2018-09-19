# coding: utf-8
import os

class Automate:
	"""classe permettant de manipuler des automates finis,
	déterministes ou non, avec ou sans epsilon-transitions"""


	def __init__(self, alphabet, etats, transition, initiaux, finals):
		"""fonction d'initialisation (constructeur) de l'automate"""
		
		# l'alphabet est une liste (list) de symboles 
		# (généralement des int ou str).
		# on réserve le mot 'eps' comme symbole des epsilon-transitions
		self.alphabet = alphabet

		# ensemble (set) d'etats (généralement des int ou str)
		self.etats = etats

		# ensemble (set) des etats initiaux
		self.initiaux = initiaux

		# ensemble (set) des etats final
		self.finals = finals

		# fonction de transition : c'est un dict de dict de set !
		# plus simplement si auto est un automate, q un etat et s un symbole
		# alors auto.transition[q][s] est un ensemble (set) contenant
		# les etats de transition possibles depuis q pour le symbole s
		# on pourra aussi prendre s='eps' pour les epsilon-transitions
		if transition != None:
		    self.transition = transition
		else:
		    # on initialise des ensembles de transitions vides
		    self.transition = initialiser_transition(alphabet, etats)

	@staticmethod
	def initialiser_transition(alphabet, etats):
		"""méthode statique permettant d'initialiser la fonction
		de transition a partir de l'ensemble d'etats et de l'alphabet
		(deux 'list'). Pour chaque etat q et symbole s et pour s='eps',
		transition[q][s] sera un set (ensemble) vide au depart."""

		transition = {}
		for q in etats :
		    transition[q] = {}
		    for a in alphabet + ['eps'] :
		        transition[q][a] = set([])
		return transition


	def __str__(self):
		"""conversion en str : permet d'afficher un automate auto dans 
		la console a en faisant simplement 'print a'     """
		texte = "AUTOMATE\n   ALPHABET\n     "
		for symb in self.alphabet:
		    texte += " " + str(symb)
		texte +="\n   ETATS\n     "
		for e in self.etats:
		    texte += " " + str(e)
		texte +="\n   TRANSITIONS\n"
		for q in self.transition:
		    for symb in self.transition[q]:
		        if len(self.transition[q][symb]) > 0 :
		            texte += "      " + str(q) + " --" + str(symb) + "-->"
		            for q2 in self.transition[q][symb] :
		                texte += " " + str(q2)
		            texte +="\n"
	 
		texte +="   INITIAUX\n     "
		for e in self.initiaux:
		    texte += " " + str(e)
		    texte +="\n   FINALS\n     "
		for e in self.finals:
		    texte += " " + str(e)
		return texte


	def verification(self):
		"""méthode qui vérifie que l'automate est convenablement formé
		assert renvoie une exception si la condition
		n'est pas vérifiée"""

		#verifie les types des champs de l'automate
		assert type(self.alphabet) is list
		assert type(self.etats) is set
		assert type(self.initiaux) is set
		assert type(self.finals) is set

		#verifie que 'eps' ne soit pas dans l'alphabet
		assert 'eps' not in self.alphabet

		#on verifie que la fonction de transition contient toutes les entrees
		#etat * symbole exactement et que les ensembles correspondants
		#sont bien des ensembles d'états
		assert type(self.transition) is dict
		assert set(self.transition.keys()) == self.etats

		for q in self.etats:
			assert set(self.transition[q].keys()) \
					== set(self.alphabet + ["eps"])

			for symb in self.alphabet + ['eps']:
				for q2 in self.transition[q][symb]:
					assert q2 in self.etats

		#etats initiaux non vide et sont des etats
		assert self.initiaux and self.initiaux.issubset(self.etats)

		#etats finals non vide et sont des etats
		assert self.finals and self.initiaux.issubset(self.etats)

	def est_complet(self):
		lesTransitions = []
		for i in self.etats:
			for j in self.alphabet:
				if self.transition[i][j]:
					lesTransitions.append(j)
			if lesTransitions != self.alphabet:
				return False
			lesTransitions = []
		return True

	def est_deterministe(self):
		def parcourir(etat, symbole):
			print lesEtats
			if not etat:
				return True
			if len(self.transition[etat][symbole]) > 1:
				return False
			else:
				return parcourir(etat.pop(), symbole)
		lesEtats = set(self.etats)
		print lesEtats
		return parcourir(self.etats.copy().pop(), self.alphabet[0])
	
	def contient_epsilon(self):
		print self
		for i in self.etats:
			for j in self.alphabet:
				print i, j, self.transition[i][j]
				if self.transition[i][j] == "eps":
					return True
		return False

def lire_automate(nomfichier):
	"""lit un fichier contenant un automate et renvoie l'automate
	correspondant. 

	FORMAT D'UN FICHIER AUTOMATES
	commentaires au debut puis dans l'ordre :

	1. une ligne 
	ALPHABET s1 s2 ... 
	où s1, s2, ... sont les symboles (str) de l'alphabet

	2. une ligne 
	ETATS q1 q2 ...
	où q1, q2, etc. sont les noms (str) des états

	3. autant de lignes 
	TRANSITION  etat_depart  symbole  etat_arrivee 
	que nécessaire

	4. une ligne 
	INITIAUX i1 i2 ...
	liste des etats initiaux

	5. une ligne 
	FINALS f1 f2 ... 
	liste des etats finals"""


	#lit et met toutes les lignes du fichier dans un tableau de str
	fichier = open(nomfichier,"r")
	lignes = fichier.readlines()
	fichier.close()

	i = 0 # numero de ligne

	#recherche de la première ligne commençant par "ALPHABET"
	mots = lignes[i].split()
	while len(mots)==0 or mots[0] != "ALPHABET":
		i +=1 
		mots = lignes[i].split()
	alphabet = mots[1:]

	#idem pour "ETATS"
	i +=1
	mots = lignes[i].split()
	while mots[0] != "ETATS":
		i +=1 
		mots = lignes[i].split()
	etats = set(mots[1:])

	#idem pour "TRANSITION"
	i+=1
	mots = lignes[i].split()
	while mots[0] != "TRANSITION":
		i +=1 
		mots = lignes[i].split()


	transition = Automate.initialiser_transition(alphabet, etats)
	#pour chaque ligne "TRANSITION" on ajoute ce qui crresipond
	while mots[0] == "TRANSITION":
		depart = mots[1]
		symbole = mots[2]
		arrivee = mots[3]
		transition[depart][symbole].add(arrivee)
		i +=1 
		mots = lignes[i].split()

	while mots[0] != "INITIAUX":
		i +=1 
		mots = lignes[i].split()
	initiaux = set(mots[1:])

	while mots[0] != "FINALS":
		i +=1 
		mots = lignes[i].split()
	finals = set(mots[1:])

	resultat = Automate(alphabet, etats, transition, initiaux, finals)

	#on lance une verification de l'automate
	try:
		resultat.verification()
	except AssertionError as e:
		raise 

	return resultat


def mots_taille_au_plus(n, alphabet):
	"""renvoie la liste des mots de taille de 0 à n compris
	dans l'alphabet fourni"""

	mots = [ [''] ] + [ [] for i in range(n)]
	for i in range(1,n+1):
		for symb in alphabet:
			mots[i].extend([m+symb for m in mots[i-1]])
	return [x for ligne in mots for x in ligne]


os.system('clear')


print "*" * 45
auto1 = lire_automate("auto1.txt")
print auto1, "\n", auto1.est_complet(), "\n", auto1.est_deterministe(), "\n", auto1.contient_epsilon(), "\n\n", "*"*45
auto2 = lire_automate("auto2.txt")
print auto2, "\n", auto2.est_complet(), "\n", auto2.est_deterministe(), "\n", auto2.contient_epsilon(), "\n\n", "*"*45
auto3 = lire_automate("auto3.txt")
print auto3, "\n", auto3.est_complet(), "\n", auto3.est_deterministe(), "\n", auto3.contient_epsilon(), "\n\n", "*"*45
auto4 = lire_automate("auto4.txt")
print auto4, "\n", auto4.est_complet(), "\n", auto4.est_deterministe(), "\n", auto4.contient_epsilon(), "\n\n", "*"*45












