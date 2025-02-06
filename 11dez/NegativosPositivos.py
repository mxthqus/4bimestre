# Leia 10 numeros reais do usuario e armazene em uma lista
numeros = []

for i in range(10):
    # Leia um numero real
    numero = float(input("Digite um número real: "))
    # Adicione o numero a lista
    numeros.append(numero)

# Inicialize variaveis para contar a quantidade de numeros negativos e somar os numeros positivos
negativos = 0
somaPositivos = 0

# Itera sobre a lista de numeros
for numero in numeros:
    # Verifica se o numero e negativo
    if numero < 0:
        # Incrementa a quantidade de numeros negativos
        negativos += 1
    else:
        # Soma o numero caso ele seja positivo
        somaPositivos += numero

# Imprime a quantidade de numeros negativos
print(f"Quantidade de números negativos: {negativos}")
# Imprime a soma dos numeros positivos
print(f"Soma dos números positivos: {somaPositivos}")
