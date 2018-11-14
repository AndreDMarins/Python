nomes = ["Andre","Milena","julia","Anne","Muri"]


for nome in nomes:
    print(nome)


listaNumeros = range(5)

for i in listaNumeros:
    print(i)

listaDois = range(50,100,2) #mostra do 3 ao 100 passo 2
for i in listaDois:
        print (i)

for i in range(5): #não é a melhor alternatira
    print(nomes[i])

for i in range(len(nomes)):
    nomes.append("Oia")
    print(nomes[i])


print(nomes)

teste = '12345678'

for i in teste:
    print(i)


i=0
while i<=10:
    print('I ainda é menor que 10',i)
    i=i+1


#EXERCICIO CRIA LISTA DE CONVIDADOS E IMPRIME NO FINAL

pessoa='a'
convidados = []


while pessoa !='':
    pessoa = input('Qual o nome do convidado?  ')
    convidados.append(pessoa)

print(convidados)