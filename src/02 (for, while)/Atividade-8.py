
nome = input('digite seu nome:')
while(len(nome) <= 3):
    nome = input('digite seu nome:')


idade = int(input('digite sua idade:'))
while idade < 0 or idade > 150:
    idade = int(input('digite sua idade'))


salario = float(input('digite seu salario'))
while salario <= 0:
    salario = float(input('qual o seu salario'))


estado = (input('digite seu estado civil:'))
while estado != 's' or estado != 'c' or estado != 'd' or estado != 'y':
    estado = input('digite seu estado civil')
