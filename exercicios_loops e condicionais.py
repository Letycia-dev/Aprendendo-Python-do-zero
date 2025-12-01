#Condicionais if/elif/else
#As condicionais servem para tomar decisões no código.
#Elas verificam uma condição e executam um bloco de código dependendo se essa condição é verdadeira ou falsa.

idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida.")
elif idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")  

#Loops servem para repetir ações.

#Existem dois principais em Python:

#for → usado quando você sabe quantas vezes quer repetir, tem um começo e um final

#while → usado quando você não sabe quantas vezes, ele repete até a condição ser falsa, ou seja, até ele tentar rodar o código e não conseguir mais.

#Exemplo de loop for
print("Números de 1 a 5 usando for:")
for i in range(1, 6): # se fosse um for numero in range(5): (aqui ele lista de 0 a 4)
    print(i)    

#Exemplo de loop while 
print("Números de 1 a 5 usando while:")
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Equivalente a contador = contador + 1
#Funciona assim: ele imprime de 1 até 5 e para quando a condição vira falsa.

#Exercícios

#1. Escreva um programa que peça ao usuário para digitar um número e informe se ele é positivo, negativo ou zero.
numero = int(input("Digite um número para descobrir se ele é positivo, negativo ou zero: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")
    
#2. Crie um programa que imprima todos os números pares de 1 a 10 usando um loop for.
print("Números de 1 a 10")
for num in range(1,11):
    print(num)

#3. Peça que o usuário digite uma palavra e imprima cada letra dessa palavra em uma linha separada usando um loop.
palavra = input("Digite uma palavra:")
for letra in palavra:
    print(letra)

#4. Contar até o usuário digitar 'parar'.
while True:
    comando = input("Digite 'parar' para encerrar o programa: ")
    if comando.lower() == 'parar':
        print("Programa encerrado.")
        break

#5. Faça uma contagem regressiva de 10 a 1 usando um loop while.
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
print("Contagem regressiva finalizada!")




