num1 = int(input("Digite primeiro numero: "))
num2 = int(input("Digite segundo numero: "))
operacao = int(input("Qual operacao quer efetuar?\n 1 - divisao \n 2 - soma \n 3 - multiplicacao \n 4 - subtracao \n => "))
if operacao == 1:
	resultado = num1 / num2
	print(f"O resultado da divisao é {resultado}")
elif operacao == 2:
	resultado = num1 + num2
	print(f"O resultado da soma é {resultado}")
elif operacao == 3:
	resultado = num1 * num2
	print(f"O resultado da multiplicacao é {resultado}")
elif operacao == 4:
	resultado = num1 - num2
	print(f"O resultado da subtracao é {resultado}")
else:
	print("Opcao invalida!")
