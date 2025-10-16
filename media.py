nota1 = float(input("Digite a sua nota do 1º bimestre:"))
nota2 = float(input("Digite a sua nota do 2º bimestre:"))
nota3 = float(input("Digite a sua nota do 3º bimestre:"))
nota4 = float(input("Digite a sua nota do 4º bimestre:"))

total = nota1 + nota2 + nota3 + nota4

media = total / 4
print(media)

if media >=7.0:
    print("aprovado")
elif media >= 5.0 and media <=7.0:
    print("recuperação")
else:
    print("reprovado")



