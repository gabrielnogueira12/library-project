from helper.extracao import extrai_livros, extrai_leitores


def procura_leitor_nome(nome):
    leitores = extrai_leitores()
    for leitor in leitores:
        if leitor['nome_completo'] == nome:
            return leitor, True
    return None, False


def procura_leitor_id(codigo_id):
    leitores = extrai_leitores()
    for leitor in leitores:
        if leitor['id'] == codigo_id:
            return leitor, True
    return None, False


def procura_livro_nome(titulo):
    livros = extrai_livros()
    for livro in livros:
        if livro['titulo'] == titulo:
            return livro, True
    return None, False


def procura_livro_id(codigo_id):
    livros = extrai_livros()
    for livro in livros:
        if livro['id'] == codigo_id:
            return livro, True
    return None, False
