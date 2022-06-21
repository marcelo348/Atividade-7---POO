from consultor import ConsultTecnologico, ConsultFinanceiro, ConsultJuridico
from medico import Interno, Titular, Cirurgiao, MedicoClinico, Residente
from suporte import Zelador, Entregador, Farmaceutico
from atendente import Recepcionista, Seguranca
from enfermeiro import Chefe, Tecnico
from gerente import Gerente


import random
import datetime

selecionar = int(input('Olá professora! A senhora tem as seguintes opções para checar a funcionalidade do nosso programa:\n \
  > Digite 1 para checar o funcionamento do código de enfermeiros\n \
  > Digite 2 para checar o funcionamento do código de médicos\n \
  > Digite 3 para checar o funcionamento do código de consultores\n \
  > Digite 4 para checar o funcionamento do código de atendentes e gerentes\n \
  > Digite 5 para checar o funcionamento do código de suporte\n '))


if selecionar == 1: 
  #dados vindos de uma API
  fichaTecnicosE3 = {
    0:{
      "nome": "Márcia",
      "idade": 31, 
      "sexo": "Mulher",
      "id": 3,
      "turno": "matutino",
      "enfermaria": "E03",
      "coren": "1755",
      "especialidadeEnf": "Fêmur"
    },
    1:{
      "nome": "Lúcio",
      "idade": 26, 
      "sexo": "Homem",
      "id": 4,
      "turno": "matutino",
      "enfermaria": "E03",
      "coren": "1541",
      "especialidadeEnf": "Braço"
    },
  }

  fichaTecnicosE4 = {
     0:{
      "nome": "André",
      "idade": 30, 
      "sexo": "Homem",
      "id": 5,
      "turno": "matutino",
      "enfermaria": "E04",
      "coren": 2674,
      "especialidadeEnf": "Fêmur"
    },
  }
  
  fichaChefe = {
    "nome": "Josiane",
    "idade": 51, 
    "sexo": "Mulher",
    "id": 2,
    "turno": "integral",
    "enfermaria": "E03",
    "coren": "1969",
    "equipe": []
  }

  fichaChefe["equipe"].append(fichaTecnicosE3)
  fichaChefe["equipe"].append(fichaTecnicosE4)

  josiane = Chefe(fichaChefe)

  print("\n{} é a chefe do departamento de Enfermaria do hospital, seu coren é {}, trabalha no turno {}\
        \n".format(josiane.getNome(), josiane.getCoren(), josiane.getTurno()))
  
  for i in range( len(fichaChefe["equipe"][0]) ):
    # o 0 significa que é o primeiro elemento da lista, ou seja, o dicionário dos técnicos da enfermaria E03
    print("Dados da {}º Enfermeira(o) da enfermaria E03:\n".format(i+1),josiane.getEquipe()[0][i], " \n") 

  
  marcia = Tecnico(fichaTecnicosE3[0])
  print("\n{} é a enfermeira da Enfermaria E03 do hospital, seu coren é {}, trabalha no turno {}\
        \n".format(marcia.getNome(), marcia.getCoren(), marcia.getTurno()))
  
