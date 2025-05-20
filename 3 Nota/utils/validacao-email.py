def validacao_email():
    caracteres_proibidos = ['#', '!', '%', '&', '*']
    email_invalido = any(proibido in email for proibido in caracteres_proibidos)

    validacao_email()