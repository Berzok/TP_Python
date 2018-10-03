#coding: utf-8

import os
from affiche_arbre import *
from affiche_arbre import TreeDrawer

def parcoursProfondeur(arbre):
	if arbre != None:
		parcourir(arbre.gauche, saigyou)
		parcourir(arbre.droite, saigyou)
		return saigyou

def prefixe(arbre):
	if arbre != None:
		flower_viewing_event(arbre)
		prefixe(arbre.G)
		prefixe(arbre.D)


def symetrique(arbre):
	if arbre != None:
		symetrique(arbre.G)
		flower_viewing_event(arbre)
		symetrique(arbre.D)


def flower_viewing_event(arbre):
	print arbre.val,



cerisier = entrerArbre(0)

treeDrawer = TreeDrawer()
treeDrawer.dessiner_arbre(cerisier)
treeDrawer.wait()

prefixe(cerisier)



