def verificar_data(data):
    dia = int(data.split('/')[0])
    mes = int(data.split('/')[1])
    ano = int(data.split('/')[2])
    if dia <= 0 or dia > 31:
        return False
    if mes < 1900 or ano > 2025:
        return False
    return True

def verificar_cpf(cpf:str):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if len(cpf) == 11:
        return True
    else:
        return False
