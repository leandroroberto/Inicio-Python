import random
import time
a = 1
b = 2
while True:
	escolha = int(input("Digite um valor: "))
	if escolha <=6:
	    print("Jogando o dado.....")
	    time.sleep(2)
	    resultado = random.randint(a, b)
	elif escolha > 6:
	   print("Valor inválido!!")
	   break
	if resultado == escolha:
	    print("Você acertou..Parabéns")
	elif resultado != escolha:
	     print("Saiu o numero", resultado, "!")
	     print("Voce perdeu!")
	     break