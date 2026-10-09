# Escreva um programa em python que pergunte tres 
# informacoes ao usuario:
# - é estudante? (uma string:"sim"ou "nao')
# - dia da semana? (uma string: "terca" ou "outro")
# - tipo de sala? ( uma string: "vip" ou "comum")
#
# o programa deve exibir "desconto aplicado!"
# ou "valor integral"
#
# Regra
# O cliente ganha o desconto 
# se for estudante ou for terca 
# e a sala for comum.





estudante = input("Voce é estudante?")
dia_da_semana = input("Qual dia da semana voce prefere?")
tipo_de_sala = input("Qual tipo de sala? ")


if estudante == "sim" or dia_da_semana == "terca" and tipo_de_sala == "comum":
    print("desconto aplicado")

else:
    print("valor integral")






