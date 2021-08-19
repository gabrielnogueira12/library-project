from helper.definidor import define_leitor_id, define_livro_id, define_emprestimo_id
from helper.procuradores import procura_livro_nome, procura_leitor_nome


def cadastra_leitor(nome, email, telefone):
    with open("dataset/leitores.csv", 'a') as leitores:
        id_leitor = define_leitor_id()
        valida_nome = procura_leitor_nome(nome)
        if valida_nome[1] is True:
            return "Leitor já cadastrado!"
        leitores.seek(2, 0)
        leitores.write(f"\n{id_leitor},{nome},{email},{telefone}")
        return "Leitor cadastrado com sucesso!"


def cadastra_livro(titulo, autor, paginas):
    with open("dataset/biblioteca.csv", 'a') as biblioteca:
        id_livro = define_livro_id()
        valida_titulo = procura_livro_nome(titulo)
        if valida_titulo[1] is True:
            return "Livro já cadastrado!"
        if int(paginas) <= 299:
            valor = 4
        else:
            valor = 6
        biblioteca.seek(2, 0)
        biblioteca.write(f"\n{id_livro},{titulo},{autor},{paginas},{valor}")
    return "Livro cadastrado com sucesso!"


def cadastra_emprestimo(nome_leitor, nome_livro, data_inicio, data_fim):
    with open("dataset/emprestimos.csv", 'a') as emprestimos:
        id_emprestimo = define_emprestimo_id()
        emprestimos.seek(2, 0)

        leitor = procura_leitor_nome(nome_leitor)
        if leitor[1] is False:
            return "Leitor não cadastrado!"
        else:
            id_leitor = leitor[0]['id']

        livro = procura_livro_nome(nome_livro)
        if livro[1] is False:
            return "Livro não cadastrado!"
        else:
            id_livro = livro[0]['id']

        emprestimos.write(f"\n{id_emprestimo},{id_leitor},{id_livro},{data_inicio},{data_fim},1")
        return "Empréstimo cadastrado com sucesso!"
