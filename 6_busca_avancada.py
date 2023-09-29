# 6. Busca Avançada:
# Realize buscas em documentos ou bases de dados usando padrões complexos para encontrar informações específicas.

# Exemplo: Buscar nomes de arquivos que seguem um padrão

import re

arquivos = ['documento123.txt', 'relatorio_final.pdf', 'imagem.jpg', 'planilha.xls']

padrao = r'\w+\.(txt|pdf)'

arquivos_selecionados = [arquivo for arquivo in arquivos if re.match(padrao, arquivo)]
print(arquivos_selecionados)  # ['documento123.txt', 'relatorio_final.pdf']