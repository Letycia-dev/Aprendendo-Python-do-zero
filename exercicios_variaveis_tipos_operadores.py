"""
Arquivo: exercicios_basicos.py
Descrição: Exercícios de variáveis, tipos e operadores para treinar no VS Code.

Instruções:
- Leia os exercícios no código.
- Escreva suas respostas abaixo de cada comentário indicado.
- Para executar: python exercicios_basicos.py
"""

# =============================================================
# EXPLICAÇÃO: VARIÁVEIS, TIPOS E OPERADORES
# -------------------------------------------------------------
# VARIÁVEIS:
# São "caixinhas" na memória onde guardamos valores. Ex:
# nome = "Lê"  → armazena um texto
# idade = 25     → armazena um número inteiro
# peso = 68.5    → armazena número decimal
# Você pode mudar o valor da variável quando quiser.
# -------------------------------------------------------------
# TIPOS DE DADOS:
# int    → números inteiros (1, 20, -5)
# float  → números decimais (3.5, 9.8)
# str    → textos ("Python", "Olá")
# bool   → valores lógicos (True ou False)
# Para saber o tipo: type(variavel)
# -------------------------------------------------------------
# OPERADORES:
# ARITMÉTICOS:
# + soma | - subtração | * multiplicação | / divisão
# // divisão inteira | % resto | ** potência
# COMPARAÇÃO (retornam True ou False):
# == igual
# != diferente
# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# -------------------------------------------------------------
# Agora siga com os exercícios!
# =============================================================

print("=== EXERCÍCIOS BÁSICOS DE PYTHON ===")
print("Execute e leia as instruções dentro do arquivo.\n")

# =============================================================
# EXERCÍCIO 1 — Variáveis
# Crie 3 variáveis:
# 1. Seu nome
# 2. Sua idade
# 3. Seu peso
# Depois imprima: "Meu nome é ..., tenho ... anos e peso ... kg."
# =============================================================

# Escreva sua solução abaixo:
# 1. 12 + 7
nome = "Leticia"
idade = 24
peso = 60.5

print(f"Meu nome é {nome}, tenho {idade} anos e peso {peso} kg.")

# =============================================================
# EXERCÍCIO 2 — Tipos
# Observe as variáveis e escreva abaixo qual é o tipo de cada uma.
# (não é código, apenas comentários explicando)
# =============================================================

a = 20
b = 4.7
c = "Python é legal"
d = False

# Escreva aqui os tipos:
# a = int
# b = float
# c = str
# d = bool

# =============================================================
# EXERCÍCIO 3 — Operadores Aritméticos
# Calcule e mostre o resultado de cada operação.
# =============================================================

# Exemplo: resultado = 12 + 7
# print(resultado)

# 1. 12 + 7
print(12 + 7)

# 2. 20 - 5
print(20 - 5)

# 3. 6 * 4
print(6 * 4)

# 4. 15 / 2   -> divisão normal
print(15 / 2)

# 5. 15 // 2  -> divisão inteira
print(15 // 2)

# 6. 15 % 2   -> resto da divisão
print(15 % 2)

# 7. 3 ** 4   -> potência
print(3 ** 4)

# =============================================================
# EXERCÍCIO 4 — Comparação
# Diga se cada expressão retorna True ou False.
# =============================================================

# Escreva em comentários:
# 10 == 10 → True
# 7 != 3 → True
# 5 > 9 → False
# 8 <= 8 → True
# (4 + 2) >= (3 * 2) → True

# =============================================================
# EXERCÍCIO 5 — Misturando tudo
# Use as variáveis abaixo:
# num1 = 8
# num2 = 3
# Calcule: soma, subtracao, multiplicacao, (num1 > num2), resto
# =============================================================

num1 = 8
num2 = 3

# Escreva seu código aqui:

num1 = 8
num2 = 3

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
comparacao = num1 > num2
resto = num1 % num2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("num1 > num2?", comparacao)
print("Resto:", resto)


print("\nExercícios carregados. Complete o arquivo e execute novamente!")
