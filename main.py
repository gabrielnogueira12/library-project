from functions.consulta import consulta_leitores, consulta_livros, consulta_emprestimos_ativos, \
    consulta_historico_emprestimos
from functions.cadastro import cadastra_leitor, cadastra_livro, cadastra_emprestimo
from functions.alteracao import finalizar_emprestimo

print("===========================================")
print("------------ Bem vindo a LIBER ------------")

menu = True

while menu:
    print("===========================================")
    escolha1_menu = input('Selecione o número do serviço que você deseja realizar:\n'
                          '1. Consultar\n'
                          '2. Cadastrar\n'
                          '3. Finalizar empréstimo\n'
                          '4. Sair\n')

    if escolha1_menu == '1':
        escolha2_control = True
        while escolha2_control:
            print("===========================================")
            print("--- Escolha o que você deseja consultar ---")
            escolha2_menu = input('1. Leitores\n'
                                  '2. Livros\n'
                                  '3. Empréstimos ativos\n'
                                  '4. Histórico de Empréstimos\n'
                                  '5. Voltar\n')
            if escolha2_menu == '1':
                print("===========================================")
                consulta_leitores()
            elif escolha2_menu == '2':
                print("===========================================")
                consulta_livros()
            elif escolha2_menu == '3':
                print("===========================================")
                consulta_emprestimos_ativos()
            elif escolha2_menu == '4':
                print("===========================================")
                consulta_historico_emprestimos()
            elif escolha2_menu == '5':
                escolha2_control = False
                break
            else:
                print('ESCOLHA INVÁLIDA! Por favor, selecione uma escolha válida.')

    elif escolha1_menu == '2':
        escolha2_control = True
        while escolha2_control:
            print("===========================================")
            print("--- Escolha o que você deseja cadastrar ---")
            escolha2_menu = input('1. Leitor\n'
                                  '2. Livro\n'
                                  '3. Empréstimo\n'
                                  '4. Voltar\n')

            if escolha2_menu == '1':
                print("===========================================")
                nome = input('Nome completo: ')
                email = input('Email: ')
                telefone = input('Telefone: ')
                print(cadastra_leitor(nome, email, telefone))

            elif escolha2_menu == '2':
                print("===========================================")
                titulo = input('Título: ')
                autor = input('Autor: ')
                paginas = input('Quantidade de páginas: ')
                print(cadastra_livro(titulo, autor, paginas))

            elif escolha2_menu == '3':
                print("===========================================")
                nome_leitor = input('Leitor: ')
                titulo_livro = input('Livro: ')
                data_inicio = input('Data início: ')
                data_fim = input('Data fim: ')
                print(cadastra_emprestimo(nome_leitor, titulo_livro, data_inicio, data_fim))

            elif escolha2_menu == '4':
                escolha2_control = False
                break
            else:
                print('ESCOLHA INVÁLIDA! Por favor, selecione uma escolha válida.')

    elif escolha1_menu == '3':
        print("===========================================")
        codigo_emprestimo = input('Digite o código do empréstimo: ')
        print(finalizar_emprestimo(codigo_emprestimo))
    elif escolha1_menu == '4':
        menu = False
        break
    else:
        print('ESCOLHA INVÁLIDA! Por favor, selecione uma escolha válida.')
