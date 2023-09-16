posicao = int(input())
lista_assentos = input().split()

def ordenando_bubble_sort(lista_assentos):
  total_assentos = len(lista_assentos)
  nao_houve_trocas = 0 #armazena o numero de trocas não realizadas naquela rodada
  
  for assento in range(total_assentos-1): #faz reorganização de lista percorrendo o (tamanho da lista - 1) vezes
    for item in range(total_assentos-1-assento): #pega um assento e compara com os outros
      #faz troca com o item seguinte
      if lista_assentos[item][0] == lista_assentos[item+1][0]: #compara se a letra do assento atual é igual a do assento seguinte 
        
        if len(lista_assentos[item]) <= 2: #se o número do assento possui apenas um caracter 
          if len(lista_assentos[item+1]) <= 2: #se o número do assento seguinte possui apenas um caracter 
            if lista_assentos[item] > lista_assentos[item+1]:
              lista_assentos[item], lista_assentos[item+1] = lista_assentos[item+1], lista_assentos[item]
            else:
              nao_houve_trocas +=1
          else:
            nao_houve_trocas +=1
        else: #se o número do assento possui mais de um caracter
          if len(lista_assentos[item+1]) > 2: #se o número do assento seguinte possui mais de um caracter
            if int(lista_assentos[item][1:]) > int(lista_assentos[item+1][1:]):
                lista_assentos[item], lista_assentos[item+1] = lista_assentos[item+1], lista_assentos[item]
            else:
                nao_houve_trocas +=1
          else: #se o número do assento seguinte possui apenas um caracter
            lista_assentos[item], lista_assentos[item+1] = lista_assentos[item+1], lista_assentos[item]
        
      elif lista_assentos[item][0] > lista_assentos[item+1][0]: #compara se a letra do assento atual é maior que do assento seguinte 
        lista_assentos[item], lista_assentos[item+1] = lista_assentos[item+1], lista_assentos[item]
      else:
        nao_houve_trocas +=1
    
    if nao_houve_trocas == (total_assentos-1):
      break
    else:
      nao_houve_trocas = 0

ordenando_bubble_sort(lista_assentos)
if len(lista_assentos[posicao-1]) <= 2: #se o número do assento possui apenas um caracter 
  num_poltrona = lista_assentos[posicao-1][1]
else: #se o número do assento possui mais de um caracter 
  num_poltrona = lista_assentos[posicao-1][1] + lista_assentos[posicao-1][2]

print(f'O vencedor está na fila {lista_assentos[posicao-1][0]} poltrona {num_poltrona}!')