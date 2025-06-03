import utils

data_narcer = input('digite sua data de nascimento no padrão BR:')
while not utils.verificar_data(data_narcer):
    print('data informada com sucesso!')
    data_narcer = input('digite sua data de nascimento no padrão BR:')

nome = input('digite seu nome')