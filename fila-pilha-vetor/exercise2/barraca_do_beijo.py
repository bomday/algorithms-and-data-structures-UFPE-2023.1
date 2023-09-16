class Beijo: #controla beijos presentes
  def __init__(self, beijo, proximo_beijo = None, anterior_beijo = None): 
    self.beijo = beijo
    self.proximo_beijo = proximo_beijo
    self.anterior_beijo = anterior_beijo

class PerfilUsuario: #controla Perfil com métodos para cada comando
  def __init__(self): 
    self.nome = None
    self.primeiro_beijo = None
    self.ultimo_beijo = None
  
  def set_nome(self, nome): #adiciona nome do usuário
    self.nome = nome

  def adiciona_beijo(self, beijo): #adiciona beijos na pilha
    if self.primeiro_beijo is None:
      self.ultimo_beijo = self.primeiro_beijo = Beijo(beijo)
    else:
      beijo_existe = self.busca_beijo_existe(beijo)
      if not beijo_existe: #adiciona apenas se a pessoa já não foi adicionada na lista
        self.ultimo_beijo.proximo_beijo = Beijo(beijo, None, self.ultimo_beijo)
        self.ultimo_beijo = self.ultimo_beijo.proximo_beijo
  
  def adiciona_superbeijo(self, beijo): #adiciona superbeijo na pilha
    beijo_existe = self.busca_beijo_existe(beijo)
    
    if beijo_existe: 
      self.deleta_beijo(beijo)
    
    self.adiciona_beijo(beijo)
  
  def deleta_beijo(self, beijo): #deleta beijo da pilha
    beijo_atual = self.primeiro_beijo
    while beijo_atual is not None:
      if beijo_atual.beijo == beijo:
        if beijo_atual == self.primeiro_beijo:
          self.primeiro_beijo.beijo = beijo
        elif beijo_atual == self.ultimo_beijo:
          self.ultimo_beijo.beijo = beijo
        
        beijo_anterior = beijo_atual.anterior_beijo
        proximo_beijo = beijo_atual.proximo_beijo
        
        if beijo_anterior is not None:
          beijo_anterior.proximo_beijo = proximo_beijo
        else:
          self.primeiro_beijo = proximo_beijo
        
        if proximo_beijo is not None:
          proximo_beijo.anterior_beijo = beijo_anterior
        else:
          self.ultimo_beijo = beijo_anterior
      
      beijo_atual = beijo_atual.proximo_beijo
  
  def busca_beijo_existe(self, beijo): #verifica se beijo existe
    beijo_atual = self.primeiro_beijo
    while beijo_atual is not None:
      if beijo_atual.beijo == beijo:
        return True
      beijo_atual = beijo_atual.proximo_beijo
    
    return False

  def historico_beijos(self): #fornece histórico de beijos do último ao primeiro
    if self.ultimo_beijo is None:
      print("Histórico vazio.")
    else:
      beijo_atual = self.ultimo_beijo
      while beijo_atual is not None:
        print(beijo_atual.beijo)
        beijo_atual = beijo_atual.anterior_beijo
  
class Main: #recebe os inputs
  usuario = PerfilUsuario()
  acao = [''] 
  
  while acao[0] != "FIM": #Faz loop para receber comandos até finalização do código
    acao = input().split(' ')
    
    if acao[0] != "FIM":
      if acao[0] == "NOME":
        usuario.set_nome(acao[1])
      elif acao[0] == "BEIJO":
        usuario.adiciona_beijo(acao[1])
      elif acao[0] == "SUPERBEIJO":
        usuario.adiciona_superbeijo(acao[1])
      elif acao[0] == "XODÓ":
        usuario.deleta_beijo(acao[1])
      elif acao[0] == "MOSTRAR":
        usuario.historico_beijos()
  
  print(f"O histórico final do usuário {usuario.nome} é:")
  usuario.historico_beijos()