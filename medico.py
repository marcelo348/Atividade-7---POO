from funcionario import Funcionario
from typing import List
import datetime

class Medico(Funcionario):
  def __init__(self, data: dict):
    f = open("logs.txt", "a")
    try:
      self.__emAtendimento = data["emAtendimento"]
      self.__especialidade = data["especialidade"]
      super().__init__(data["nome"], data["idade"], data["sexo"], data["id"])
    except ValueError as e:
      print(e)
      f.write("{}: Dados incorretos de Médico, favor preencher corretamente a ficha de inscrição\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))
    f.close()

    
  def getEmAtendimento(self) -> bool:
    return self.__emAtendimento
  def getEspecialidade(self) -> str:
    return self.__especialidade

  def setEmAtendimento(self, atendendo: bool):
    self.__emAtendimento = atendendo
  def setEspecialidade(self, especialidade):
    self.__especialidade = especialidade

class Interno(Medico):
  def __init__(self, data: dict):
    try:
      if data["tempoDeInternato"] >= datetime.datetime.now():
        self.__tempoDeInternato = data["tempoDeInternato"] - datetime.datetime.now()
      else:
        raise Exception("Favor fornecer uma data válida")
      self.__supervisor = data["supervisor"]
      self.__rotacao = data["rotacao"]
      super().__init__(data)
    except :
      print("Dados incorretos de Interno, favor preencher corretamente a ficha de inscrição")
    else:
      f = open("logs.txt", "a")
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))
      f.close()

  def getTempoDeInternato(self) -> datetime:
    return self.__tempoDeInternato
  def getSupervisor(self):
    return self.__supervisor
  def getRotacao(self):
    return self.__rotacao

  def setTempoDeInternato(self, tempoInternato):
    if tempoInternato >= datetime.datetime.now():
      self.__tempoDeInternato = tempoInternato - datetime.datetime.now()
    else:
      raise Exception("Favor fornecer uma data válida")


class Titular(Medico):
  def __init__(self, data: dict):
    try:
      f = open("logs.txt", "a")
      super().__init__(data)
      if (type(data["crm"]) and type(data["areaAtuacao"])) is str:
        self.__crm = data["crm"]
        self.__areaAtuacao = data["areaAtuacao"]
        
      else:
        raise Exception("dados enviados estão com tipos incorretos")
    except:
      f.write("{}: Dados incorretos de Médico Titular, favor preencher corretamente a ficha de inscrição\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))

    f.close()

  def getCrm(self) -> str:
    return self.__crm
  def getAreaAtuacao(self) -> str:
    return self.__areaAtuacao

  def reCadastroTitular(self, data: dict):
    self.__crm = data["crm"]
    self.__areaAtuacao = data["areaAtuacao"]

  def setAreaAtuacao(self, areaAtuacao):
    self.__areaAtuacao = areaAtuacao

class Residente(Titular):
  def __init__(self, data: dict):
    try:
      f = open("logs.txt", "a")
      super().__init__(data)
      self.__supervisor = data["supervisor"]
    except:
      f.write("{}: Dados incorretos de Residente, favor preencher corretamente a ficha de inscrição\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))

    f.close()

  def getSupervisor(self) -> Titular:
    return self.__supervisor
  
  def reCadastroTitular(self, data: dict):
    f = open("logs.txt", "a")
    try:
      # utiliza o método da superclasse para cadastrar dados gerais, para depois cadastrar dados especificos
      self.__supervisor = data["supervisor"]
      super().reCadastroTitular(data)
    except:
      f.write("{}: Recadastro de Residente incompletos, favor preenchê-los integralmente\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))
    f.close()

class Cirurgiao(Titular):
  def __init__(self, data: dict):
    try:
      f = open("logs.txt", "a")
      self.__inicioDeCarreira = data["inicioDeCarreira"] #data de início do profissional na área de atuação
      self.__equipeCirurgica = data["equipeCirurgica"]
      super().__init__(data)
    except:
      f.write("{}: Dados incorretos de Residente, favor preencher corretamente a ficha de inscrição\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))

    f.close()

  def getInicioDeCarreira(self) -> datetime:
    return self.__inicioDeCarreira
  def getEquipeCirurgica(self) -> List[Titular]:
    try:
      return self.__equipeCirurgica
    except:
      raise Exception("Dados não são listas de Médicos titulares, favor preencher corretamente")

  def addMembroEquipe(self, membro: Titular):
    try:
      f = open("logs.txt", "a")
      self.__equipeCirurgica.append(membro)
    except:
      f.write("{}: Favor inserir dados corretamente\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Membro cadastrado com sucesso!\n".format(datetime.datetime.now()))

    f.close()

  def removeMembroEquipe(self, membro: Titular):
    try:
      f = open("logs.txt", "a")
      self.__equipeCirurgica.remove(membro)
    except:
      f.write("{}: Médico não encontrado, favor colocar cadastro válido\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Membro removido com sucesso.\n".format(datetime.datetime.now()))
    f.close()
  
  def reCadastroTitular(self, data: dict):
    try:
      # utiliza o método da superclasse para cadastrar dados gerais, para depois cadastrar dados especificos
      f = open("logs.txt", "a")
      self.__inicioDeCarreira = data["inicioDeCarreira"]
      self.__equipeCirurgica = data["equipeCirurgica"]
      super().reCadastroTitular(data)
    except:
      f.write("{}: Recadastro de Cirurgião incompletos, favor preenchê-los integralmente".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))

    f.close()

class MedicoClinico(Titular):
  def __init__(self, data: dict):
    f = open("logs.txt", "a")
    try:
      super().__init__(data)
      self.__endereco = data["enderecoClinica"]
    except:
      f.write("{}: Dados incorretos de Médico Geral, favor preencher corretamente a ficha de inscrição\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))
    f.close()

  def getEndereco(self):
    return self.__endereco
  def reCadastroTitular(self, data: dict):
    f = open("logs.txt", "a")
    try:
      # utiliza o método da superclasse para cadastrar dados gerais, para depois cadastrar dados especificos
      
      super().reCadastroTitular(data)
      self.__endereco = data["enderecoClinica"]

    except:
      f.write("{}: Recadastro de Médico Geral incompletos, favor preenchê-los integralmente\n".format(datetime.datetime.now()))
    else:
      f.write("{}: Dados cadastrados com sucesso!\n".format(datetime.datetime.now()))
    f.close()