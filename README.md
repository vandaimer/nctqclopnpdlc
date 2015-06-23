# nctqclopnpdlc ou CifraDeCesar
Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de César ou troca de César, é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, A seria substituído por D, B se tornaria E, e assim por diante. O nome do método é em homenagem a Júlio César, que o usou para se comunicar com os seus generais.

Fonte do resumo: https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar

Fonte onde aprendi o algoritmo: https://www.youtube.com/watch?v=wtwlVqEoyyw

##Como funciona

+ 1º - Temos uma lista de letras não repetidas do alfabeto e em sequencia
+ 2º - Precisamos escolher uma dessas letras como "chave", por exemplo a letra "g"
+ 3º - Agora criamos uma nova lista de letras não repetidas do alfabeto, definindo a primera posição da lista como nossa chave, a segunda posição segue a sequencia, que neste caso é "h", até chegar em "z"
+ 4º - Precisamos terminar de preencher a segunda lista, pois no nosso exemplo partimos do "g" até "z", então só adicionamos 19 letras, se não falha minha conta.
+ 5º - Agora iniciamos da letra "a" até a letra "f", para fechar as 26 letras
+ 6º - Escolher a palavra para ser cifrada ( palavra sem espaço ), exemplo "codigo"
+ 7º - Para cada letra dessa palavra, vamos pegar o inidice dela na lista do alfabeto original ( que incia em "a" ), no nosso caso a primera letra é "g", então o indice é 2
+ 8º - Com o indice em "mãos" vamos pegar a letra do indice 2 do alfabeto que iniciou com nossa chave, como o "g" é a primeira letra tem indice zero, a letra "i" corresponde ao indice 2.
+ 9º - As linha 7 até 8 se repentem até acabar as letras, então a palavra está cifrada

 <code>python3 ./main.py qualquerfrase</code>

Ainda preciso melhorar o código e implementar a decrifragem, então no momento está somente cifrando.
