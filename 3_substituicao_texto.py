# 3. Substituição de Texto:
# Substitua palavras ou padrões específicos em um texto por outras palavras ou padrões.

# Exemplo: Substituir palavras específicas em um texto

import re

texto = "O gato está no telhado."

padrao = r'\b(gato)\b'

novo_texto = re.sub(padrao, 'cachorro', texto)
print(novo_texto)  # "O cachorro está no telhado."