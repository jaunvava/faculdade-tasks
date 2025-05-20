import random

def gerar_id(lista_ids:list):
    num = random.randint(0,999999)
    while lista_ids.count(num) > 0:
        num = random.randint(0, 9999999)
    return num

