class Mulher: #cria mulheres como "nós" da árvore
  def __init__(self, nome, filhaDir=None, filhaEsq=None):
    self.nome = nome
    self.filhaDir = filhaDir
    self.filhaEsq = filhaEsq

class ArvoreGenealogica: #cria árvore genealógica
  def __init__(self):
    self.raiz = None

  def criarArvore(self, lista): #cria árvore a partir de conteúdo da lista fornecida
    for mulher in lista:     
      nova_mulher = Mulher(mulher)
      if self.raiz is None:
        self.raiz = nova_mulher
      else:
        entrou = False
        item_atual = self.raiz
        while not entrou:
          if item_atual.nome < nova_mulher.nome:
            if item_atual.filhaDir is None:
              item_atual.filhaDir = nova_mulher
              nova_mulher.pai = item_atual
              entrou = True                    
            else:
              item_atual = item_atual.filhaDir
          else:
            if item_atual.filhaEsq is None:
              item_atual.filhaEsq = nova_mulher
              nova_mulher.pai = item_atual
              entrou = True
            else:
              item_atual = item_atual.filhaEsq
  
  def imprimeArvore(self, mulher): #começa a imprimir a árvore a partir do nó dado
    if self.raiz:
      item_atual = mulher

      if item_atual is None:
        item_atual = self.raiz

      #outputs
      if item_atual.filhaDir and item_atual.filhaEsq is not None:
        print(f'{item_atual.nome} é mãe de {item_atual.filhaEsq.nome} e {item_atual.filhaDir.nome}.')
      else:
        if item_atual.filhaDir:
          print(f'{item_atual.nome} é mãe de {item_atual.filhaDir.nome}.')
        if item_atual.filhaEsq:
          print(f'{item_atual.nome} é mãe de {item_atual.filhaEsq.nome}.')
        
      #chamando as outras mulheres
      if item_atual.filhaEsq:
        self.imprimeArvore(item_atual.filhaEsq)
      if item_atual.filhaDir:
        self.imprimeArvore(item_atual.filhaDir)

class Main:
  lista = input().split(' ')
  arvoreFamiliar = ArvoreGenealogica()
  
  arvoreFamiliar.criarArvore(lista)
  arvoreFamiliar.imprimeArvore(arvoreFamiliar.raiz)