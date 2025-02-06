#cria uma lista para armazenar as notas
nota = []


#inicializa o loop para digitar as 5 notas
for i in range(5):
    #armazena a nota digitada na lista
    notaunitaria = float(input("Digite a nota: "))
    nota.append(notaunitaria)

    #inicializa a variável media em 0
    media = 0

#inicializa o loop para somar as notas
for no in nota:
    #soma a nota atual com a media
    media = media + no

#calcula a média das notas
media = media / 5

#imprime a média das notas
print("A média das notas é: ", {media})


