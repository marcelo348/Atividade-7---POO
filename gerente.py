from funcionario import Funcionario
from atendente import Atendente
from typing import List

class Gerente(Funcionario):
  def __init__(self, data:dict):
    try:
      self.__nivel = data["nivel"]
      self.__funcionarios = data["funcionarios"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except:
      print("Dados incorretos de Gerente, favor preencher corretamente a ficha de inscrição")
    else:
      print("Dados cadastrados com sucesso!")

  def getNivel(self) -> int:
    return self.__nivel
  def getFuncionarios(self) -> List[Atendente]:
    try:
      return self.__funcionarios
    except:
      raise Exception("Dados não são listas de atendentes, favor preencher corretamente")

  def getSpecificFunc(self, i) -> Atendente:
    try:
      print("\
       nome: {}\n \
      idade: {} anos\n \
      sexo: {}\n \
      id: {}º\n \
      setor: {}\n \
      Carga horária: {} horas\n \
      ".format(self.getFuncionarios()[i].getNome(), self.getFuncionarios()[i].getIdade(),
              self.getFuncionarios()[i].getSexo(), self.getFuncionarios()[i].getId(),
              self.getFuncionarios()[i].getSetor(), self.getFuncionarios()[i].getCargaHoraria()))
      return self.getFuncionarios()[i]
    except:
      raise Exception("Atendente não encontrado")
      return []

  
  def setNivel(self, nivel):
    self.__nivel = nivel

  
  def addFuncionario(self, funcionario: dict):
    self.__funcionarios.append(funcionario)

  def removeFuncionario(self, funcionario: dict):
    self.__funcionarios.remove(funcionario)