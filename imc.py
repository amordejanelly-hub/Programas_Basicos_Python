print("Índice de Masa Corporal")

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura * altura)

print("Tu IMC es:", round(imc, 2))