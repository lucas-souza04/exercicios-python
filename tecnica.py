import json

# Exercicios em python:

# 1. Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)
# O valor da variável soma é igual a 91, que é o resultado da soma dos números
# de 1 a 13.

# 2. Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


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

# 3. Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

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

# 4. Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

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

# 5. Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


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