elif selecionar == 2:
  fichaMedTitular = {
    0:{
      "nome": "Letícia",
      "idade": 44, 
      "sexo": "Mulher",
      "id": 8,
      "emAtendimento": False,
      "especialidade": "Generalista",
      "crm": "42070",
      "areaAtuacao": "Titular"
    },
    1:{
      "nome": "Marcelo",
      "idade": 31, 
      "sexo": "Homem",
      "id": 7,
      "emAtendimento": False,
      "especialidade": "Cirurgia",
      "crm": "6969",
      "areaAtuacao": "Titular"
    },
    2: {
      "nome": "Ricardo",
      "idade": 26, 
      "sexo": "Homem",
      "id": 27,
      "emAtendimento": False,
      "especialidade": "Nenhuma",
      "crm": "1378",
      "areaAtuacao": "Titular"
    },
  }
  leticia = Titular(fichaMedTitular[0])
  marcelo = Titular(fichaMedTitular[1])
  ricardo = Titular(fichaMedTitular[2])
  print("---------------------------------------------------------------------------------------------------------------------")
  print("\n{} é médica(o) titular do hospital, seu crm é {}\
        \n".format(marcelo.getNome(), marcelo.getCrm()))

  fichaInterno = {
    0:{
      "nome": "Gabriel",
      "idade": 24, 
      "sexo": "Homem",
      "id": 10,
      "emAtendimento": False,
      "especialidade": "Cirurgia",
      "supervisor": marcelo,
      "rotacao": "Cardiologia",
      "tempoDeInternato": datetime.datetime(2022, 12, 29)
    }
  }
  gabriel = Interno(fichaInterno[0])
  
  print("\n{} é interna(o) do hospital, atualmente está na rotação de {} com especialidade em {}, seu supervisor é {}\
        ".format(gabriel.getNome(), gabriel.getRotacao(), gabriel.getEspecialidade(), gabriel.getSupervisor().getNome()))
  print("\n{} remaign until the end of {}'s  internship\n".format(gabriel.getTempoDeInternato(), gabriel.getNome()))
  print("---------------------------------------------------------------------------------------------------------------------")
  '''
  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  A partir daqui é POLIMORFISMO
  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  '''
  fichaCirurgiao = {
    "nome": "Dr. House",
    "idade": 57, 
    "sexo": "Homem",
    "id": random.randint(1,25),
    "emAtendimento": False,
    "especialidade": "Cirurgião",
    "crm": "0666",
    "areaAtuacao": "Cardiologia",
    "inicioDeCarreira": datetime.datetime(1982, 3, 18),
    "equipeCirurgica": [leticia, marcelo]
  }
  cirurgiao = Cirurgiao(fichaCirurgiao)
  
  print("CIRURGIÃO: \n")
  print("\
    {} é um(a) {} com especialização em {}, seu crm é {}, teve início de sua carreira em {}\
 sua equipe tem os seguintes profissionais:\n \
        ".format(cirurgiao.getNome(), cirurgiao.getEspecialidade(), cirurgiao.getAreaAtuacao(), cirurgiao.getCrm(), cirurgiao.getInicioDeCarreira().year))

  cirurgiao.addMembroEquipe(ricardo)

  for equipe in cirurgiao.getEquipeCirurgica():
    print('\
      {}'.format(equipe.getNome()))
  print()
  fichaRecadastro = {
    "crm": "0005",
    "areaAtuacao": "Neurocirurgia",
    "inicioDeCarreira": datetime.datetime(2000, 1, 30),
    "equipeCirurgica": [leticia, marcelo]
  }

  cirurgiao.reCadastroTitular(fichaRecadastro)

  print("\
    {} é um(a) {} com especialização em {}, seu crm é {}, teve início de sua carreira em {}\
 e sua equipe tem os seguintes profissionais:\n \
        ".format(cirurgiao.getNome(), cirurgiao.getEspecialidade(), cirurgiao.getAreaAtuacao(), cirurgiao.getCrm(), cirurgiao.getInicioDeCarreira().year))
  
  for equipe in cirurgiao.getEquipeCirurgica():
    print('\
      {}'.format(equipe.getNome()))
  print()

  fichaClinico = {
    "nome": "Homero",
    "idade": 33, 
    "sexo": "Homem",
    "id": random.randint(26,50),
    "emAtendimento": False,
    "especialidade": "Clínico",
    "crm": "5412",
    "areaAtuacao": "Geral",
    "enderecoClinica": "Av. ACM Neto"
  }

  clinico = MedicoClinico(fichaClinico)


  print("CLÍNICO: \n")
  print("\
    {} é {} especialista {}, seu crm é {}, com uma clinica localizada na {}\n\
    ".format(clinico.getNome(), clinico.getEspecialidade(),clinico.getAreaAtuacao(), clinico.getCrm(), clinico.getEndereco()))

  fichaRecadastro = {
    "crm": "2204",
    "areaAtuacao": "Urologia",
    "enderecoClinica": "Av. Joana Angélica"
  }
  
  clinico.reCadastroTitular(fichaRecadastro)
  
  print("\
    {} é {} especialista em {}, seu crm é {}, com uma clinica localizada na {}\n\
    ".format(clinico.getNome(), clinico.getEspecialidade(),clinico.getAreaAtuacao(), clinico.getCrm(), clinico.getEndereco()))
  
  fichaResidente = {
    "nome": "Rafaela",
    "idade": 26, 
    "sexo": "Mulher",
    "id": random.randint(51,75),
    "emAtendimento": False,
    "especialidade": "Não tem",
    "crm": "0532",
    "areaAtuacao": "Cirurgia",
    "supervisor": cirurgiao
  }
  
  residente = Residente(fichaResidente)

  print("RESIDENTE: \n")
  print("\
    {} {} especialidade, está na residência de {}, seu crm é {} e seu supervisor é {}\n\
    ".format(residente.getNome(), residente.getEspecialidade(), residente.getAreaAtuacao(), residente.getCrm(), residente.getSupervisor().getNome()))
  
  fichaRecadastro = {
    "crm": "0077",
    "areaAtuacao": "Clinica",
    "supervisor": clinico
  }
  
  residente.reCadastroTitular(fichaRecadastro)

  print("\
    {} {} especialidade, está na residência de {}, seu crm é {} e seu supervisor é {}\n\
    ".format(residente.getNome(), residente.getEspecialidade(), residente.getAreaAtuacao(), residente.getCrm(), residente.getSupervisor().getNome()))
  
  print("---------------------------------------------------------------------------------------------------------------------")
  '''
  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  >>>>>>>>>>>>>FIM POLIMORFISMO<<<<<<<<<<<<<<<
  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  '''

  
