
###############################################################################
# La classe Graphe Non Oriente
###############################################################################

class GrapheNO:
	"""graphe code par liste d'adjacence. Les sommets devront etre numerotes 0,1,...,n-1"""

	def __init__(self, l_adj):
		"""initialise un graphe d'apres la liste d'adjacence l_adj""" 

		self.ordre = len(l_adj) # attribut ordre = nb de sommets
		self.adj = l_adj        # attribut liste adjacence

	def affiche(self):
		"""affiche des infos sur le graphe"""
		print "Ordre du graphe :", self.ordre
		for v in range(self.ordre):
			print "voisins de ", v, " ->", self.adj[v]

	def __str__(self):
		"""permet de faire un print sur le graphe"""
		s = "Ordre du graphe : " + str(self.ordre) + "\n"
		s += "Taille du graphe : " + str(self.taille()) + "\n"
		for v in range(self.ordre):
			s += "voisins de " + str(v) + " -> " + str(self.adj[v]) + "\n"
		return s

	def degre(self, v):
		"""renvoie le degré du sommet v"""
		return len( self.adj[v] )

	def taille(self):
		"""renvoie la taille du graphe"""
		somme = 0
		for v in range(self.ordre):
			somme += self.degre(v)
		return somme/2

	###########################################################################
	# La méthode bipartition_valide de la question 2, à compléter
	###########################################################################

	def bipartition_valide(self, A, B):
		"""renvoie un booléen qui indique si A et B forment
		une bipartition valide du graphe"""
		adjacencesA = []
		adjacencesB = []
		for i in range(len(self.adj)):
		  if i%2==0:
		      adjacencesA.append(self.adj[i])
		for i in range(1, len(self.adj)):
		  if i%2!=0:
		      adjacencesB.append(self.adj[i])
		for i in A:
		  for j in adjacencesA:
		    if i in j:
		      return False
		for i in B:
		  for j in adjacencesB:
		    if i in j:
		      return False
		return True


	###########################################################################
	# La méthode est_biparti de la question 3, à compléter
	###########################################################################

	def est_biparti(self):
		"""renvoie False si le graphe n'est pas biparti ou
		un couple [A,B] formant une bipartition s'il l'est"""
		A = []
		B = []
		sommetsA = []
		sommetsB = []
		for i in self.adj:
			if self.adj.index(i)%2==0:
			  sommetsA.append(i)
			if self.adj.index(i)%2!=0:
			  sommetsB.append(i)
		for i in sommetsA:
		  A.append(i[1]-1)
		for i in sommetsB:
		  B.append(i[0]+1)
		if self.bipartition_valide(A, B):
		  return A, B
		return False


###############################################################################
# Constructeurs de graphes
###############################################################################

def cycle(n):
    """"renvoie un GrapheNO pour le cycle a n sommets"""

    #crée la liste d'adjacence d'un cycle à n sommets
    ladj = []
    ladj.append( [n-1,1] )
    for i in range(1,n-1):
        ladj.append( [i-1, i+1] )
    ladj.append( [n-2, 0])

    #on renvoie le graphe correspondant
    return GrapheNO( ladj )

###############################################################################
# Lecture de graphes dans fichier et conversions
###############################################################################

def aretes_vers_liste_adj(lar, ordre):
    """renvoie une liste d'adjacence créée à partir
    de la liste d'aretes lar"""

    ladj = [ [] for i in range(ordre)]
    for arete in lar:
        sommet1 = arete[0]
        sommet2 = arete[1]
        ladj[sommet1].append(sommet2)
        ladj[sommet2].append(sommet1)
    return ladj


def lireAretesEtOrdre(nomdufichier):
    """lit le fichier et renvoie la liste des aretes qui s'y trouvent
    ainsi que l'ordre"""
    f = file(nomdufichier, 'r')
    lignes = f.readlines()
    #on extrait les lignes qui commencent par 'E' 
    #si c'est bon on cree une nouvelle arete
    aretes = []
    ordre = 0
    for l in lignes:
        mots = l.split()
        if len(mots) >= 3 and mots[0]=='E':
            aretes.append([int(mots[1]), int(mots[2])])  #ATTENTION ne pas oublier la conversion str en int
        if len(mots) > 0 and mots[0]=="ordre":
            ordre = int(mots[1])
    return aretes, ordre


def lireGrapheNO(nomfichier):
    """lit le fichier et renvoie le GrapheNO correpondant"""

    aretes, ordre = lireAretesEtOrdre(nomfichier)
    adj = aretes_vers_liste_adj(aretes, ordre)
    return GrapheNO(adj)

###############################################################################
# Question 1 : méthode qui renvoie un graphe biparti complet
###############################################################################

def grapheBipartiComplet(p,q):
	"""renvoie un graphe biparti complet GrapheNO"""
	sommetsEst = []
	sommetsOuest = []
	lesAretes = []
	alphaAretes = []
	for i in range(p):
		sommetsEst.append(i)
	for i in range(p, q+p):
		sommetsOuest.append(i)
	for i in range(p+q):
		lesAretes.append([i])
		for j in range(len(lesAretes[i])):
			if lesAretes[i][j] in sommetsEst:
				lesAretes[i].append(sommetsOuest)
			if lesAretes[i][j] not in sommetsEst:
				lesAretes[i].append(sommetsEst)
	
	for i in range(len(lesAretes)):
		lesAretes[i] = lesAretes[i][1]
	
	return GrapheNO(lesAretes)


###############################################################################
# Tests des questions 1, 2 et 3
###############################################################################

#Question 1
g = grapheBipartiComplet(3,5)
if g==None:
    print "Question 1 non traitée"
else:
    print g

#Question 2
#test sur un cycle à 10 sommets
print "\n"+"*"*30
g = cycle(10)
A = [0,2,4,6,8]
B = [1,3,5,7,9]
res = g.bipartition_valide(A,B)
if res==None:
	print "Question 2 non traitée"
else:
	print res
	#test sur un cycle à 11 sommets
	g = cycle(11)
	A = [0,2,4,6,8,10]
	B = [1,3,5,7,9]
	res = g.bipartition_valide(A,B)
	print res

#Question 3
print "\n"+"*"*30
#test sur un cycle à 10 sommets
g = cycle(10)
res = g.est_biparti()
if res==None:
    print "Question 3 non traitée"
else:
    print res
    #test sur un cycle à 11 sommets
    g = cycle(11)
    res = g.est_biparti()
    print res
