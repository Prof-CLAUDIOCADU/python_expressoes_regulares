# 1. Validação de Entrada de Usuário:
# Utilize expressões regulares para validar entradas de usuário, como e-mails, números de telefone, datas, senhas, etc.

# Exemplo: Validar um endereço de e-mail

import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))

print(validar_email('exemplo@email'))  # True
print(validar_email('invalido@exemplo'))    # False