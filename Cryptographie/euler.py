#coding: utf-8
import os

os.system('clear')

def is_prime(x, tab=[2]):
	for i in range(tab[len(tab)-1], x-1):
		if(x%i == 0):
			return False
	return True

def decomP(n, i=2, tab=[2]):
	if n==1:
		return tab[1:]
	if(is_prime(i, tab)):
		if(n%i==0):
			tab.append(i)
			return decomP(n/i, i, tab)
		else:
			return decomP(n, i+1, tab)
	else:
		return decomP(n, i+1, tab)


def euler(n, tab):
	index = []
	resultat = 1
	i = 0
	while i<len(tab):											#Création tableau du nombre d'occurrences
		index.append(tab.count(tab[i]))
		i += tab.count(tab[i])
	tab = list(set(tab))
	for i in range(len(index)):
		resultat *= pow(tab[i], index[i]) - pow(tab[i], index[i]-1)
	return resultat

def congruence(x, n):
	return x%n

def euclide2(a, b, x=-100, y=-100):
	for x in range(-100, 100):
		for y in range(-100, 100):
			if((a * x + b * y) == 1):
				tab = []
				tab.append(x)
				tab.append(y)
				return tab
	tab = []
	tab.append(x)
	tab.append(y)
	return tab

def euclide(a, b, tab=[]):
	if(b == 1):
		return tab
	else:
		tab.append([])
		tab[len(tab)-1].append(a)
		tab[len(tab)-1].append(b)
		tab[len(tab)-1].append(a//b)
		tab[len(tab)-1].append(a%b)
		return euclide(b, a%b, tab)



#n = int(input("Entrez un nombre: "))
#tab = decomP(n)
#print tab


#laEuler = euler(n, tab)
#print laEuler


a = int(input("a: "))
b = int(input("b: "))
d = euclide(a, b)
d = d[::-1]
print "n =", len(d)
print d
tab = euclide2(a, b)
print tab






