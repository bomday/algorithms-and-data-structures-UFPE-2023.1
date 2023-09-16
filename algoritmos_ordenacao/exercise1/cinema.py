lista1 = input().split(',')
lista2 = input().split(',')

def juntar_listas_ordenadas(lista1, lista2): #vai juntar as listas de forma ordenada
  topo_lista1, topo_lista2 = 0, 0 #inicia analise pelo primeiro índice de cada lista
  lista_geral_nao_ordenada = lista1 + lista2 #calcula tamanho total da lista final
  lista_geral = [] #armazena a lista geral formada
  
  for count in range(len(lista_geral_nao_ordenada)): #faz processo de adição de elementos na lista geral de forma ordenada
    if topo_lista1 >= len(lista1): #quando todos os elementos da lista 1 já foram adicionados na lista geral
      lista_geral.append(lista2[topo_lista2])
      topo_lista2 += 1
    elif topo_lista2 >= len(lista2): #quando todos os elementos da lista 2 já foram adicionados na lista geral
      lista_geral.append(lista1[topo_lista1])
      topo_lista1 += 1
    elif lista1[topo_lista1] < lista2[topo_lista2]: #quando elemento da lista1 é menor que o da lista2
      lista_geral.append(lista1[topo_lista1])
      topo_lista1 += 1
    else: #quando elemento da lista2 é menor que o da lista1
      lista_geral.append(lista2[topo_lista2])
      topo_lista2 += 1
  
  return lista_geral #retorna a lista geral formada

lista_final_ordenada = juntar_listas_ordenadas(lista1, lista2)
filme_mediana = len(lista_final_ordenada)//2 #calcula mediana da lista final

print(f'Os amigos decidiram assistir a {lista_final_ordenada[filme_mediana]} que estava na posição {filme_mediana+1} da lista.')