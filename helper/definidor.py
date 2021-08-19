from helper.extracao import extrai_leitores, extrai_livros, extrai_emprestimo


def define_leitor_id():
    leitores = extrai_leitores()
    try:
        ultimo_id = int(leitores[-1]['id'])
        return ultimo_id + 1
    except IndexError:
        return 1


def define_livro_id():
    livros = extrai_livros()
    try:
        ultimo_id = int(livros[-1]['id'])
        return ultimo_id + 1
    except IndexError:
        return 1


def define_emprestimo_id():
    emprestimo = extrai_emprestimo()
    try:
        ultimo_id = int(emprestimo[-1]['id'])
        return ultimo_id + 1
    except IndexError:
        return 1