elif selecionar == 3:
  consultor = {
    0: {
    "nome": "Luiza",
    "idade": 29,
    "sexo": "Mulher",
    "id": 55,
    "especialidade": "financeiro",
    "setor": "vendas"
    },
    1:{
    "nome": "Saul Goodman",
    "idade": 62,
    "sexo": "Homem",
    "id": 66,
    "especialidade": "juridico",
    "casos":["processo por danos morais", "processo por casca de banana no chao"]
    },
    2:{
    "nome": "Elliot Alderson",
    "idade": 28,
    "sexo": "Homem",
    "id": 314,
    "especialidade": "tecnologia",
    "tecnologiasResponsaveis":["ciber seguranca", "qualidade de software"],
    "setor":"software"
    }
  }
  mrRobot = ConsultTecnologico(consultor[2])# eu peguei errado, esse era pra ser o juridico kkj
  conMan = ConsultJuridico(consultor[1]) #esse é o novo zape
  finances = ConsultFinanceiro(consultor[0])
  print("\n{} é o consultor de {} responsavel pelas tecnologias {} do setor de {}\n".format(mrRobot.getNome(), mrRobot.getEspecialidade(), mrRobot.getTecnologias(), mrRobot.getSetor()))
  
  print("{} é o consultor de {} responsavel pelos casos {}\n".format(conMan.getNome(), conMan.getEspecialidade(), conMan.getCasos()))

  print("{} é a consultora de {} responsavel pelo setor {}".format(finances.getNome(), finances.getEspecialidade(), finances.getSetor()))

