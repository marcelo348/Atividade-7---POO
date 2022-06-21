from funcionario import Funcionario

class Suporte(Funcionario):
  def __init__(self, data):
    try:
      self.__area = data["area"]
      self.__secoesAtendidas = data["secoesAtendidas"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Suporte, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!\n")

  def getArea(self):
    return self.__area
  def getSecoesAtendidas(self):
    return self.__secoesAtendidas
  def alterarArea(self, novaArea):
    self.__area = novaArea
  def alterarSecoes(self, novaSecao):
    self.__secoesAtendidas.append(novaSecao)
  def addEntregas(self):
    self.__totalMedEntregues = self.__totalMedEntregues + 1
  def removeEntrega(self):
    self.__totalMedEntregues = self.__totalMedEntregues - 1

class Farmaceutico(Suporte):
  def __init__(self, data):
    try:
      self.__totalMedEntregues = data["totalMedEntregues"]
      self.__estoqueMeds = data["estoqueMeds"]
      super().__init__(data)
    except:
      print("Dados incorretos de Farmaceutico, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!\n")
  def getEstoque(self):
    return self.__estoqueMeds
  def getTotalMedEntregues(self):
    return self.__totalMedEntregues
  def addEntregas(self):# Farmaceutico entrega 2 pedidos por vez
    self.__totalMedEntregues = self.__totalMedEntregues + 2
  def removeEntrega(self):
    self.__totalMedEntregues = self.__totalMedEntregues - 2
    
class Entregador(Suporte):
  def __init__(self, data):
    try:
      self.__totalEntregas = data["totalEntregas"]
      super().__init__(data)
    except:
      print("Dados incorretos de Entregador, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!\n")
  def getTotalEntregas(self):
    return self.__totalEntregas
  def addEntregas(self):
    self.__totalEntregas = self.__totalEntregas + 5# entregador entrega 5 pedidos por vez
  def removeEntrega(self):
    self.__totalEntregas = self.__totalEntregas - 5

class Zelador(Suporte):
  def __init__(self, data):
    try:
      self.__totalQuartoResponsaveis = data["totalQuartoResponsaveis"]
      super().__init__(data)
    except:
      print("Dados incorretos de Zelador, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!\n")
  def getTotalQuarto(self):
    return self.__totalQuartoResponsaveis
  def setTotalQuarto(self, novoTotal):
    self.__totalQuartoResponsaveis = novoTotal

