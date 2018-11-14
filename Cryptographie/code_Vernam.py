#coding: utf-8

import os

os.system('clear')



def chiffrer(phrase):
	message = []
	phrase = list(phrase)
	clef = bin(3)
	for i in range(len(phrase)):
		phrase[i] = bin(ord(phrase[i]))
	for i in phrase:
		message.append(clef + i)
	print message

message = raw_input("Entrez un message à chiffrer: ")
message = str(message)

chiffrer(message)
