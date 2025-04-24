#faça um sistema que mostra a tabuada da multiplicação do 1 até ao 9, use um for dentro do outro for

for numero in range(1,10):
    for i in range(1, 10):
        print(f'{numero} x {i} = {numero+i}')
    