
'''
try:
    div0 = 2/a
except ZeroDivisionError:
    print('Divisão por zero')

except NameError:
    print('Você digitou algo errado')

except Exception as erro:
    print('Ocorreu o seguinte erro: ', erro)
'''
import time


def abreArquivo():
    try:
        arquivo = open('arquivoteste.txt')
        return True
    except Exception as erro:
        print('Houve o segujnte erro: ',erro)
        return False

while not abreArquivo():
    print('tentando abrir arquivo')
    time.sleep(5)

print('Arquivo aberto')