#coding: utf-8
import os

os.system('clear')


class GrapheNO:
	def __init__(self, l_adj):
		self.ordre = len(l_adj)
		self.adj = l_adj
	def affiche(self):
		print "Le graphe est d'ordre:", self.ordre
		letruc = len(self.adj)
		for i in range(letruc):
			print "Adjacences sommet", i+1, ":", self.adj[i]
	def degre(self, leSommet):
		return len(self.adj[leSommet])
	def taille(self):
		laTaille = 0
		for i in range(len(self.adj)):
			laTaille +=len((self.adj[i]))
		return laTaille/2
	def composantesConnexe(self, i):
		
		laListe = []
		laListe.append(i)
		

def grapheComplet(n):
	laListe = []
	laListe3 = []
	for i in range(1, 1001):
		laListe3.append(i)
	for i in range(n):
		laListe.append([])
	for i in range(len(laListe)):
		laListe[i] += (laListe3[:n])
		laListe[i].remove(i+1)
	unGraphe = GrapheNO(laListe)
	return unGraphe

def cycle(n):
	laListe = []
	laListe2 = [n, 2]
	laListe.append(laListe2)
	laListe2 = [1, 3]
	for i in range(n):
		laListe.append([])
	for i in range(1, len(laListe)):
		if i == n-1:
			laListe2 = [laListe2[0]+1, 1]
			laListe[i] += laListe2
			laListe.pop(len(laListe)-1)
			break
		laListe[i] += (laListe2[::])
		laListe2[0] += 1
		laListe2[1] += 1
	unGraphe = GrapheNO(laListe)
	return unGraphe

def aretes_vers_liste_adj(aretes, n):
	laListe = []
	listeCommuns = []
	for i in range(len(aretes)):
		laListe.append([])
		for j in range(len(aretes)):
			for k in range(len(aretes[j])):
				laListe[i].append(aretes[j][k])
		try:
			laListe[i].remove(i+1)
		except:
			pass
	for i in range(len(laListe)):
		laListe2 = set(laListe[i])
		laListe2 = list(laListe2)
		laListe2.sort()
		laListe[i] = laListe2
		if(i+1 in laListe[i]):
			try:
				laListe[i].remove(i+1)
			except:
				pass
	return laListe

def lire_aretes(nomdufichier):
	lesAretes = []
	f = file(nomdufichier, 'r')
	lesLignes = f.readlines()
	for i in lesLignes:
		if "#" in i:
			lesLignes.remove(i)
			continue
		if i == "\n":
			lesLignes.remove(i)
			continue
		if "E" in i:
			lesAretes.append(i)
			continue
	print ""
	longueurAretes = len(lesAretes)
	for i in range(longueurAretes):
		uneArete = (lesAretes[i].split()[1:])
		uneArete[0] = int(uneArete[0])
		uneArete[1] = int(uneArete[1])
		print uneArete, "i=", i
		lesAretes.append(uneArete)
	for i in range(len(lesAretes)):
		print lesAretes[i]
	return lesAretes

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
	
print ""
liste = [[1, 2], [2, 3], [3, 1]]
leGraphe = GrapheNO(liste)
leGraphe.affiche()
print ""
print ""
sommetChoisi = int(input("Choisissez un sommet...     "))
print "Le sommet", sommetChoisi, "est d'ordre", leGraphe.degre(sommetChoisi)
print "Le graphe est de taille", leGraphe.taille()
print ""
print ""
print "On va créer un autre graphe complet"
leGraphe2 = grapheComplet(int(input("Taille du graphe à constr8re: ")))
leGraphe2.affiche()
print ""
print ""
print "On va créer un cycle"
leGraphe3 = cycle(int(input("Taille du cycle à constr8re: ")))
leGraphe3.affiche()
print ""
print ""
print "On va constr8re la liste d'adjacences d'un graphe à partir de ses arêtes et\nde son ordre"
adjacence4 = aretes_vers_liste_adj([[1, 2], [1, 3], [2, 3], [1, 4]], 4)
print "La liste d'adjacences est: ", adjacence4
print ""
print ""
print "On va créer un graphe à partir d'un fichier"
liste, ordre = lireAretesEtOrdre("petitgraphe.txt")
leGraphe4 = GrapheNO(aretes_vers_liste_adj(liste, ordre))
print ""
print ""
print "On va à nouveau créer un graphe à partir d'un fichier"
liste = lire_aretes("petitgraphe.txt")
print ""

