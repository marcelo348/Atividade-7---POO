class Funcionario:
  def __init__(self, nome: str, idade: int, sexo: str, id: int) -> None:
    self.__nome = nome
    self.__idade = idade
    self.__sexo = sexo
    self.__id = id

  def getNome(self) -> str:
    return self.__nome
  def getIdade(self) -> int:
    return self.__idade
  def getSexo(self) -> str:
    return self.__sexo
  def getId(self) -> int:
    return self.__id

  def setNome(self, nome):
    self.__nome = nome
  def setIdade(self, idade):
    self.__idade = idade
  def setSexo(self, sexo):
    self.__sexo = sexo
    
  def atualizarCadastro(self, novoNome: str, novaIdade: int, novoSexo: str, novoId: int) -> None:
    self.__nome = novoNome
    self.__idade = novaIdade
    self.__sexo = novoSexo
    self.__id = novoId
  
