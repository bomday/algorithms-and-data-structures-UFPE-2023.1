class ListaAlunosCalourada:
    def __init__(self): 
        self.tamanho = 10 #tamanho disponível da lista
        self.lista_alunos_hash = [[] for vaga in range(10)] #tabela hash em estrutura de lista com listas dentro que irão conter índice e nome do aluno 

    def pegar_indice(self, nome_aluno): #retorna o índice que elemento ficará na lista
        valor_nome = 0 #irá comportar o valor da soma entre as letras do nome
        for letra in nome_aluno: #acrescenta à variável 'valor_nome' o valor correspondente a cada letra do nome
            valor_nome += ord(letra) - ord('A') + 1
        return valor_nome % self.tamanho #retorna o índice

    def inserir_aluno(self, nome_aluno): #insere um novo aluno na lista de alunos 
        indice = self.pegar_indice(nome_aluno)
        self.lista_alunos_hash[indice].append(nome_aluno)

    def imprimir_lista_calourada(self): #imprime lista de alunos
        for indice in range(len(self.lista_alunos_hash)):
            if self.lista_alunos_hash[indice] != []:
                print(f"{indice}:", end="")
                for aluno in self.lista_alunos_hash[indice]: #imprime todos os alunos dentro da lista de alunos
                    print(f" {aluno}", end="")
                print("")

class Main: #roda o programa
    num_alunos = int(input())
    lista_calourada = ListaAlunosCalourada()

    for count in range(num_alunos):
        nome_aluno = input()
        lista_calourada.inserir_aluno(nome_aluno)
    
    lista_calourada.imprimir_lista_calourada()