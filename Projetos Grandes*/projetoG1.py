Grupo=int(input("quantas pessoas tem no grupo:"))
Masculino = 0
Feminino = 0
Outros = 0
Velho = 0
Novo = 0
Soma_idade=0
pessoa_mais_velha=""
pessoa_mais_nova=""


#variaveis e acumaladores

for perguntas in range(1, Grupo+1):
    print("==={}ª pessoa===".format(perguntas))
    nome = str(input("Qual é o nome desta pessoa: "))
    idade= int(input("Qual a idade desta pessoa: "))
    sexo = str(input("Qual seu sexo? Digite M/F/O (M - Masculino, F - Feminino, O - Outros): ")).upper()
    
    #perguntas

    Soma_idade+=idade

    #acumulador de Idade

    if perguntas == 1:
        Velho = idade
        Novo = idade
        pessoa_mais_velha = nome
        pessoa_mais_nova = nome
    else:
        if idade > Velho:
            Velho = idade
            pessoa_mais_velha = nome
        if idade < Novo:
            Novo = idade
            pessoa_mais_nova = nome
    #mais velho ou mais novo e nome 

    if sexo == "M":
        Masculino+=1
    if sexo == "F":
        Feminino+=1
    if sexo == "O":
        Outros+=1
    #sexo das pessoas 
   
print("A idade da pessoa mais velha é:", Velho)
print("A idade da pessoa mais nova é:", Novo)
print("existem {} pessoas do sexo Masculino neste grupo".format(Masculino))
print("existem {} pessoas do sexo Feminino neste grupo".format(Feminino))
print("existem {} pessoas de Sexo Não identificado neste Grupo".format(Outros))
print("a media de idades neste Grupo é {:.2f}".format(Soma_idade/Grupo))
print("a pessoa mais nova é {}".format(pessoa_mais_nova))
print("a pessoa mais velha é {}".format(pessoa_mais_velha))

# prints