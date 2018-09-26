# -*- coding: utf-8 -*-

import os, sys
import Tkinter as tk
import tkFont
from saisie import *

"""
********************************************************
*													   *
*			Créé par Yohann MARTIN, 2017/2018		   *
*				DUT Informatique de Vélizy			   *
*													   *
********************************************************
"""

class TreeDrawer(object):

	def __init__(self):
		self.root = tk.Tk()
		self.nbTree = 0

		# La taille d'un noeud (cercle) en pixels
		self.TAILLE_NOEUD = 30
		# Le nombre de pixels de décalage entre un noeud et ses fils
		self.DIMI_OFFSET = 50
		self.FONT = None

	# Permet de calculer la hauteur d'un arbre binaire
	def calcul_hauteur_arbre(self, a):
		if(a == None):
			return -1
		else:
			h_g = self.calcul_hauteur_arbre(a.G)
			h_d = self.calcul_hauteur_arbre(a.D)
			return 1 + max(h_g, h_d)

	# Retourne le nombre de noeuds pour un niveau donné dans un arbre binaire complet
	def calcul_nb_noeud_niveau(self, k):
		return (2**(k-1))

	# Permet d'obtenir le pixel sur l'axe X qui est au centre d'un noeud
	def get_center_noeud(self, noeud_debut, noeud_largeur, text_size):
		return noeud_debut + ((noeud_largeur - noeud_debut - text_size) / 2)

	# Permet de calculer l'indice de l'axe X pour un noeud d'un niveau
	def calcul_indiceX(self, i, niveau):
		return float((2. * i + 1.) / (2.**niveau))

	# Permet de calculer les indices des coins haut/gauche et bas/droit pour un noeud
	def calcul_indice(self, indice, indiceX, niveau):
		return [indice[0] * indiceX - (self.TAILLE_NOEUD / 2), (indice[1] * niveau) + self.DIMI_OFFSET * niveau, indice[0] * indiceX + (self.TAILLE_NOEUD / 2), (indice[1] * niveau) + self.TAILLE_NOEUD + (self.DIMI_OFFSET * niveau)]

	# Permet de dessiner l'arbre à partir d'un parcours en profondeur (récursivité)
	def dessiner(self, canvas, a, indice, niveau, i):
		if(a != None):
			# La longueur & largeur du texte va nous permettre de centrer la valeur du noeud
			(textWidth, textHeight) = (self.FONT.measure(a.val),self.FONT.metrics("linespace"))

			# On calcul l'indice pixel sur l'axe X du noeud courant
			IndiceX = self.calcul_indiceX(i, niveau)

			# On calcul le reste des indices du noeud
			calculIndice = self.calcul_indice(indice, IndiceX, niveau)

			# On dessine le cercle aux indices donnés
			canvas.create_oval(calculIndice[0], calculIndice[1], calculIndice[2], calculIndice[3], outline ='black')
			# Puis on dessine le texte au milieu
			canvas.create_text(self.get_center_noeud(calculIndice[0], calculIndice[2], textWidth), self.get_center_noeud(calculIndice[1], calculIndice[3], textHeight), text = a.val, font = self.FONT, fill = 'black', anchor= 'nw')

			# On dessine ensuite les enfants gauche et droite
			self.dessiner(canvas, a.G, indice, niveau+1, i*2)
			self.dessiner(canvas, a.D, indice, niveau+1, (i*2)+1)

			# Si on à un fils gauche, on calcul ses indices pour dessiner une ligne entre le noeud courant et son fils
			if(a.G != None):
				filsGIndice = self.calcul_indice(indice, self.calcul_indiceX(i*2, niveau+1), niveau+1)
				canvas.create_line(self.get_center_noeud(filsGIndice[0], filsGIndice[2], 0), filsGIndice[1], self.get_center_noeud(calculIndice[0], calculIndice[2], 0), calculIndice[3], fill = 'black')
			# De même pour le fils droit
			if(a.D != None):
				filsDIndice = self.calcul_indice(indice, self.calcul_indiceX((i*2)+1, niveau+1), niveau+1)
				canvas.create_line(self.get_center_noeud(filsDIndice[0], filsDIndice[2], 0), filsDIndice[1], self.get_center_noeud(calculIndice[0], calculIndice[2], 0), calculIndice[3], fill = 'black')

	def dessiner_arbre(self, a):
		# On créé une nouvelle fenêtre graphique
		image_Largeur = (self.calcul_nb_noeud_niveau(self.calcul_hauteur_arbre(a) + 1) * self.TAILLE_NOEUD) * 2
		image_Hauteur = ((self.calcul_hauteur_arbre(a) + 1 + 1) * (self.TAILLE_NOEUD + self.DIMI_OFFSET))

		if(image_Largeur < 500):
			image_Largeur = 500
		if(image_Hauteur > 1000):
			image_Hauteur = 1000

		self.FONT = tkFont.Font(family='Arial', size=-(self.TAILLE_NOEUD - 10))

		fenetre = tk.Frame(self.root)
		fenetre.pack()
		if(self.nbTree > 0):
			fenetre = tk.Toplevel(fenetre)
			fenetre.title("Arbre n°" + str(self.nbTree+1))
		else:
			self.root.title("Arbre n°" + str(self.nbTree+1))
		canvas = tk.Canvas(fenetre, width=image_Largeur, height=image_Hauteur)
		canvas.pack()
		self.nbTree += 1
		# On dessine notre arbre
		self.dessiner(canvas, a, [image_Largeur, 20], 1, 0)

	# On attend la fermeture des fenêtres avant de continuer
	def wait(self):
		tk.mainloop()

# Cette partie n'est exécutée que si l'on lance le script directement, et non dans les import
if __name__ == "__main__":

	treeDrawer = TreeDrawer()
	# On demande à rentrer un arbre (saisie classique en console, se référer au fichier saisie.py)
	print "Entrez un arbre:"
	arbre = entrerArbre(1)

	treeDrawer.dessiner_arbre(arbre)

	print "Entrez un arbre:"
	arbre2 = entrerArbre(1)
	treeDrawer.dessiner_arbre(arbre2)

	print "Entrez un arbre:"
	arbre3 = entrerArbre(1)
	treeDrawer.dessiner_arbre(arbre3)

	# On attend la fermeture des fenêtres avant de terminer le programme
	treeDrawer.wait()
