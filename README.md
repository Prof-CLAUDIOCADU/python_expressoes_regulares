## Utilização de Expressões Regulares em Python

As expressões regulares (regex) são sequências de caracteres que definem um padrão de busca. Elas são poderosas ferramentas para manipulação e validação de strings em Python.

### 1. **Validação de Entrada de Usuário:**

Utilize expressões regulares para validar entradas de usuário, como e-mails, números de telefone, datas, senhas, etc.

#### Exemplo: Validar um endereço de e-mail
```python
import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))

print(validar_email('exemplo@email.com'))  # True
print(validar_email('invalido@exemplo'))    # False
```

### 2. **Extração de Informações:**

Extraia informações específicas de um texto, como números de telefone, endereços, IDs, etc.

#### Exemplo: Extrair números de telefone de um texto
```python
import re

texto = "Meu número é (123) 456-7890 e o outro é (987) 654-3210."

padrao = r'\(\d{3}\) \d{3}-\d{4}'

numeros_telefone = re.findall(padrao, texto)
print(numeros_telefone)  # ['(123) 456-7890', '(987) 654-3210']
```

### 3. **Substituição de Texto:**

Substitua palavras ou padrões específicos em um texto por outras palavras ou padrões.

#### Exemplo: Substituir palavras específicas em um texto
```python
import re

texto = "O gato está no telhado."

padrao = r'\b(gato)\b'

novo_texto = re.sub(padrao, 'cachorro', texto)
print(novo_texto)  # "O cachorro está no telhado."
```

### 4. **Análise de Log:**

Analise logs ou arquivos de texto para extrair informações relevantes, como erros, URLs, endereços IP, etc.

#### Exemplo: Extrair URLs de um log
```python
import re

log = "Erro ao acessar http://exemplo.com/pagina. Erro 404. Mais info em http://exemplo.com/erro404."

padrao = r'https?://\S+'

urls = re.findall(padrao, log)
print(urls)  # ['http://exemplo.com/pagina', 'http://exemplo.com/erro404']
```

### 5. **Tokenização de Texto:**

Divida o texto em tokens com base em padrões específicos, como palavras, frases, pontuação, etc.

#### Exemplo: Tokenização de palavras em uma frase
```python
import re

frase = "Expressões regulares são úteis no processamento de texto."

tokens = re.split(r'\s', frase)
print(tokens)  # ['Expressões', 'regulares', 'são', 'úteis', 'no', 'processamento', 'de', 'texto.']
```

### 6. **Busca Avançada:**

Realize buscas em documentos ou bases de dados usando padrões complexos para encontrar informações específicas.

#### Exemplo: Buscar nomes de arquivos que seguem um padrão
```python
import re

arquivos = ['documento123.txt', 'relatorio_final.pdf', 'imagem.jpg', 'planilha.xls']

padrao = r'\w+\.(txt|pdf)'

arquivos_selecionados = [arquivo for arquivo in arquivos if re.match(padrao, arquivo)]
print(arquivos_selecionados)  # ['documento123.txt', 'relatorio_final.pdf']
```

### 7. **Transformação de Dados:**

Manipule e transforme dados com base em padrões, como formatação de texto, limpeza de dados, etc.

#### Exemplo: Padronizar números de telefone
```python
import re

numeros_telefone = ['123-456-7890', '(987) 654-3210', '555.123.4567']

padrao = r'\D'  # Remove não dígitos

telefones_padronizados = [re.sub(padrao, '', telefone) for telefone in numeros_telefone]
print(telefones_padronizados)  # ['1234567890', '9876543210', '5551234567']
```

Esses exemplos ilustram como as expressões regulares podem ser aplicadas de maneira prática no desenvolvimento de software, permitindo validação, extração e manipulação de informações em strings de forma eficaz.

## re - Biblioteca padrão do Python para Expressões Regulares

A biblioteca `re` (regular expression) em Python é um módulo embutido que fornece funcionalidades para trabalhar com expressões regulares. As expressões regulares são padrões de busca que podem ser usados para encontrar, substituir ou manipular texto com base em um padrão específico.

Aqui está uma explicação mais detalhada sobre a biblioteca `re` e alguns comandos frequentemente utilizados:

1. **`re.compile(pattern)`**:
   - Compila uma expressão regular em um objeto de padrão que pode ser usado para realizar várias operações de correspondência.

2. **`re.match(pattern, string)`**:
   - Tenta casar o padrão no início da string. Retorna um objeto de correspondência se o padrão casar e `None` caso contrário.

3. **`re.search(pattern, string)`**:
   - Procura por uma correspondência em qualquer lugar da string. Retorna um objeto de correspondência se o padrão casar e `None` caso contrário.

4. **`re.findall(pattern, string)`**:
   - Retorna uma lista de todas as correspondências do padrão na string.

5. **`re.finditer(pattern, string)`**:
   - Retorna um iterador que produz objetos de correspondência para cada correspondência do padrão na string.

6. **`re.sub(pattern, repl, string)`**:
   - Substitui todas as ocorrências do padrão na string pelo texto de substituição (`repl`).

7. **`re.split(pattern, string)`**:
   - Divide a string com base no padrão especificado e retorna uma lista de substrings.

Referências úteis:
- Documentação oficial do Python para o módulo `re`: [Python re - Regular expression operations](https://docs.python.org/pt-br/3/library/re.html#writing-a-tokenizer)
Essas referências fornecem uma compreensão mais profunda sobre expressões regulares em Python e como usar o módulo `re` para manipular e trabalhar com padrões de texto de forma eficaz.
