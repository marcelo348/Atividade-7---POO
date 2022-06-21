from funcionario import Funcionario

class Consultor(Funcionario):
  def __init__(self, data):
    try:
      self.__especialidade = data["especialidade"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Consultor, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def getEspecialidade(self):
    return self.__especialidade
  def alterarEspecialidade(self, novaEspecialidade):
    self.__especialidade = novaEspecialidade

class ConsultJuridico(Consultor):
  def __init__(self, data):
    try:
      self.__casosResponsaveis = data["casos"]
      super().__init__(data)
    except:
      print("Dados incorretos de Consultor Jurídico, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getCasos(self):
    return self.__casosResponsaveis
  def addCaso(self, casoNovo):
    self.__casosResponsaveis.append(casoNovo)
  def removeCaso(self, casoRemovido):
    self.__casosResponsaveis.remove(casoRemovido)
    
class ConsultFinanceiro(Consultor):
  def __init__(self, data):
    try:
      self.__setorResponsavel = data["setor"]
      super().__init__(data)
    except:
      print("Dados incorretos de Consultor Financeiro, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getSetor(self):
    return self.__setorResponsavel
  def mudaSetor(self, novoSetor):
    self.__setorResponsavel = novoSetor

class ConsultTecnologico(Consultor):
  def __init__(self, data):
    try:
      self.__tecnologiaResponsavel = data["tecnologiasResponsaveis"]
      self.__setorResponsavel = data["setor"]
      super().__init__(data)
    except:
      print("Dados incorretos de Consultor Tecnológico, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  def getTecnologias(self) -> list:
    return self.__tecnologiaResponsavel
  def getSetor(self):
    return self.__setorResponsavel
  def mudaSetor(self, __setorResponsavel):
    return self.__setorResponsavel
  def addTecnologia(self, tecnologiaNova):
    self.__tecnologiaResponsavel.append(tecnologiaNova)
  def removeTecnologia(self, tecnologiaRemovida):
    self.__tecnologiaResponsavel.remove(tecnologiaRemovida)
