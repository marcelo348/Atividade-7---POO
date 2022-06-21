from funcionario import Funcionario

class Atendente(Funcionario):
  def __init__(self, data: dict):
    try:
      self.__setor = data["setor"]
      self.__cargaHoraria = data["cargaHoraria"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Atendente, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")
  
  def getSetor(self) -> str:
    return self.__setor
  def getCargaHoraria(self) -> str:
    return self.__cargaHoraria
  
  
  def setSetor(self, setor):
    self.__setor = setor
  def setCargaHoraria(self, cargaHoraria: float):
    self.__cargaHoraria = cargaHoraria

class Recepcionista(Atendente):
  def __init__(self, data: dict):
    try:
      self.__telefoneBancada = data["telefoneBancada"]
      super().__init__(data)
    except:
      print("Dados incorretos de Recepcionista, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def setTelefone(self, telefoneBancada):
    self.__telefoneBancada = telefoneBancada

  def getTelefone(self):
    return self.__telefoneBancada

class Seguranca(Atendente):
  def __init__(self, data: dict):
    try:
      self.__turno = data["turno"]
      super().__init__(data)
    except:
      print("Dados incorretos de Segurança, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def setTurno(self, turno: str):
    self.__turno = turno

  def getTurno(self) -> str:
    return self.__turno