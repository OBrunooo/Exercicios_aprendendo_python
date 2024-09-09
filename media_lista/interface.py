def welcome ():
    print("Bem vindo a calculadora de média \n")

def thanks ():
    print("Obrigado por utilizar a calculadora de média")

def introduction():
    print("""Vou calcular a média dos valores que você digitar. 
Quando desejar parar de inserir valores e calcular a média é só enviar 'X'""")

def menu():
    menu = int(input("""=== MENU ===
1- Calcular média de uma nova lista
2- Finalizar o programa 
                     
Selecione: """))
    return menu


def new_value():
    new_value = input("Digite um novo valor: ").upper()
    return new_value

def return_media(list, media):
    print("valores:")
    for i in range(len(list)):
        print(list[i])
    print(f"\nA média dos valores é {media}")