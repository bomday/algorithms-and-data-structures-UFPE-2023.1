class Brazino:
  def __init__(self, tamanho, partidas_disponiveis): 
    self.tamanho = tamanho #tamanho disponível da lista
    self.partidas_disponiveis = partidas_disponiveis #número de partidas disponíveis por índice da lista
    self.lista_timestamp_hash = ['' for timestamp in range(tamanho)] #tabela hash em estrutura de lista
    self.lista_partidas = [[] for partida in range(tamanho)] #lista com partidas de cada timestamp 

  def pegar_indice(self, timestamp): #retorna o índice que elemento ficará na lista
    return timestamp % self.tamanho #retorna o índice

  def inserir_partida(self, timestamp, partida, indice_partida=None): #faz processo para inserir ou não partida
    if indice_partida == None:
      indice_partida = self.pegar_indice(timestamp)
    
    if self.lista_timestamp_hash[indice_partida] == '': #cria timestamp se índice não tiver nenhum
      self.lista_timestamp_hash[indice_partida] = timestamp #coloca timestamp no índice indicado
      self.lista_partidas[indice_partida].append(partida) #adiciona partida na lista de partidas do timestamp indicado
    elif self.lista_timestamp_hash[indice_partida] == timestamp: #processo de adição para timestamps iguais
        if len(self.lista_partidas[indice_partida]) < self.partidas_disponiveis: #adiciona partida se ainda houver espaço
          self.lista_partidas[indice_partida].append(partida)
        else:
          print(f'partida: {partida} não foi adicionada por falta de espaço na lista!')
    else: #quando timestamps não são iguais
        if timestamp in self.lista_timestamp_hash: #insere partida no timestamp específico se ele estiver em outro local da lista
          indice_atual = self.lista_timestamp_hash.index(timestamp)
          self.inserir_partida(timestamp, partida, indice_atual)
        else: #busca espaço vazio na tabela
          indice_atual = (indice_partida + 1) % self.tamanho
          while self.lista_timestamp_hash[indice_atual] != '' and indice_atual != indice_partida: #vai buscar espaço vazio
            indice_atual = (indice_atual + 1) % self.tamanho
          
          if indice_atual != indice_partida: #chama função de inserir com o indice encontrado vazio
            self.inserir_partida(timestamp, partida, indice_atual)
          else:
            print(f'partida: {partida} não foi adicionada por falta de espaço na hashtable!')

  def remover_partida_unica(self, timestamp, partida): #faz processo para remover uma única partida 
    if timestamp in self.lista_timestamp_hash: #remove se timestamp dado existir no armazenamento
      indice_timestamp = self.lista_timestamp_hash.index(timestamp)
      if partida in self.lista_partidas[indice_timestamp]: #remove se partida estiver contida na lista de partidas do timestamp dado
        self.lista_partidas[indice_timestamp].remove(partida)
      else:
        print(f'partida: {partida} não foi removida porque não pertencia a lista!')
      
      if len(self.lista_partidas[indice_timestamp]) <= 0:
        self.lista_timestamp_hash[indice_timestamp] = ''
    else:
        print('o sistema não está armazenando partidas nesse horario!')

  def remover_todas_partidas(self, timestamp): #faz processo para remover todas as partidas de uma timestamp
    if timestamp in self.lista_timestamp_hash:
      indice_timestamp = self.lista_timestamp_hash.index(timestamp)
      self.lista_timestamp_hash[indice_timestamp] = ''
      self.lista_partidas[indice_timestamp] = []
    else:
      print('o sistema não está armazenando partidas nesse horario!')

  def imprimir_partidas(self): #imprime partidas
    for count in range(self.tamanho):
      if self.lista_partidas[count] == []:
        lista_final_partidas = 'Vazio'
      else:
        lista_final_partidas = self.lista_partidas[count]
      print(f'Slot {count}: {lista_final_partidas}')

class Main: #roda o programa
  info_hash_table = input().split(' ')
  brazino = Brazino(int(info_hash_table[0]), int(info_hash_table[1]))

  comando = input().split(' ')

  while comando:
    try:
      if comando[0] == 'ADD':
        partida = input().split(' ', 1)
        while partida[0] != 'DONE':
          brazino.inserir_partida(int(partida[0]), partida[1])
          partida = input().split(' ', 1)
      if comando[0] == 'REM':
        partida = input().split(' ', 1)
        while partida[0] != 'DONE':
          brazino.remover_partida_unica(int(partida[0]), partida[1])
          partida = input().split(' ', 1)
      if comando[0] == 'REMT':
        brazino.remover_todas_partidas(int(comando[1]))
      if comando[0] == 'PRINT':
        if len(comando) > 1:
          brazino.imprimir_partidas(int(comando[1]))
        else:
          brazino.imprimir_partidas()
      
      comando = input().split(' ')
    except EOFError:
      comando = None