from funcionario import Funcionario

class Enfermeiro(Funcionario):
  def __init__(self, data: dict):
    self.__turno = data["turno"]
    self.__enfermaria = data["enfermaria"]
    self.__coren = data["coren"]
    super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])

  def getTurno(self) -> str:
    return self.__turno
  def getEnfermaria(self) -> str:
    return self.__enfermaria
  def getCoren(self) -> int:
    return self.__coren

  def __setTurno(self, turno):
    self.__turno = turno
  def setEnfermaria(self, enfermaria):
    self.__enfermaria = enfermaria
  def __setCoren(self, coren):
    self.__coren = coren
  
class Tecnico(Enfermeiro):
  def __init__(self, data):
    self.__especialidadeEnf = data["especialidadeEnf"]
    super().__init__(data)

  def __getEspecialidadeEnf(self) -> str:
    return self.__especialidadeEnf

class Chefe(Enfermeiro):
  def __init__(self, data:dict):
    self.__equipe = data["equipe"]
    super().__init__(data)

  def getEquipe(self) -> list:
    return self.__equipe
