times = {'flamengo':23, 'sousa':24, 'vasco':25, 'joao':26}

lista_del = []

auxiliar = dict()

for time in times.keys():
    print(times, ' - ', times[time])
    if times[time] % 2 != 0:
        auxiliar[time] = times[time]
    
del times
# função del serve para deletar manualmente variaveis e indices e dicionarios 

print('sobrou:')
print(auxiliar)

