from helper.extracao import extrai_emprestimo


def finalizar_emprestimo(id_emprestimo):
    emprestimos = extrai_emprestimo()
    with open('dataset/emprestimos.csv', 'w') as emprestimos_novo:
        emprestimo_encontrado = False
        emprestimos_novo.write('id,id_leitor,id_livro,data_inicio,data_fim,ativo')
        for emprestimo in emprestimos:
            if emprestimo['id'] == id_emprestimo:
                emprestimo['ativo'] = '0'
                emprestimo_encontrado = True
            emprestimos_novo.write(f"\n{emprestimo['id']},"
                                   f"{emprestimo['id_leitor']},"
                                   f"{emprestimo['id_livro']},"
                                   f"{emprestimo['data_inicio']},"
                                   f"{emprestimo['data_fim']},"
                                   f"{emprestimo['ativo']}")
        if emprestimo_encontrado:
            return "Empréstimo finalizado!"
        else:
            return "Empréstimo não encontrado!"
