import re

# ---------------------------------------------------------
# ANÁLISE LÉXICA
# ---------------------------------------------------------
# Este módulo identifica os elementos básicos da linguagem,
# chamados de tokens.
# ---------------------------------------------------------

TOKENS = [
    ('INICIO', r'inicio'),
    ('FIM', r'fim'),
    ('NUMERO', r'\d+'),
    ('ID', r'[a-zA-Z_]\w*'),
    ('ATRIB', r'='),
    ('SOMA', r'\+'),
    ('ESPACO', r'\s+'),
]

def lexer(codigo):
    tokens = []

    while codigo:
        match = None

        for tipo, regex in TOKENS:
            padrao = re.compile(regex)
            match = padrao.match(codigo)

            if match:
                texto = match.group(0)

                if tipo != 'ESPACO':
                    tokens.append((tipo, texto))

                codigo = codigo[len(texto):]
                break

        if not match:
            raise SyntaxError(f"Token inválido: {codigo[0]}")

    return tokens
