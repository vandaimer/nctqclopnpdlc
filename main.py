import sys

chave 	 = sys.argv[1].lower()
palavra	 = sys.argv[2].lower()

#criei o alfabeto usando a função map para não usar a dependência da lib "string"
alfabeto		= list( map( chr, range( 97, 123 ) ) )
asciiChave		= ord( chave )
alfabetoModificado	= []
palavraCifrada		= ""

for i in range ( asciiChave, 123 ):
	alfabetoModificado.append( chr( i ) )
for i in range ( 97,asciiChave ):
	alfabetoModificado.append( chr( i ) )
for i in palavra:
	palavraCifrada += alfabetoModificado[ alfabeto.index( i ) ]
print(palavraCifrada)
