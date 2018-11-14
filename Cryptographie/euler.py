#coding: utf-8
import os
from collections import Counter

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
	value = 0
	index = []
	cnt = Counter(tab)
	cnt = cnt.items()
	print cnt[2][1]
	for i in tab:
		pass
	print index
	return None




n = int(input("Entrez un nombre: "))
tab = decomP(n)
print tab


laEuler = euler(n, tab)
print laEuler











