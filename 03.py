# Escreva um programa em python que receba
# as seguintes quatro informacoes do usuario:
# - Renda mensal (um numero float)
# - score de credito ( um numero inteiro de 0 a 1000)
# - Possui bens como garantia? (uma string: "sim" ou "nao")
# - tem historico de inadinplencia? (uma string: "sim"  ou "nao")
#
# O imprestimo sera APROVADO se o cliente cumprir uma das duas regras abaixo:
# Regra 1:  Ter renda mensal maior ou igual a R$ 3.000,00
#           e score de credito maior ou igual a 600
#           E NAO ter historico de inadimplencia.
# Regra 2:  Independentemente da renda ou do score, 
#           se o cliente NAO tiver historico de inadinplencia
#           E possuir bens como garantia, ele tambem é aprovado.
#
# Se o cliente nao se encaixar em nenhuma das duas regras,
# o emprestimo sera REPROVADO.




renda_mensal = float(input("Qual é a renda mensal? "))
score = int(input("Qual o seu score?"))
bens = input("Possui bens como garantia? ")
historico = input("Tem historico de inadinplencia? ")


if  renda_mensal >= 3000.00 and score >= 600 and historico == "nao":
    print("APROVADO")

elif bens == "sim" and historico == "nao":
    print("APROVADO!")

else:
    print("REPROVADO")



