# Faça um programa para verificar se um determinado número inteiro é divisível
# por 3 ou 5, mas não simultaneamente pelos dois.
while True:
    try:
        print(" ");
        print("### Programa pra mostrar se um número é divisível por 3 ou 5, e não para ambos! ###");
        print(" ");
        num = int(input("Digite um número inteiro: "));
        if num % 3 == 0 and num % 5 == 0:
            print("O número é divisível por 3 e 5, logo é um número inválido!");
            continue
        elif num % 3 == 0:
            print("O número é divisível por 3!");
            break
        elif num % 5 == 0:
            print("O número é divisível por 5!")
            break
    except ValueError:
        print("O número digitado não é um número inteiro. Tente novamente.");
        continue