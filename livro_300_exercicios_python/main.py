# 30 - Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os números pares:

def return_number_par():
    for i in range (0, 21):
        if(i % 2 == 0):
            print (i)

return_number_par()

# 31 - Crie um programa que realiza a Progressão Aritmética de 20 elementos, com primeiro termo e razão definidos pelo usuário:

def aritmetic_progress ():
    initial_value = int(input("Digite o valor inicial: "))
    progression = int(input("Digite a razão: "))
    quantity = int(input("Digite a quantidade de números: "))

    for i in range(quantity):
        i += 1
        print(f'{i}° = {initial_value}')
        initial_value += progression

aritmetic_progress()

# 32 - Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário:

def tabuada():
    x = int(input("Digite um número: "))

    for num in range(1, 11):
        print(f"{x} X {num} = {x*num}")

tabuada()

# 33 - Crie um programa que realiza a contagem regressiva de 20 segundos:

def program_in_20_seconds ():
    from time import sleep

    for i in range (20, -1, -1):
        print(i)
        sleep(1)

program_in_20_seconds()

# 34 - Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, 
# ao final do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos:

def count_impar ():
    count = 0
    quantity = 0
    for i in range(0, 101):
        if (i % 2 != 0):
            print(i)
            count += i
            quantity += 1
    print(f"A quantidade de números ímpar é de {quantity} e a soma deles é {count}")

count_impar()

# Crie um programa que pede ao usuário que o mesmo digite um número qualquer,
#  em seguida retorne se esse número é primo ou não, caso não, retorne também quantas vezes esse número é divisível:

def primo():
    x = int(input("Digite um valor: "))
    count = 0
    for i in range(1, x+1):
        if (x % i == 0):
            count += 1
    if(count == 2):
        print(f"O número {x} é primo")
    else:
        print(f"O número {x} não é primo. Ele é divisível por {count} números")

primo()