import json

# Exercicios em python:

# 1.)
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)
# O valor da variável soma é igual a 91, que é o resultado da soma dos números
# de 1 a 13.

# 2.)
def numero_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a < n:
        a, b = b, a + b

    return a == n


numero = int(input("Informe um número: "))
resultado = numero_fibonacci(numero)
mensagem = f"O número informado, {numero}, pertence à sequência de Fibonacci" if resultado else f"O número informado, {
    numero}, não pertence à sequência de Fibonacci"

print(mensagem)

# 3.)
with open('faturamento.json', 'r') as file:
    data = json.load(file)

faturamento_diario = [dia['valor']
                      for dia in data['faturamento_diario'] if dia['valor'] > 0]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum(
    1 for valor in faturamento_diario if valor > media_mensal)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {
      dias_acima_da_media}")

# 4.)
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valor_total = sum(faturamento.values())
percentuais = {estado: (valor / valor_total) *
               100 for estado, valor in faturamento.items()}

print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# 5.)
def inverter_frase(s):
    lista = list(s)

    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]

        inicio += 1
        fim -= 1

    return ''.join(lista)


entrada = input("Digite uma frase: ")
resultado = inverter_frase(entrada)
print("Frase invertida:", resultado)
