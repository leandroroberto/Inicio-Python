import random
try:
	print("...::: ADIVINHE O NÚMERO:::...")
	c = 1
	d = 100
	e = random.randint(c, d)
	while True:
		a = int(input("       Chute um número: "))
		if a > e:
			print("    Chute um valor mais baixo!")
		elif a < e:
			print("    Chute um valor mais alto!")
		elif a == e:
			print("      = = Voce acertou! = =")
			break
except:
	print("      Digitou em branco!!!")
