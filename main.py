from veiculo import Veiculo
from carro import Carro

objveiculo1 = Veiculo('Rosa',6,'Chefrolet',200)

print('Marca '+ objveiculo1.marca +' Tanque ' + str(objveiculo1.tanque))

objveiculo1.abastecer(33)

print('Marca '+ objveiculo1.marca +' Tanque ' + str(objveiculo1.tanque))

objcarro1 = Carro('Preto',4,'Fiat',45)

print('Marca '+ objcarro1.marca +' Tanque ' + str(objcarro1.tanque))

objcarro1.abastecer(30)
print('Marca '+ objcarro1.marca +' Tanque ' + str(objcarro1.tanque))
