
var_verdade = True #dado tipo boleano
var_false = False

print(type(var_false)), print(type(var_verdade))

print(var_false)

if var_verdade == True:
	print('Var_verdade é verdadeiro')
	
print ('Menu: \n1 - Escreve Guilherme\n2 - Escreve André')
opcao = input('Escolha uma opção: ')

if opcao == '1':
	print('Guilherme')
elif opcao =='2': #elif é a mesma coisa que Else if
	print('André')
else:
	print('Opção errada')
	
