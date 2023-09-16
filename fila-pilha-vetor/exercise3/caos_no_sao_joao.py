class Cliente: #cria novos clientes
  def __init__(self, pessoa, dinheiro, proxima_pessoa = None, anterior_pessoa = None): 
    self.pessoa = pessoa
    self.dinheiro = dinheiro
    self.proxima_pessoa = proxima_pessoa
    self.anterior_pessoa = anterior_pessoa

class Caixas: #cria novos caixas
  dinheiro_arrecadado = 0

  def __init__(self, num): 
    self.num = num
    self.primeira_pessoa = None
    self.ultima_pessoa = None

  def tamanho_fila(self): #calcula e retorna quantas pessoas estão na fila
    pessoas_na_fila = 0
    pessoa_atual = self.primeira_pessoa
    
    while pessoa_atual != None:
      pessoas_na_fila+=1 
      pessoa_atual= pessoa_atual.proxima_pessoa
    
    return pessoas_na_fila

  def adiciona_cliente_fila(self, pessoa, dinheiro): #adiciona cliente na fila
    if self.primeira_pessoa is None:
      self.ultima_pessoa = self.primeira_pessoa = Cliente(pessoa, dinheiro)
    else:
      self.ultima_pessoa.proxima_pessoa = Cliente(pessoa, dinheiro, None, self.ultima_pessoa)
      self.ultima_pessoa = self.ultima_pessoa.proxima_pessoa

  def retira_ultimo_cliente(self): #retira último cliente da fila
    if self.ultima_pessoa.anterior_pessoa is not None:
      penultima_pessoa = self.ultima_pessoa.anterior_pessoa
      penultima_pessoa.proxima_pessoa = None
      pessoa_retirada = self.ultima_pessoa
      self.ultima_pessoa = penultima_pessoa
      return pessoa_retirada
    else:
      pessoa_retirada = self.ultima_pessoa
      self.ultima_pessoa = self.primeira_pessoa = None
      return pessoa_retirada

  def chama_cliente(self, caixa_atual, outro_caixa): #chama próximo cliente, controlando fila atual e fila adicional (quando não há mais clientes)
    tamanho_fila = self.tamanho_fila()

    if tamanho_fila != 0:
      print(f"{self.primeira_pessoa.pessoa} foi chamado para o caixa {caixa_atual.num}")

      self.adiciona_dinheiro_caixa(self.primeira_pessoa.dinheiro)
      self.primeira_pessoa = self.primeira_pessoa.proxima_pessoa
      if self.primeira_pessoa == None:
        self.ultima_pessoa = None
            
      self.chama_cliente
    else:
      tamanho_fila_outro_caixa = outro_caixa.tamanho_fila()

      if tamanho_fila_outro_caixa != 0:
        num_pessoas_adicionar_na_fila = tamanho_fila_outro_caixa/2
        if int(num_pessoas_adicionar_na_fila) < num_pessoas_adicionar_na_fila:
          num_pessoas_adicionar_na_fila = int(num_pessoas_adicionar_na_fila) + 1

        for cliente in range(int(num_pessoas_adicionar_na_fila)):
          pessoa_retirada = outro_caixa.retira_ultimo_cliente()
          self.adiciona_cliente_fila(pessoa_retirada.pessoa, pessoa_retirada.dinheiro)
                
        self.chama_cliente(caixa_atual, outro_caixa)

  def adiciona_dinheiro_caixa(self, dinheiro): #acrescenta dinheiro no caixa
    self.dinheiro_arrecadado += dinheiro

  def get_dinheiro_arrecadado(self): #retorna valor no caixa
    return self.dinheiro_arrecadado

class Main:
  caixa1 = Caixas(1)
  caixa2 = Caixas(2)
  acao = [''] 
  
  while acao[0] != "FIM": #Faz loop para receber comandos até finalização do código
    acao = input().split(' ')
    
    #realiza as chamadas de acordo com os inputs
    if acao[0] != "FIM":
      if acao[0] == "ENTROU:":
        #separa varíaveis para ação "ENTROU"
        pessoa = acao[1]
        dinheiro = float(acao[3])
        caixa = int(acao[2])
        
        print(f"{pessoa} entrou na fila {caixa}")
        
        if caixa == 1:
          caixa1.adiciona_cliente_fila(pessoa, dinheiro)
        else:
          caixa2.adiciona_cliente_fila(pessoa, dinheiro)
      elif acao[0] == "PROXIMO:":
        #separa varíaveis para ação "PROXIMO"
        caixa = int(acao[1])
        
        if caixa == 1:
          caixa1.chama_cliente(caixa1, caixa2)
        else:
          caixa2.chama_cliente(caixa2, caixa1)
  
  dinheiro_arrecadado_caixa1 = caixa1.get_dinheiro_arrecadado()
  dinheiro_arrecadado_caixa2 = caixa2.get_dinheiro_arrecadado()

  print(f"Caixa 1: R$ {dinheiro_arrecadado_caixa1:.2f}, Caixa 2: R$ {dinheiro_arrecadado_caixa2:.2f}")