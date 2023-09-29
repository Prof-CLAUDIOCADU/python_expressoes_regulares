# 4. Análise de Log:
# Analise logs ou arquivos de texto para extrair informações relevantes, como erros, URLs, endereços IP, etc.

# Exemplo: Extrair URLs de um log

import re

log = "Erro ao acessar http://exemplo.com/pagina. Erro 404. Mais info em http://exemplo.com/erro404."

padrao = r'https?://\S+'

urls = re.findall(padrao, log)
print(urls)  # ['http://exemplo.com/pagina', 'http://exemplo.com/erro404']