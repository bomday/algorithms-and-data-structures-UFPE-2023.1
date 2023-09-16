class Suspeito: #cria suspeitos como "nós" da árvore
    def __init__(self, nome, cpf, susPai=None, susDir=None, susEsq=None, susProximo=None):
        self.nome = nome #nome do suspeito
        self.cpf = cpf #cpf de identificação do suspeito
        self.susPai = susPai #suspeito acima do nó atual
        self.susDir = susDir #suspeito à direita do nó atual
        self.susEsq = susEsq #suspeito à esquerda do nó atual
        self.susProximo = susProximo #cria fila de elementos que estão na árvore

class ArvoreSuspeitos: #cria árvore de suspeitos
    def __init__(self): #armazena raiz da árvore, que também é o primeiro elemento da fila
        self.raiz = None
        self.primeiro = None
        self.ultimo = None

    def busca_suspeito_por_nome(self, nome_suspeito): #busca nó do suspeito a partir do nome dele
        suspeito_busca_atual = self.primeiro
        while suspeito_busca_atual.nome != nome_suspeito: #busca elemento na fila para localizá-lo na árvore
            suspeito_busca_atual = suspeito_busca_atual.susProximo

        return suspeito_busca_atual

    def adicionaSuspeito(self, info_suspeito): #adiciona, item fornecido, na árvore
        cpf = info_suspeito[1]
        nome = info_suspeito[2]
        novo_suspeito = Suspeito(nome, cpf)

        if self.raiz is None:
            self.raiz = novo_suspeito
            self.primeiro = self.raiz
            self.ultimo = self.raiz
        else:
            suspeito_adicionado = False
            suspeito_atual = self.raiz
            self.ultimo.susProximo = novo_suspeito
            self.ultimo = novo_suspeito

            while not suspeito_adicionado:
                if suspeito_atual.cpf < novo_suspeito.cpf:
                    if suspeito_atual.susDir is None:
                        suspeito_atual.susDir = novo_suspeito
                        novo_suspeito.susPai = suspeito_atual
                        suspeito_adicionado = True                        
                    else:
                        suspeito_atual = suspeito_atual.susDir
                else:
                    if suspeito_atual.susEsq is None:
                        suspeito_atual.susEsq = novo_suspeito
                        novo_suspeito.susPai = suspeito_atual
                        suspeito_adicionado = True   
                    else:
                        suspeito_atual = suspeito_atual.susEsq

    def remove_suspeito(self, nome_suspeito): #remove suspeito da árvore
        suspeito_excluir = self.busca_suspeito_por_nome(nome_suspeito)
        pai = suspeito_excluir.susPai

        if suspeito_excluir.susEsq is None: #um filho à direita ou nenhum 'filho'
            if suspeito_excluir.susDir is not None:
                suspeito_excluir.susDir.susPai = pai

            if pai.susEsq == suspeito_excluir:
                pai.susEsq = suspeito_excluir.susDir
            else:
                pai.susDir = suspeito_excluir.susDir
        elif suspeito_excluir.susDir is None: #um filho à esquerda
            suspeito_excluir.susEsq.susPai = pai

            if pai.susEsq == suspeito_excluir:
                pai.susEsq = suspeito_excluir.susEsq
            else:
                pai.susDir = suspeito_excluir.susEsq
        else:
            menor_dir = suspeito_excluir.susDir
            suspeito_esquerda = suspeito_excluir.susEsq
            suspeito_direita = suspeito_excluir.susDir

            while menor_dir.susEsq is not None: #busca menor à direita
                menor_dir = menor_dir.susEsq

            if menor_dir.susDir is not None:
                pai_menor_dir = menor_dir.susPai
                pai_menor_dir.susEsq = menor_dir.susDir

                menor_dir.susEsq = suspeito_esquerda
                menor_dir.susDir = suspeito_direita

                if pai.susEsq == suspeito_excluir:
                    pai.susEsq = menor_dir
                else:
                    pai.susDir = menor_dir
            else:
                pai_menor_dir = menor_dir.susPai
                pai_menor_dir.susEsq = None

                menor_dir.susEsq = suspeito_esquerda
                menor_dir.susDir = suspeito_direita

                if pai.susEsq == suspeito_excluir:
                    pai.susEsq = menor_dir
                else:
                    pai.susDir = menor_dir
    
    def nivel_suspeito(self, nome_suspeito): #busca nível do suspeito
        suspeito_procurado = self.busca_suspeito_por_nome(nome_suspeito)
        suspeito_atual = self.raiz
        suspeito_achado = False
        nivel_suspeito = 0

        while not suspeito_achado:
            if suspeito_atual.cpf > suspeito_procurado.cpf:
                nivel_suspeito += 1   
                suspeito_atual = suspeito_atual.susEsq 
            elif suspeito_atual.cpf < suspeito_procurado.cpf:
                nivel_suspeito += 1 
                suspeito_atual = suspeito_atual.susDir
            else:
                suspeito_achado = True
        
        return nivel_suspeito
    
    def principal_suspeito(self, nome_suspeito): #faz troca de raízes para novo principal suspeito
        novo_suspeito_principal = self.busca_suspeito_por_nome(nome_suspeito)
        pai = novo_suspeito_principal.susPai
        avo = None

        while pai != None:
            suspeito_direita = novo_suspeito_principal.susDir
            suspeito_esquerda = novo_suspeito_principal.susEsq

            #coloca neto como filho do avô, se avô existir
            if pai.susPai != None:
                avo = pai.susPai
                if avo.susEsq == pai:
                    avo.susEsq = novo_suspeito_principal
                else:
                    avo.susDir = novo_suspeito_principal

            if suspeito_esquerda is None and suspeito_direita is None: #nenhum filho
                if novo_suspeito_principal == pai.susEsq:    
                    pai.susEsq = None #pai recebe novo filho                
                    novo_suspeito_principal.susDir = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
                else:                    
                    pai.susDir = None #pai recebe novo filho
                    novo_suspeito_principal.susEsq = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
            elif suspeito_esquerda is None: #um filho à direita
                if novo_suspeito_principal == pai.susEsq:                    
                    pai.susEsq = suspeito_direita #pai recebe novo filho
                    suspeito_direita.susPai = pai #antigo filho recebe novo pai
                    novo_suspeito_principal.susDir = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
                else:                  
                    pai.susDir = suspeito_esquerda #pai recebe novo filho
                    novo_suspeito_principal.susEsq = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
            elif suspeito_direita is None: #um filho à esquerda
                if novo_suspeito_principal == pai.susEsq:
                    pai.susEsq = suspeito_direita #pai recebe novo filho
                    novo_suspeito_principal.susDir = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
                else:                  
                    pai.susDir = suspeito_esquerda #pai recebe novo filho
                    suspeito_esquerda.susPai = pai #antigo filho recebe novo pai
                    novo_suspeito_principal.susEsq = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
            else: #dois filhos
                if novo_suspeito_principal == pai.susEsq:                    
                    pai.susEsq = suspeito_direita #pai recebe novo filho
                    suspeito_direita.susPai = pai #antigo filho recebe novo pai
                    novo_suspeito_principal.susDir = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
                else:
                    pai.susDir = suspeito_esquerda #pai recebe novo filho
                    suspeito_esquerda.susPai = pai #antigo filho recebe novo pai
                    novo_suspeito_principal.susEsq = pai #pai se torna filho
                    novo_suspeito_principal.susPai = avo #avô é novo pai
            pai.susPai = novo_suspeito_principal #antigo pai vira filho do seu antigo filho 
            pai = novo_suspeito_principal.susPai #pai é o novo pai do novo suspeito principal
            if pai != None:
                avo = pai.susPai
            
        self.raiz = novo_suspeito_principal
            
class Main:
    arvore_suspeitos = ArvoreSuspeitos()
    running = True

    while running: #roda programa até receber comando 'FIM'
        comando = input().split(' ')

        if comando[0] == "FIM":
            if arvore_suspeitos.raiz is not None:
                print(f'{arvore_suspeitos.raiz.nome} foi declarado o ladrão da coca!')
            running = False
        elif comando[0] == "ADD":
            arvore_suspeitos.adicionaSuspeito(comando)            
        elif comando[-1] == "saborosa.":
            nivel_suspeito = arvore_suspeitos.nivel_suspeito(comando[0])
            arvore_suspeitos.principal_suspeito(comando[0])
            print(f'{comando[0]} virou o principal suspeito e estava no nível {nivel_suspeito}.')
        elif comando[1] == "doou":
            nivel_suspeito = arvore_suspeitos.nivel_suspeito(comando[0])
            arvore_suspeitos.remove_suspeito(comando[0])
            print(f'{comando[0]} deixou de ser o principal suspeito e estava no nível {nivel_suspeito}.')