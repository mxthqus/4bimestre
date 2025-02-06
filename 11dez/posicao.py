# Inicializa a lista com 10 valores
valores = [5, 3, 9, 1, 7, 12, 4, 8, 6, 10]

# Inicializa as variáveis para encontrar o maior valor e sua posição
# A variável maior_valor armazena o maior valor encontrado na lista
# A variável posicao_maior armazena a posição do maior valor encontrado na lista
maior_valor = valores[0]
posicao_maior = 0

# Percorre a lista para encontrar o maior valor e sua posição
# O laço for percorre a lista a partir do segundo elemento (índice 1)
# Até o último elemento (índice len(valores)-1)
# Para cada elemento o programa verifica se o valor do elemento é maior do que o valor da variável maior_valor
# Se for maior, o valor do elemento é armazenado na variável maior_valor e a sua posição é armazenada na variável posicao_maior
for i in range(1, len(valores)):
    if valores[i] > maior_valor:
        maior_valor = valores[i]
        posicao_maior = i

# Exibe a posição onde se encontra o maior valor
# A mensagem exibida informa o maior valor encontrado na lista e a sua posição
print(f"O maior valor é {maior_valor} e se encontra na posição {posicao_maior}.")

