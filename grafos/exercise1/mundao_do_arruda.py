class Local:
  def __init__(self, nome, index, caminho=[], prox=None):
    self.nome = nome
    self.index = index
    self.caminho = caminho
    self.prox = prox

class CaminhoArruda:
  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0] * vertices for vertice in range(vertices)]
  
  def adicionar_aresta(self, vertice1, vertice2):
    self.grafo[vertice1][vertice2] = 1
    self.grafo[vertice2][vertice1] = 1
  
  def busca_em_largura(self, vertice_inicial, lista_locais):
    visitados = [False]*self.vertices #registra vértices visitados
    visitados[vertice_inicial] = True #marca vértice informado como visitado
    novo_vertice_fila = Local(lista_locais[vertice_inicial], vertice_inicial, [vertice_inicial]) #insere vértice informado em fila
    vertice_atual = vertice_inicial
    vertice_final = self.vertices-1 #vértice final é o que deve ser encontrado
    vertice_fila_conferido = novo_vertice_fila #adiciona os vértices na fila
    prox_vertice_fila = novo_vertice_fila #registra o prox vértice a se conferir 
    
    while vertice_atual != vertice_final and prox_vertice_fila: #enquanto não se encontra o vértice final e existe prox na fila
      for vertice_vizinho in range(self.vertices):
        if self.grafo[vertice_atual][vertice_vizinho] == 1: #adiciona cada vértice ligado ao atual na fila
          if visitados[vertice_vizinho] == False:
            vertice_fila_conferido.prox = Local(lista_locais[vertice_vizinho], vertice_vizinho, prox_vertice_fila.caminho + [vertice_vizinho]) #adiciona prox na fila
            vertice_fila_conferido = vertice_fila_conferido.prox #registra o prox vértice na fila a ser conferido
            visitados[vertice_vizinho] = True
          if vertice_vizinho == vertice_final:
            vertice_atual = vertice_final
            break
      if prox_vertice_fila.prox == None:
        prox_vertice_fila = None
      elif vertice_atual != vertice_final:
        vertice_atual = prox_vertice_fila.prox.index #vértice atual é o índice do vértice do prox da fila
        prox_vertice_fila = prox_vertice_fila.prox #o prox vértice a se conferir será o prox do atual
    
    if vertice_atual == vertice_final:
      return vertice_fila_conferido.caminho
    else:
      return None

class Main: #roda o programa
  lista_locais = input().split()
  conexoes = len(lista_locais)
  caminho_arruda = CaminhoArruda(conexoes)

  while conexoes > 0: #recebe as conexões entre os locais
    comando = input().split()
    for item in comando:
      caminho_arruda.adicionar_aresta(len(lista_locais)-conexoes, int(item))
    conexoes -= 1
  
  caminho_final = caminho_arruda.busca_em_largura(0, lista_locais)

  if caminho_final:
    print(f'Grafite precisou passar por {len(caminho_final)} pontos através do caminho', end='')
    for vertice in caminho_final:
      if vertice != caminho_final[-1]:
        print(f' {lista_locais[vertice]} ->', end='')
      else:
        print(f' {lista_locais[vertice]}.')
  else:
    print('Infelizmente Grafite não pode chegar no Arruda.')