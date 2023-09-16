probabilidades_suspeitos = input().split()
probabilidades_suspeitos = [int(probabilidade) for probabilidade in probabilidades_suspeitos]
tamanho_lista = len(probabilidades_suspeitos)
tempos_gastos = [] #ordem: isabela -> mateus -> joaquim -> bianca
participantes = ['Isabela', 'Mateus', 'Joaquim', 'Bianca']

tempo_isabela = 0 
tempo_mateus = 0
tempo_joaquim = 0
tempo_bianca = 0

def heapsort(lista, tamanho_lista):
  lista_manipulada = lista[:]
  #criando um MaxHeap com elementos da lista
  aux = tamanho_lista//2 - 1
  for index in range(aux, -1, -1): #percorre elementos que não são folhas
    heapsort_max(lista_manipulada, tamanho_lista, index)

def heapsort_max(lista, tamanho_lista, index):
  global tempo_isabela
  maior_atual = index #recebe pai
  maior_atual_esq = 2 * index + 1 #recebe filho à esquerda
  maior_atual_dir = 2 * index + 2 #recebe filho à direita

  #se filho à esquerda existir e for maior que pai, faz a troca
  tempo_isabela += 1
  if maior_atual_esq < tamanho_lista and lista[maior_atual] < lista[maior_atual_esq]:
    maior_atual = maior_atual_esq

  #se filho à direita existir e for maior que pai, faz a troca
  tempo_isabela += 1
  if maior_atual_dir < tamanho_lista and lista[maior_atual] < lista[maior_atual_dir]:
    maior_atual = maior_atual_dir

  tempo_isabela += 1
  #se houve troca de pai
  if maior_atual != index:
    tempo_isabela += 2
    lista[index], lista[maior_atual] = lista[maior_atual], lista[index]  #faz troca de lugares
    heapsort_max(lista, tamanho_lista, maior_atual)

#quicksort
def quicksort(lista, tamanho_lista, inicio=0, fim=None):
  lista_manipulada = lista[:]

  if fim is None:
    fim = tamanho_lista-1
  if inicio < fim:
    #encontra nova posição do elemento (pivot) que servirá de comparação e registra o tempo gasto
    posicao_pivot = encontra_posicao_pivot(lista_manipulada, inicio, fim)
    #faz reorganização na sublista à esquerda do pivot
    quicksort(lista_manipulada, tamanho_lista, inicio, posicao_pivot-1)
    #faz reorganização na sublista à direita do pivot
    quicksort(lista_manipulada, tamanho_lista, posicao_pivot+1, fim)

def encontra_posicao_pivot(lista, inicio, fim):
  global tempo_mateus
  pivot = lista[fim]
  posicao_pivot = inicio

  for item_analisado in range(inicio, fim):
    #busca a nova posição do pivot enquanto os elementos são menores ou iguais ao pivot
    tempo_mateus += 1
    if lista[item_analisado] <= pivot: 
      tempo_mateus += 2
      lista[item_analisado], lista[posicao_pivot] = lista[posicao_pivot], lista[item_analisado]
      posicao_pivot = posicao_pivot + 1
  #muda pivot para a nova posição
  tempo_mateus += 2
  lista[posicao_pivot], lista[fim] = lista[fim], lista[posicao_pivot] 

  return posicao_pivot

#selectionsort
def selectionsort(lista, tamanho_lista):
  global tempo_joaquim
  lista_manipulada = lista[:]

  for index in range(tamanho_lista-1):
    min_index = index
    #encontra indíce do valor mínimo 
    for i in range(index + 1, tamanho_lista):
      tempo_joaquim += 1 #fez comparação
      if lista_manipulada[i] < lista_manipulada[min_index]: 
        min_index = i
    #faz troca de posições se o mínimo encontrado for menor que o elemento no índice atual
    if lista_manipulada[min_index] < lista_manipulada[index]:
      tempo_joaquim += 2 #fez troca
      antigo_minimo = lista_manipulada[index]
      lista_manipulada[index] = lista_manipulada[min_index]
      lista_manipulada[min_index] = antigo_minimo

#shellsort
def shellsort(lista, tamanho_lista):
  global tempo_bianca
  lista_manipulada = lista 
  range_comparacao = tamanho_lista//2

  while range_comparacao > 0:
    for index in range(range_comparacao, tamanho_lista):
      item_comparacao = lista_manipulada[index]
      index_comparacao = index
      #faz troca de posições 
      if index_comparacao >= range_comparacao:
        tempo_bianca+= 1
      while index_comparacao >= range_comparacao and lista_manipulada[index_comparacao] < lista_manipulada[index_comparacao - range_comparacao]:
        tempo_bianca += 1 #fez comparação
        tempo_bianca += 2 #fez troca
        lista_manipulada[index_comparacao] = lista_manipulada[index_comparacao - range_comparacao]
        index_comparacao -= range_comparacao
      lista_manipulada[index_comparacao] = item_comparacao
    range_comparacao = range_comparacao//2

#heapsort
heapsort(probabilidades_suspeitos, tamanho_lista)
tempos_gastos.append(tempo_isabela)
#quicksort
quicksort(probabilidades_suspeitos, tamanho_lista)
tempos_gastos.append(tempo_mateus)
#selectionsort
selectionsort(probabilidades_suspeitos, tamanho_lista)
tempos_gastos.append(tempo_joaquim)
#shellsort
shellsort(probabilidades_suspeitos, tamanho_lista)
tempos_gastos.append(tempo_bianca)
#ordenando os tempos gastos para saber o menor
tempos_ordenados = sorted(tempos_gastos)
qtd_vencedor = 1

#confere se houve empate
for tempo in range(1, 4):
  if tempos_ordenados[0] == tempos_ordenados[tempo]:
    qtd_vencedor += 1

if qtd_vencedor == 1: #faz print de um vencedor
  vencedor_index = tempos_gastos.index(tempos_ordenados[0])
  print(f'{participantes[vencedor_index]} vai assistir o filme da Barbie com seu combo novo após levar {tempos_ordenados[0]} minutos para descobrir o assassino.')
else: #faz print de empate
  vencedor_index = 0
  for tempo in tempos_gastos:
    if tempo == tempos_ordenados[0] and qtd_vencedor > 1:
      qtd_vencedor -= 1 #diminui quantidade de vencedores a serem impressos
      print(f'{participantes[vencedor_index]}, ', end='')
    elif tempo == tempos_ordenados[0] and qtd_vencedor == 1:
      print(f'{participantes[vencedor_index]} vão assistir o filme da Barbie com seu combo novo após levar {tempos_ordenados[0]} minutos para descobrir o assassino.')
    vencedor_index += 1