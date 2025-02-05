#vamos pensar como funciona o algoritmo de uma impressora que pode receber impressão de diversos computadores, vamos pensar em uma fila

def menu():
        fila_impressao = FilaDeImpressao()
        #criando uma instância para a classe
        fila_impressao.configurar.inicial()
        #configurar os atributos de entrada/inicial
        while True:
            #opções para o nosso usuário
            print("Opções: ")
            print("1 - Adicionar um trabalho na fila de impressão")
            print("2 - Imprimir o próximo trabalho na fila")
            print("3 - Mostrar a fila de impressão")
            print("4 - Sair")
            escolha = input("Escolha uma opção de 1 até 4: ")
            #aqui vai ser lido a escolha do usuário
            
        if escolha== "1":
            trabalho = input("Digite o nome do trabalho: ") #maquina da pessoa que está imprimindo
            fila_impressao.adicionar_trabalho(trabalho)
        elif escolha == "2":
            fila_impressao.processar_trabalho()
        elif escolha == "3":
            fila_impressao.mostrar_fila()
        elif escolha == "4":
            print("Até mais!")
            break
        else:
            print("Opção inválida")