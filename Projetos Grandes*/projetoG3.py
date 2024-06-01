###Ex092 Sistema de Validação de Aposentadoria

import datetime

data_atual = datetime.datetime.now()
ano_atual = data_atual.year
informacoes = {}

# Entrada de dados
nome = input("Qual seu nome: ").strip().title()

# Validação do ano de nascimento
while True:
    ano_de_nascimento = int(input("Qual seu ano de nascimento: "))
    if ano_de_nascimento > ano_atual or ano_de_nascimento < ano_atual - 150:
        print("Ano de nascimento inválido. Por favor, tente novamente.")
    else:
        break

carteira_de_trabalho = int(input("Digite sua carteira de trabalho (0 não tem): "))
sexo = input("Digite seu sexo (F/M/O - Feminino, Masculino, Outros): ").strip().upper()
trabalho_atual = ""

informacoes["Nome"] = nome
informacoes["Idade"] = ano_atual - ano_de_nascimento
informacoes["Carteira de Trabalho"] = carteira_de_trabalho
informacoes["Sexo"] = sexo

# Determinando a idade de aposentadoria
if sexo == "F":
    idade_aposentadoria = 60
else:
    idade_aposentadoria = 65

# Calculando a idade de aposentadoria baseada no tempo de contribuição
if sexo == "F":
    aposentadoria = 30
elif sexo == "M" or sexo == "O":
    aposentadoria = 35

if carteira_de_trabalho == 0:
    print("Entendo, você não tem carteira.")
    trabalho_atual = input("Digite seu trabalho atual (nada caso não tenha): ").strip()
    if trabalho_atual.lower() == "nada":
        print("Você deveria procurar um emprego!")
    else:
        print(f"Parabéns por trabalhar como {trabalho_atual}, qualquer trabalho é digno.")
        print("Recomendo fazer uma boa bolsa de investimentos.")
else:
    print("Parabéns por ter carteira de trabalho! Digite suas informações:")
    informacoes["Ano de Contratação"] = int(input("Qual o ano que você foi contratado: "))
    informacoes["Salário"] = float(input("Qual seu salário: "))
    print("Vamos a todas as informações:")
    
    print(f"Seu nome é {informacoes['Nome']}.")
    print(f"Sua idade é {informacoes['Idade']}.")
    print(f"Seu ID de carteira de trabalho é {informacoes['Carteira de Trabalho']}.")
    print(f"Seu ano de contratação é {informacoes['Ano de Contratação']}.")
    print(f"Você foi contratado há {ano_atual - informacoes['Ano de Contratação']} anos.")
    print(f"Seu salário é R${informacoes['Salário']:.2f}.")

    ano_aposentadoria = informacoes['Ano de Contratação'] + aposentadoria
    print(f"Seu ano de aposentadoria será {ano_aposentadoria}.")

    if informacoes["Ano de Contratação"] < ano_atual:
        anos_para_aposentadoria = aposentadoria - (ano_atual - informacoes['Ano de Contratação'])
        print(f"Faltam {anos_para_aposentadoria} anos para sua aposentadoria.")
    elif informacoes["Ano de Contratação"] > ano_atual:
        print("Coloque uma data válida.")
    elif informacoes["Ano de Contratação"] == ano_atual:
        print("Faltam exatamente 35 anos, você começou a trabalhar recentemente, não é?")

# Exibição das informações gerais
print("\nResumo das Informações:")
print(f"Nome: {informacoes['Nome']}")
print(f"Idade: {informacoes['Idade']} anos")
print(f"Sexo: {informacoes['Sexo']}")
print(f"Carteira de Trabalho: {'Não possui' if carteira_de_trabalho == 0 else carteira_de_trabalho}")
if carteira_de_trabalho != 0:
    print(f"Ano de Contratação: {informacoes['Ano de Contratação']}")
    print(f"Salário: R${informacoes['Salário']:.2f}")
    print(f"Ano de Aposentadoria: {ano_aposentadoria}")
