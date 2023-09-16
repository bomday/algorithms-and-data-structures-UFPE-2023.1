class Aluno: #cria alunos como "nós" da árvore
    def __init__(self, nome, fatorBalanceamento=0, pai=None, dir=None, esq=None):
        self.nome = nome #nome do aluno
        self.fatorB = fatorBalanceamento #aramzena fator de balanceamento do nó
        self.pai = pai #aluno acima do nó atual
        self.dir = dir #aluno à direita do nó atual
        self.esq = esq #aluno à esquerda do nó atual

class ArvoreAlunos: #cria árvore de alunos
    def __init__(self):
        self.raiz = None #raiz da árvore

    def imprimir_pre_ordem(self, aluno=None): #imprime a árvore em pré ordem
        if self.raiz: #se raiz existir, imprime os alunos
            aluno_atual = aluno

            if aluno_atual is None: #se não recebe nenhum aluno como parâmetro, inicia pela raiz
                aluno_atual = self.raiz

            #output
            print(aluno_atual.nome, "-> ", end="") #imprime com formatação requerida
            
            #chamando outros alunos
            if aluno_atual.esq:
                self.imprimir_pre_ordem(aluno_atual.esq)
            if aluno_atual.dir:
                self.imprimir_pre_ordem(aluno_atual.dir)
        else:
            print('ARVORE VAZIA')

    def altura_arvore_alunos(self, aluno):
        #alturas -1, pois assim adiciona nós e conta a quantidade de ponteiros até o nó máx
        altura_arvore_esquerda = -1
        altura_arvore_direita = -1
        #se existe raiz, faz cálculo da altura e recebe parâmetro do nó atual para fazer o cálculo da altura
        if self.raiz and aluno:
            if aluno.esq:
                altura_arvore_esquerda = self.altura_arvore_alunos(aluno.esq)
            if aluno.dir:
                altura_arvore_direita = self.altura_arvore_alunos(aluno.dir)

            return max(altura_arvore_esquerda, altura_arvore_direita) + 1
                                
        return max(altura_arvore_esquerda, altura_arvore_direita)
    
    def buscar_aluno_por_nome(self, nome_aluno, aluno_atual=None): #busca nó do aluno a partir do nome dele
        if not aluno_atual: #se não recebe nenhum aluno como parâmetro, inicia pela raiz
            aluno_atual = self.raiz

        if nome_aluno == aluno_atual.nome: 
            return aluno_atual
        elif nome_aluno < aluno_atual.nome: 
            return self.buscar_aluno_por_nome(nome_aluno, aluno_atual.esq)
        else:
            return self.buscar_aluno_por_nome(nome_aluno, aluno_atual.dir)

    def calcular_fator_balanceamento(self, aluno): #calcula fator de balanceamento
        if aluno: #calcula fator de balanceamento se aluno existe na árvore
            altura_arvore_esquerda = self.altura_arvore_alunos(aluno.esq)
            altura_arvore_direita = self.altura_arvore_alunos(aluno.dir)

            fator_balanceamento =  altura_arvore_direita - altura_arvore_esquerda
            return fator_balanceamento
        
        return None 

    def atualizar_fator_balanceamento(self, aluno): #atualiza o fator de balanceamento do nó
        if aluno:
            aluno.fatorB = self.calcular_fator_balanceamento(aluno) #calcula fator de balanceamento e atualiza valor no nó
            
            if aluno.fatorB == 1 or aluno.fatorB == -1: #chama cálculo de pai do nó atual
                self.atualizar_fator_balanceamento(aluno.pai)
            elif aluno.fatorB >= 2: #chama rotações de balanceamento quando altura direita é maior     
                aluno_conferir = aluno.dir #variável de busca para rotações  

                if aluno_conferir.fatorB == 0 or aluno_conferir.fatorB == 1: #chama rotação simples quando o fator de balanceamento do filho é 0 ou de mesmo sinal
                    self.rotacionar_para_esquerda(aluno)
                    self.atualizar_fator_balanceamento(aluno) #atualiza fator de balanceamento a partir do antigo aluno
                else: #chama rotação dupla quando o fator de balanceamento do filho é de sinal diferente
                    self.rotacionar_para_direita(aluno_conferir)  
                    self.rotacionar_para_esquerda(aluno_conferir.pai.pai) #aluno_conferir.pai.pai é equivalente ao antigo pai do nó atual
                    self.atualizar_fator_balanceamento(aluno.pai) #atualiza fator de balanceamento do novo pai
            
            elif aluno.fatorB <= -2: #chama rotações de balanceamento quando altura esquerda é maior          
                aluno_conferir = aluno.esq #variável de busca para rotações   

                if aluno_conferir.fatorB == 0 or aluno_conferir.fatorB == -1: #chama rotação simples quando o fator de balanceamento do filho é 0 ou de mesmo sinal
                    self.rotacionar_para_direita(aluno)
                    self.atualizar_fator_balanceamento(aluno) #atualiza fator de balanceamento a partir do antigo aluno
                else: #chama rotação dupla quando o fator de balanceamento do filho é de sinal diferente
                    self.rotacionar_para_esquerda(aluno_conferir) 
                    self.rotacionar_para_direita(aluno_conferir.pai.pai) #aluno_conferir.pai.pai é equivalente ao antigo pai do nó atual                   
                    self.atualizar_fator_balanceamento(aluno.pai) #atualiza fator de balanceamento do novo pai

    def rotacionar_para_direita(self, aluno): #rotaciona para a direita, a partir do nó de referência dado
        pai = aluno.pai #pai do nó dado
        aluno_substituto = aluno.esq #nó que vai substituir a posição do nó dado
        aluno_temporario = aluno_substituto.dir #filho do nó substituto que será transferido para o nó dado
        
        #designa novo filho para o pai do nó dado
        if pai != None and pai.dir == aluno: 
            pai.dir = aluno_substituto
        elif pai != None and pai.esq == aluno:
            pai.esq = aluno_substituto
        elif pai is None:
            self.raiz = aluno_substituto

        aluno_substituto.pai = pai #pai do nó dado se torna pai do nó substituto
        aluno_substituto.dir = aluno #nó dado vira filho do nó substituto
        aluno.pai = aluno_substituto #nó substituto vira pai do nó dado
        aluno.esq = aluno_temporario #filho do nó substituto é transferido para o nó dado
        if aluno_temporario: #se filho do nó substituto não for NONE, ele recebe o nó dado como pai
            aluno_temporario.pai = aluno
        
        if aluno_substituto.esq: #se existir filho à esquerda da posição atualizado do nó substituto 
            aluno_substituto.esq.fatorB = self.calcular_fator_balanceamento(aluno_substituto.esq) #calcula fator de balanceamento e atualiza valor do nó substituto
        aluno.fatorB = self.calcular_fator_balanceamento(aluno) #calcula fator de balanceamento e atualiza valor do nó

    def rotacionar_para_esquerda(self, aluno): #rotaciona para a esquerda, a partir do nó de referência dado
        pai = aluno.pai #pai do nó dado
        aluno_substituto = aluno.dir #nó que vai substituir a posição do nó dado
        aluno_temporario = aluno_substituto.esq #filho do nó substituto que será transferido para o nó dado

        #designa novo filho para o pai do nó dado
        if pai != None and pai.dir == aluno:
            pai.dir = aluno_substituto
        elif pai != None and pai.esq == aluno:
            pai.esq = aluno_substituto
        elif pai is None:
            self.raiz = aluno_substituto

        aluno_substituto.pai = pai #pai do nó dado se torna pai do nó substituto
        aluno_substituto.esq = aluno #nó dado vira filho do nó substituto
        aluno.pai = aluno_substituto #nó substituto vira pai do nó dado
        aluno.dir = aluno_temporario #filho do nó substituto é transferido para o nó dado
        if aluno_temporario: #se filho do nó substituto não for NONE, ele recebe o nó dado como pai
            aluno_temporario.pai = aluno

        if aluno_substituto.dir: #se existir filho à direita da posição atualizado do nó substituto
            aluno_substituto.dir.fatorB = self.calcular_fator_balanceamento(aluno_substituto.dir) #calcula fator de balanceamento e atualiza valor do nó substituto
        aluno.fatorB = self.calcular_fator_balanceamento(aluno) #calcula fator de balanceamento e atualiza valor do nó

    def adicionar_aluno(self, nome_aluno, aluno_existe): #adiciona, item fornecido, na árvore
        if aluno_existe:
            print(f'{nome_aluno} JA EXISTE')
        else:
            novo_aluno = Aluno(nome_aluno)

            if self.raiz is None: #adiciona primeiro item da árvore
                self.raiz = novo_aluno
            else:
                aluno_adicionado = False
                aluno_atual = self.raiz

                while not aluno_adicionado:
                    if aluno_atual.nome < novo_aluno.nome:
                        if aluno_atual.dir is None:
                            aluno_atual.dir = novo_aluno
                            novo_aluno.pai = aluno_atual
                            aluno_adicionado = True                        
                        else:
                            aluno_atual = aluno_atual.dir
                    else:
                        if aluno_atual.esq is None:
                            aluno_atual.esq = novo_aluno
                            novo_aluno.pai = aluno_atual
                            aluno_adicionado = True   
                        else:
                            aluno_atual = aluno_atual.esq
                
                self.atualizar_fator_balanceamento(novo_aluno.pai) #atualiza o fator de balanceamento do pai do nó adicionado
            
            print(f'{nome_aluno} INSERIDO')

    def remover_aluno(self, nome_aluno, aluno_existe): #remove, item fornecido, na árvore
        if not aluno_existe:
            print(f'{nome_aluno} NAO ENCONTRADO')
        else:
            aluno_excluir = self.buscar_aluno_por_nome(nome_aluno)
            pai = aluno_excluir.pai
    
            if aluno_excluir.esq is None: # um filho à direita ou nenhum 'filho'
                if aluno_excluir.dir:
                    aluno_excluir.dir.pai = pai
    
                if pai:
                    if pai.esq == aluno_excluir:
                        pai.esq = aluno_excluir.dir
                        self.atualizar_fator_balanceamento(pai)
                    elif pai.dir == aluno_excluir:
                        pai.dir = aluno_excluir.dir
                        self.atualizar_fator_balanceamento(pai)
                else:
                    self.raiz = aluno_excluir.dir
            elif aluno_excluir.dir is None: # um filho à esquerda
                aluno_excluir.esq.pai = pai
                        
                if pai:
                    if pai.esq == aluno_excluir:
                        pai.esq = aluno_excluir.esq
                        self.atualizar_fator_balanceamento(pai)
                    elif pai.dir == aluno_excluir:
                        pai.dir = aluno_excluir.esq
                        self.atualizar_fator_balanceamento(pai)
                else:
                    self.raiz = aluno_excluir.esq
            else:  
                menor_dir = aluno_excluir.dir
                aluno_esquerda = aluno_excluir.esq
                aluno_direita = aluno_excluir.dir
    
                # busca menor à direita
                while menor_dir.esq:
                    menor_dir = menor_dir.esq
    
                # faz trocas de filhos do pai do menor à direita
                if menor_dir.dir:
                    menor_dir.dir.pai = menor_dir.pai
                if menor_dir != aluno_excluir.dir:
                    menor_dir.pai.esq = menor_dir.dir
                pai_antigo_menor_dir = menor_dir.pai
                        
                # define novo pai do menor à direita
                if pai:
                    if pai.esq == aluno_excluir:
                        pai.esq = menor_dir
                    elif pai.dir == aluno_excluir:
                        pai.dir = menor_dir
                else:
                    self.raiz = menor_dir
                menor_dir.pai = pai
    
                # define novos filhos do menor à direita
                menor_dir.esq = aluno_esquerda
                if aluno_excluir.dir != menor_dir:
                    menor_dir.dir = aluno_direita
    
                # define novo pai do filho à direita do menor à direita
                if menor_dir.dir:
                    aluno_direita.pai = menor_dir
                if menor_dir.esq:
                    aluno_esquerda.pai = menor_dir
    
                # faz atualização do fator de balanceamento do antigo pai do menor à direita
                if pai_antigo_menor_dir != aluno_excluir:
                    self.atualizar_fator_balanceamento(pai_antigo_menor_dir)
    
            print(f'{nome_aluno} REMOVIDO')

class Main:
    lista_alunos = []
    arvore_alunos = ArvoreAlunos()
    running = True

    while running:
        comando = input().split(' ')

        if comando[0] == 'FIM':
            arvore_alunos.imprimir_pre_ordem()
            altura_arvore = arvore_alunos.altura_arvore_alunos(arvore_alunos.raiz)
            print(f'FIM. ALTURA: {altura_arvore}')
            running = False
        else:
            aluno_existe = False
            for aluno in lista_alunos:
                if aluno == comando[1]:
                    aluno_existe = True

            if comando[0] == 'INSERIR':
                if not aluno_existe:
                    lista_alunos.append(comando[1])
                arvore_alunos.adicionar_aluno(comando[1], aluno_existe)
            elif comando[0] == 'DELETAR':
                if aluno_existe:
                    lista_alunos.remove(comando[1])
                arvore_alunos.remover_aluno(comando[1], aluno_existe)