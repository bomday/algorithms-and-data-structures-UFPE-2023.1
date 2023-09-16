class CInterage:
  def __init__(self):
    self.vertices = 0 #armazena quantidade vértices que é calculado após o input de usuários
    self.grafo = [] #armazena grafo que é calculado após o input de usuários
    self.lista_dicionarios = [] #armazena lista de dicionários com infos de cada usuário
    self.lista_id = [] #armazena lista de id de cada usuário, na mesma ordem da lista de dicionários

  def adicionar_aresta(self, vertice1_inicial, vertice2_inicial):
    count = 0
    vertice1 = 0
    vertice2 = 0
    for id in self.lista_id:
      if int(id) == vertice1_inicial:
        vertice1 = count
      if int(id) == vertice2_inicial:
        vertice2 = count
      count += 1
    self.grafo[vertice1][vertice2] = 1
    self.grafo[vertice2][vertice1] = 1

  def transformar_json_lista_dic(self, json): #tranformar o json em lista de dicionário
    #inicializações gerais para o processo de tratamento de string json
    dicionario = {} #armazena cada dicionário para adicionar à lista de dicionário
    num = [str(num) for num in range(10)] 
    chave = ""
    valor = ""
    buscando_chave = True
    buscando_valor = False
    primeiro_item = True
    indice_vizinho = 0
    indice_anterior = -2
    #confere cada caracter do json
    for char in json:        
      if indice_vizinho < len(json)-1:
        indice_vizinho +=1
      indice_anterior +=1
      if (json[indice_vizinho] in num and char == ' ') or (json[indice_anterior] in num and char == ' ') or (char == '"' and json[indice_vizinho] != ':' and json[indice_vizinho] != ','):
        if buscando_chave and not primeiro_item:
          buscando_chave = False
          buscando_valor = True
        elif buscando_valor:
          buscando_chave = True
          buscando_valor = False
          dicionario[chave] = valor
          if chave == 'id':
            self.lista_id.append(valor)
          if chave == 'curso':
            self.lista_dicionarios.append(dicionario)
            dicionario = {}
            primeiro_item = True
          chave = ""
          valor = ""
      elif (char == " " and chave == 'curso' and buscando_valor == True) or (char != " " and char != "[" and char != "{" and char != "]" and char != "}" and char != ":" and char != "," and char != '"'):
        if primeiro_item:
          primeiro_item = False
        if buscando_chave:
          chave += char
        elif buscando_valor:
          valor += char

    self.vertices = len(self.lista_dicionarios) #define quantidade de vértices
    self.grafo = [[0] * self.vertices for vertice in range(self.vertices)] #define o grafo

  def transformar_tupla_lista(self, tuplas): #tranformar string de tuplas em lista de tuplas
    #inicializações gerais para o processo de tratamento de string  tuplas
    lista_tuplas = []
    num = [str(num) for num in range(10)]
    valor1 = ''
    valor2 = ''
    pegar_valor1 = True
    pegar_valor2 = False
    primeiro_item = True
    indice_vizinho = 0
    indice_anterior = -2
    #confere cada caracter da string tuplas
    for char in tuplas:        
      if indice_vizinho < len(tuplas)-1:
        indice_vizinho +=1
      indice_anterior +=1
      if char == '(' or char == ',' or char == tuplas[-1]:
        if pegar_valor1 and not primeiro_item:
          pegar_valor1 = False
          pegar_valor2 = True
        elif pegar_valor2:
          pegar_valor1 = True
          pegar_valor2 = False
          data_tupla = (int(valor1), int(valor2))
          lista_tuplas.append(data_tupla)
          primeiro_item = True
          valor1 = ""
          valor2 = ""
      elif char in num:
        if primeiro_item:
          primeiro_item = False
        if pegar_valor1:
          valor1 += char
        elif pegar_valor2:
          valor2 += char
    #adiona arestas entre os vértices contidos na tupla
    for tupla in lista_tuplas: 
      self.adicionar_aresta(tupla[0], tupla[1])

  def analise_usuario(self, id):
    #encontra nome do usuário analisado
    for dicionario in self.lista_dicionarios:
      if dicionario['id'] == str(id):
        nome_usuario = dicionario['nome']

    #encontra número de conexões e amigos
    count = 0
    conexoes = 0
    lista_amigos = []
    indice_grafo_usuario = self.lista_id.index(str(id))
    for item in self.grafo[indice_grafo_usuario]: #busca conexões dentro do grafo do usuário analisado
      if item == 1:
        conexoes += 1
        for dicionario in self.lista_dicionarios:
          if dicionario['id'] == self.lista_id[count]:
            lista_amigos.append(dicionario['nome'])
      count += 1

    lista_amigos = sorted(lista_amigos)

    print(f'O usuário {nome_usuario} tem um total de {conexoes} conexões, seus amigos são:', end='')
    for amigo in lista_amigos:
      if amigo != lista_amigos[-1]:
        print(f' {amigo},', end='')
      else:
        print(f' {amigo}.')

class Main:
  cinterage = CInterage()
  json_usuarios = input()
  cinterage.transformar_json_lista_dic(json_usuarios)
  tuplas = input()
  cinterage.transformar_tupla_lista(tuplas)
  id_usuario = int(input())
  cinterage.analise_usuario(id_usuario)