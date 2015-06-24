import sys

def cifrar():
	#nessa função o alfato é a lista de letras na sequencia "tradicional" que conhecemos
	if len( sys.argv ) < 4:
		print("Entre com uma chave (letra) e uma palavra para ser cifrada (sem espaços)")
		sys.exit()

	chave    = sys.argv[2].lower()
	palavra  = sys.argv[3].lower()

	#criei o alfabeto usando a função chr para não usar a dependência da lib "string"
	alfabeto                = list( map( chr, range( 97, 123 ) ) )
	asciiChave              = ord( chave )
	alfabetoModificado      = []
	palavraCifrada          = ""

	for i in range ( asciiChave, 123 ):
	        alfabetoModificado.append( chr( i ) )
	for i in range ( 97,asciiChave ):
		alfabetoModificado.append( chr( i ) )
	for i in palavra:
	        palavraCifrada += alfabetoModificado[ alfabeto.index( i ) ]
	print(palavraCifrada)

def descifrar():
	#nessa função o alfabeto é a lista de letra na sequecia em "função" da chave escolhida
	if len( sys.argv ) < 4:
		print("Entre com uma chave (letra) e uma palavra para ser descifrada (sem espaços)")
		sys.exit()
	chave    = sys.argv[2].lower()
	palavra  = sys.argv[3].lower()

	#criei o alfabeto usando a função chr para não usar a dependência da lib "string"
	alfabeto                = []
	asciiChave              = ord( chave )
	alfabetoModificado      = list( map( chr, range( 97, 123 ) ) )
	palavraCifrada          = ""

	for i in range ( asciiChave, 123 ):
		alfabeto.append( chr( i ) )
	for i in range ( 97,asciiChave ):
		alfabeto.append( chr( i ) )
	for i in palavra:
		palavraCifrada += alfabetoModificado[ alfabeto.index( i ) ]
	print(palavraCifrada)

def menuEncontrarChave():
	pass

opcoes = { 1:cifrar, 2:descifrar, 3:menuEncontrarChave }
def menu( opcao ):
	try:
		opcoes[opcao]()
	except KeyError:
		print( "opção errada" )
if len( sys.argv ) >= 2:
	menu( int( sys.argv[1] ) )
else:
	print("Informe a opção desejada")
