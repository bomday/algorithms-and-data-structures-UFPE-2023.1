class GrupinhosFutebol:
  def __init__(self, tamanho): 
    self.tamanho = tamanho #tamanho disponível da lista
    self.lista_grupinhos_hash = [[] for grupo in range(tamanho)] #tabela hash em estrutura de lista com listas dentro que irão conter índice e nome do aluno 

  def pegar_indice(self, nome_jogador): #retorna o índice que elemento ficará na lista
    valor_nome = 0 #irá comportar o valor da soma entre as letras do nome
    for letra in nome_jogador: #acrescenta à variável 'valor_nome' o valor correspondente a cada letra do nome
      valor_nome += ord(letra)
    return valor_nome % self.tamanho #retorna o índice

  def inserir_jogador(self, nome_jogador): #faz processo para inserir ou não jogador a um grupinho
    indice_jogador = self.pegar_indice(nome_jogador) 

    if self.lista_grupinhos_hash[indice_jogador] == []: #se índice não tem grupinho
      self.lista_grupinhos_hash[indice_jogador].append(nome_jogador)
      print(f'{nome_jogador} criou um grupinho')
    else: #se índice tem grupinho
      anagrama = True
      for letra in nome_jogador:
        if letra not in self.lista_grupinhos_hash[indice_jogador][0]:
          anagrama = False
          break
      
      if anagrama: #adiciona nome no grupinho se nome do jogador for anagrama dos nomes dos outros jogadores
        self.lista_grupinhos_hash[indice_jogador].append(nome_jogador)
        print(f'{nome_jogador} entrou no grupinho')
      else:
        print(f'{nome_jogador} tentou se entrosar, mas foi descoberto')

  def imprimir_lista_grupinhos(self): #imprime lista de alunos
    lista_final_grupinhos = []
    for grupo in self.lista_grupinhos_hash:
      if grupo != []:
        lista_final_grupinhos.append(grupo)
    print(f'Grupinhos:{lista_final_grupinhos}')

class Main: #roda o programa
  num_jogadores = int(input())
  grupinhos_futebol = GrupinhosFutebol(num_jogadores)
  comando = input()

  while comando != 'FIM':
    grupinhos_futebol.inserir_jogador(comando)
    comando = input()
  else:
    grupinhos_futebol.imprimir_lista_grupinhos()