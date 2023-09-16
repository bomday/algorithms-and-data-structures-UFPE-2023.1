class Friend: #possui as informações e métodos para pular fogueira de um amigo
  
  def __init__(self, size=None, list_friend_infos=None, count=1, jump_time=0): #inicia amigo com informações vazias
    self.size = size #armazena o tamanho
    self.list_friend_infos = list_friend_infos #armazena lista de informação
    self.count = count #contador para parar a ação de pular fogueira
    self.jump_time = jump_time #conta quantidade de pulos
  
  def add_size_list(self, size_input): #adiciona informação de tamanho da lista
    self.size = size_input

  def add_info_list(self, list_input): #adiciona lista de informação
    self.list_friend_infos = list_input.split(' ')
  
  def jumpBonfire(self): #faz ação de pular fogueira e printar mensagens após resultado
    if int(self.list_friend_infos[self.count]) == 0 or self.count >= self.size: #outputs
      if int(self.list_friend_infos[self.count]) == 0 and self.count < self.size:
        print(f"Ah, que pena, {self.list_friend_infos[0]} não conseguiu!")
      else:
        print(f"{self.list_friend_infos[0]} conseguiu!")
        print(f"{self.list_friend_infos[0]} precisou pular {self.jump_time} fogueiras")
    else: #chamada recursiva para percorrer a lista de pulos
      self.count = self.count + int(self.list_friend_infos[self.count])
      if self.count > self.size:
        self.count = self.size
      self.jump_time+=1
      self.jumpBonfire()

class Main:
  for friend in range(0, 4): #faz loop para analisar cada amigo
    friend_jumping_bonfire = Friend()
    
    #inputs
    size = int(input())
    list_info = input()
    
    #utilizando métodos da classe Friend
    friend_jumping_bonfire.add_size_list(size)
    friend_jumping_bonfire.add_info_list(list_info)
    friend_jumping_bonfire.jumpBonfire()