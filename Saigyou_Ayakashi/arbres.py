#coding: utf-8

import os
from affiche_arbre import *
from affiche_arbre import TreeDrawer

def parcoursProfondeur(arbre):
	nombreVisites = [[]]
	nombreVisites[0].append(1)
	saigyou = []
	print nombreVisites
	if arbre != None:
		parcourir(arbre.gauche, saigyou)
		parcourir(arbre.droite, saigyou)
		return saigyou


def parcourirArbre(arbre):
	


def verificationArbre(arbre):
	



cerisier = entrerArbre(0)

treeDrawer = TreeDrawer()
treeDrawer.dessiner_arbre(cerisier)

parcoursProfondeur(cerisier)


treeDrawer.wait()
