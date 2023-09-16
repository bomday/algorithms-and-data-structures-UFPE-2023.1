def creating_routes(planets, routes=[], start=0, conections=[]):
  #adiciona conexão atual à lista de rotas
  routes.append(conections[:])

  for index_planet in range(start, len(planets)):
    #adiciona o planeta atual à conexão atual
    if planets[index_planet] != ' ':
        conections.append(planets[index_planet])
        #acessa próximas conexões a partir do último planeta atual
        creating_routes(planets, routes, index_planet + 1, conections)
        #remove o planeta atual para formação de próximas conexões
        conections.pop()

  return routes #retorna rota final

planets_list = input().split(', ')
planets_list = sorted(planets_list)
routes = creating_routes(planets_list)

print(f'O número de subsets de visitação é {len(routes)}\nSão eles: {routes}')