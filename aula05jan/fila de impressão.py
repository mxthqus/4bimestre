# vamos pensar como funciona o algoritmo de uma impressora que pode receber impressão de diversos computadores, vamos pensar em uma fila
# isso daqui vai guardar a fila de impressão no vetor fila
class FilaDeImpressao:
    def configurar_inicial(self):
        self.fila = []

    # adicionar um trabalho na fila
    def adicionar_trabalho(self, trabalho):
        self.fila.append(trabalho)
        print(f"O trabalho {trabalho} foi adicionado na fila")

    # remover o trabalho da lista
    def processar_trabalho(self):
        if not self.esta_vazia():  # verifica se a lista nao esta vazia
            trabalho = self.fila.pop(0)  # remove o primeiro da fila
            print(f"O trabalho {trabalho} foi impresso")
        else:
            print("A fila de impressão está vazia")

    # mostrar a fila de impressão
    def mostrar_fila(self):
        if self.esta_vazia():  # verifica se a lista nao esta vazia
            print("A fila de impressão está vazia")
        else:  # mostra a fila de impressão se não estiver vazia
            print("Fila de impressão: ")
            for trabalho in self.fila:
                print(f" - {trabalho}")  # imprimir cada trabalho da fila

    def esta_vazia(self):
        return len(self.fila) == 0  # verifica se a fila esta vazia


# funções de interação com o usuario
def menu():
    fila_impressao = FilaDeImpressao()
    # criando uma instância para a classe
    fila_impressao.configurar_inicial()
    # configurar os atributos de entrada/inicial
    while True:
        # opções para o nosso usuário
        print("Opções: ")
        print("1 - Adicionar um trabalho na fila de impressão")
        print("2 - Imprimir o próximo trabalho na fila")
        print("3 - Mostrar a fila de impressão")
        print("4 - Sair")
        escolha = input("Escolha uma opção de 1 até 4: ")
        # aqui vai ser lido a escolha do usuário

        if escolha == "1":
            trabalho = input("Digite o nome do trabalho: ")  # maquina da pessoa que está imprimindo
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

# Executar o menu
menu()
