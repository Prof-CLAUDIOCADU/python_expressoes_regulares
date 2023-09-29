# 7. Transformação de Dados:
# Manipule e transforme dados com base em padrões, como formatação de texto, limpeza de dados, etc.

# Exemplo: Padronizar números de telefone

import re

numeros_telefone = ['123-456-7890', '(987) 654-3210', '555.123.4567']

padrao = r'\D'  # Remove não dígitos

telefones_padronizados = [re.sub(padrao, '', telefone) for telefone in numeros_telefone]
print(telefones_padronizados)  # ['1234567890', '9876543210', '5551234567']