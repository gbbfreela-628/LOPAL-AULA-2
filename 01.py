# Escreva um programa em python que peca as seguintes informacoes:
# - idade (um numero inteiro)
# - altura em centimetros (um numero inteiro)
# - tem autorizacao dos pais? (uma string: "sim" ou "nao")
#
# O programa deve exibir "acesso liberado!" se o visitante 
# puder andar no brinquedo, ou "acesso negado." caso contrario.
#
# Regra
# O visitante pode entrar se :
# - tiver idade maior ou igual a 12 e altura maior ou igual a 140 OU
# - se tiver autorizacao igual a "sim""



idade = int(input("Digite a idade da crianca: "))
altura = int(input("Digite a altura da crianca: "))
autorizacao_dos_pais = input("Ela tem a autorizacao dos pais? ")



if (idade >= 12 and altura >= 140) and autorizacao_dos_pais == "sim":
    print("acesso liberado!")
    
else:
        print("acesso negado")



