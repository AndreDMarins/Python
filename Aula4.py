
frase = 'Oi, tudo bem?'

print(frase)

listaNomes = ['João','Andre','Maria','Brutus','Popyie','Olivia','Palito']

print(type(listaNomes))

print(listaNomes[0])

print(listaNomes)

#imprime o caracter da poição 4 da String frase
print(frase[4])

#imprime o caracter da posição 4 até a posição 20
print(frase[4:20])

#imprime os caracteres de 1 a 15 pulando de 2 em 2
print(frase[0:15:2])

print(listaNomes[0:6:2])

#com o indice negativo, começa imprimir a partir do ultimo item
print(listaNomes[-2])

print(frase[::-1])

#inserir item na lista
listaNomes.append('Geralda')

print(listaNomes)

listaNomes.remove('João')

print(listaNomes)

listaNomes.insert(1,'Milena')

print(listaNomes)

listaNomes[1] = 'Milenão'

print(listaNomes)

contador = listaNomes.count('Milenão')

print(contador)

print(len(listaNomes))

print(frase.lower())
print(frase.upper())

nome = 'Isabel Cristina Leopoldina Augusta Micaela Gabriela Rafaela Gonzaga de Bourbon-Duas Sicílias e Bragança'

print(nome)

nomeSepadaro = nome.split(' ')
print(nomeSepadaro)

texto = 'Multiverso é um termo usado para descrever o conjunto hipotético de universos possíveis, incluindo o universo em que vivemos. Juntos, esses universos compreendem tudo o que existe: a totalidade do espaço, do tempo, da matéria, da energia e das leis e constantes físicas que os descrevem. É geralmente usado em enredos de ficção científica, mas também é uma extrapolação possível de algumas teorias científicas para descrever um grupo de universos que estão relacionados, os denominados universos paralelos. A ideia de que o universo que se pode observar é só uma parte da realidade física deu luz à definição do conceito multiverso'

texto = texto.split(' ')

print(texto)
