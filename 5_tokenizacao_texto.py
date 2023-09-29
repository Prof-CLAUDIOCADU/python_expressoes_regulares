# 5. Tokenização de Texto:
# Divida o texto em tokens com base em padrões específicos, como palavras, frases, pontuação, etc.

# Exemplo: Tokenização de palavras em uma frase

import re

frase = "Expressões regulares são úteis no processamento de texto."

tokens = re.split(r'\s', frase)
print(tokens)  # ['Expressões', 'regulares', 'são', 'úteis', 'no', 'processamento', 'de', 'texto.']