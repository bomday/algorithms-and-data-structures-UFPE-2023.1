def catch_necklace_sum(num_rooms, necklace_value):
  #caso o número de salas seja zero
  if num_rooms == 0:
    return 0
  #caso tenha apenas uma sala
  elif num_rooms == 1:
    return int(necklace_value[0])
  #caso tenha uma ou mais salas
  else:
    #grava as duas primeiras somas máximas para próximas comparações
    necklace_sums = [int(necklace_value[0]), max(int(necklace_value[0]), int(necklace_value[1]))]
    #começa a partir do índice 2 dos colares, fazendo comparação com os valores máximos encontrados anteriormente
    for index in range(2, num_rooms):
      #acrescenta valor máximo atual ao final da lista
      necklace_sums.append(max(necklace_sums[1], necklace_sums[0] + int(necklace_value[index])))
      #remove o primeiro elemento que não vai mais ser comparado
      necklace_sums.remove(necklace_sums[0])
    
    #retorna o último valor máximo
    return necklace_sums[1]

num_rooms = int(input())
necklace_value = input().split()
necklace_sum = catch_necklace_sum(num_rooms, necklace_value)

print(f"{necklace_sum} colares podem ser retirados.")