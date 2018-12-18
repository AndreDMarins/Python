##abrindo e escrevendo
texto = open('arquivo.txt','w')

texto.write('Vamos escrever algo\n')

for i in range(1,10):
    texto.write('andre '+ str(i)+'\n')

##abrindo e lendo
texto = open('arquivo.txt','r')

print(texto.read())