# 2. Extração de Informações:
# Extraia informações específicas de um texto, como números de telefone, endereços, IDs, etc.

# Exemplo: Extrair números de telefone de um texto

import re

texto = "Meu número é (123) 456-7890 e o outro é (987) 654-3210."

padrao = r'\(\d{3}\) \d{3}-\d{4}'

numeros_telefone = re.findall(padrao, texto)
print(numeros_telefone)  # ['(123) 456-7890', '(987) 654-3210']