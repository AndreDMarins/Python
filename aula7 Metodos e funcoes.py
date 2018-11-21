'''
print('Hello word')

print(len('Hello word'))


def soma(numero1,numero2):
    resp = numero1+numero2
    return resp


retorno = soma(10,1287)
print(retorno)

num1 = input('qual o numero 1')
num2 = input('qual o numero 2')

retorno = soma(int(num1),int(num2))

print(retorno)


def tem7itens(maiorquesete):
    if len(maiorquesete)==7:
        return True
    else:
        return False

maiorzao = input('Palavra')

print(tem7itens(maiorzao))

'''

#Escreva uma função que recebe um objeto de coleção e
# retorna o valor do maior numero dentro dessa coleção

num='a'
numeros = []


while num !=0:
    num = int(input('Digite um numero'))
    if num!=0:
        numeros.append(num)

print(numeros)
print (len(numeros))
maior = 0
i=0

for i in numeros:
    print(i)
    if maior < i:
        maior = i


print('O maior numero é: ',maior)
