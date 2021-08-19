from csv import DictReader


def extrai_leitores():
    leitores_extraidos = []
    with open("dataset/leitores.csv", 'r') as leitores_dados:
        leitores = DictReader(leitores_dados)
        for leitor in leitores:
            leitores_extraidos.append(leitor)
    return leitores_extraidos


def extrai_livros():
    livros_extraidos = []
    with open("dataset/biblioteca.csv", 'r') as biblioteca:
        livros = DictReader(biblioteca)
        for livro in livros:
            livros_extraidos.append(livro)
    return livros_extraidos


def extrai_emprestimo():
    emprestimos_extraidos = []
    with open("dataset/emprestimos.csv", 'r') as emprestimos_dados:
        emprestimos = DictReader(emprestimos_dados)
        for emprestimo in emprestimos:
            emprestimos_extraidos.append(emprestimo)
    return emprestimos_extraidos
