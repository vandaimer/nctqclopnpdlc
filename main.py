#!/bin/python3
import sys

chave 	 = sys.argv[1].lower()
word	 = sys.argv[2].lower()

original = list( map( chr, range( 97, 123 ) ) )
letra	 = ord(chave)
fic	 = []
cript	 = ""

for i in range (letra, 123):
	fic.append(chr(i))
for i in range (97,letra):
	fic.append(chr(i))
for i in word:
	cript += fic[original.index(i)]
print(cript)
