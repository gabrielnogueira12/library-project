from helper.extracao import extrai_leitores, extrai_livros, extrai_emprestimo
from helper.procuradores import procura_livro_id, procura_leitor_id


def consulta_leitores():
    leitores = extrai_leitores()
    for leitor in leitores:
        print(f"Código: {leitor['id']}".ljust(12), end="\t")
        print(f"Nome completo: {leitor['nome_completo']}".ljust(50), end="\t")
        print(f"Email:{leitor['email']}".ljust(30), end="\t")
        print(f"Telefone: {leitor['telefone']}".ljust(20))


def consulta_livros():
    livros = extrai_livros()
    for livro in livros:
        print(f"Código: {livro['id']}".ljust(12), end="\t")
        print(f"Título: {livro['titulo']}".ljust(50), end="\t")
        print(f"Autor:{livro['autor']}".ljust(30), end="\t")
        print(f"Páginas: {livro['pages']}".ljust(20), end="\t")
        print(f"Valor: R${livro['valor_aluguel']},00")


def consulta_emprestimos_ativos():
    emprestimos = extrai_emprestimo()
    for emprestimo in emprestimos:
        if emprestimo['ativo'] == '1':
            leitor = procura_leitor_id(emprestimo['id_leitor'])
            livro = procura_livro_id(emprestimo['id_livro'])
            print(f"Código: {emprestimo['id']}".ljust(12), end="\t")
            print(f"Leitor: {leitor[0]['nome_completo']}".ljust(50), end="\t")
            print(f"Livro:{livro[0]['titulo']}".ljust(30), end="\t")
            print(f"Data início: {emprestimo['data_inicio']}".ljust(10), end="\t")
            print(f"Data final: {emprestimo['data_fim']}".ljust(10))


def consulta_historico_emprestimos():
    emprestimos = extrai_emprestimo()
    for emprestimo in emprestimos:
        if emprestimo['ativo'] == '0':
            leitor = procura_leitor_id(emprestimo['id_leitor'])
            livro = procura_livro_id(emprestimo['id_livro'])
            print(f"Código: {emprestimo['id']}".ljust(12), end="\t")
            print(f"Leitor: {leitor[0]['nome_completo']}".ljust(50), end="\t")
            print(f"Livro:{livro[0]['titulo']}".ljust(30), end="\t")
            print(f"Data início: {emprestimo['data_inicio']}".ljust(10), end="\t")
            print(f"Data final: {emprestimo['data_fim']}".ljust(10))
