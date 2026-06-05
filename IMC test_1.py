#Imc
peso = input("Qual é o seu peso?:")
altura = input("Qual a sua altura?:")
pn = float(peso)
an = float(altura)
if float(pn/an**2) >25: print("Você está acima do peso")
elif float(pn/an**2) ==25Z :print ("Você está em um peso ideal")
else: print("Você está abaixo do peso")