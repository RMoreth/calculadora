
r = ''
while r != 'n':
    num1 = str(input("Digite o primeiro valor")).replace(',', '.')
    print("Qual operação deseja realizar:\n")
    print('"+" para somar.')
    print('"-" para subtrair')
    print('"*" para multiplicar')
    print('"/" para dividir')
    print('"%" para encontrar o resto da divisao')
    operacao = str(input())
    num2 = str(input("Digite o segundo valor")).replace(',', '.')
    num1 = float(num1)
    num2 = float(num2)

    if operacao == '+':
        resultado = num1 + num2
        print(f"o resultado foi {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"o resultado foi {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"o resultado foi {resultado}")
    elif operacao == '/':
        resultado = num1 / num2
        print(f"o resultado foi {resultado}")
    elif operacao == '%':
        resultado = num1 % num2
        print(f"o resultado foi {resultado}")
    else:
        print("nao foi encontrada a operação")

    r = str(input("Deseja continuar?[s/n]"))

    if r == 'n':
        print("Fim do programa")
        break