elif selecionar == 4:
  gerente ={
    "nome": "Karen",
    "idade": 31, 
    "sexo": "Mulher",
    "id": 11,
    "nivel": 2,
    "funcionarios": []
  }

  funcionarios = {
    0:{
      "nome": "Roberto",
      "idade": 21, 
      "sexo": "Homem",
      "id": 12,
      "setor": "Telefonia",
      "cargaHoraria": 6,
      "telefoneBancada": 71992887733,
    },
    1:{
      "nome": "Roberta",
      "idade": 26, 
      "sexo": "Mulher",
      "id": 13,
      "setor": "Telefonia",
      "cargaHoraria": 8,
      "telefoneBancada": 71992887744,
    },
    2:{
      "nome": "Tâmara",
      "idade": 33, 
      "sexo": "Mulher",
      "id": 14,
      "setor": "Segurança",
      "cargaHoraria": 8,
      "turno": "matutino"
    },
    3:{
      "nome": "Thanos, o conquistador",
      "idade": 1000, 
      "sexo": "Titan",
      "id": 9999,
      "setor": "Segurança",
      "cargaHoraria": 24,
      "turno": "integral"
    }
  }

  
  for i in range( len(funcionarios) ):
    if(funcionarios[i]["setor"] == "Telefonia"):
      funcionarios[i] = Recepcionista(funcionarios[i])
      gerente["funcionarios"].append(funcionarios[i])
    else:
      funcionarios[i] = Seguranca(funcionarios[i])
      gerente["funcionarios"].append(funcionarios[i])

  
  karen = Gerente(gerente)
  
  print("\n{} é gerente do hospital e  tem {}º nível de privilégios, sua equipe é composta de\
 {} pessoas, sendo elas:\n".format(karen.getNome(), karen.getNivel(), len(karen.getFuncionarios())))
  
  print("\n-----------------------------------------\n")
  
  for i in funcionarios:
    fi = karen.getSpecificFunc(i)

  print("\n-----------------------------------------\n")

  c = random.randint(0,len(funcionarios)-1)
  b = random.randint(0,len(funcionarios)-1)

  if (b != c):
    print(" '{}' e '{}' são os funcionários do mês!".format(karen.getFuncionarios()[c].getNome(), karen.getFuncionarios()[b].getNome()))
  else:
    print("'{}' é funcionário do mês!".format(karen.getFuncionarios()[c].getNome()))

elif selecionar == 5:
  '''
  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  Tudo aqui é para a atividade de polimorfismo
  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  '''
  suporte = {
    0: {
    "nome": "Willy",
    "idade": 45,
    "sexo": "Homem",
    "id": 512,
    "area":"Limpeza",
    "secoesAtendidas":["Segundo andar", "Terceiro andar"],
    "totalQuartoResponsaveis": 534
    },
    1:{
    "nome": "Rose",
    "idade": 26,
    "sexo": "Mulher",
    "id": 656,
    "area":"Anti alérgicos",
    "secoesAtendidas":["Primeiro andar"],
    "totalMedEntregues": 53,
    "estoqueMeds": 5332
    },
    2:{
    "nome": "Hermes",
    "idade": 20,
    "sexo": "Homem",
    "id": 314,
    "area":"Refeições",
    "secoesAtendidas":["Segundo andar", "Terceiro andar",     "Mezzanino"],
    "totalEntregas": 51241
    }
  }
  zelador = Zelador(suporte[0])
  farmaceutico = Farmaceutico(suporte[1]) #esse é o novo zape
  uberflash = Entregador(suporte[2]) #isster egues
  
  print("\n{} é o zelador da área de {} atendendo as seções  {} e cuidando de {} quartos\n".format(zelador.getNome(), zelador.getArea(), zelador.getSecoesAtendidas(), zelador.getTotalQuarto()))
  
  
  print("\n{} é a farmaceutica da área de {} atendendo as seções  {}, entregando {} medicamentos e com {} restantes no estoque\n".format(farmaceutico.getNome(), farmaceutico.getArea(), farmaceutico.getSecoesAtendidas(), farmaceutico.getTotalMedEntregues(),farmaceutico.getEstoque()))

  print("\n{} é o entregador da área de {} atendendo as seções  {} com um total de {} entregas\n".format(uberflash.getNome(), uberflash.getArea(), uberflash.getSecoesAtendidas(), uberflash.getTotalEntregas()))

else:
  print("Oi professora! não se esqueça de digitar os números de 1 a 5! Se quiser escolher novamente rode o programa!")