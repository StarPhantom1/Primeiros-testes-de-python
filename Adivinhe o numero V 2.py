#Randomização
import random
numero = random.randint(1,10)
nt = str(numero)
acertou = False
T = 0

#Repetidor
while not acertou:

    Ad = input("Adivinhe o numero:")
    T +=1
    Adn = int(Ad)
        # Codigo após adivinhação
    if Adn == numero:
        acertou = True
        print ("O numero q eu escolhi era "+nt+ " você acertou!!!" )
        print ("Você precisou de "+str(T)+" tentativas")
    else:
        
        print ("Você errou :(")
        if int (Adn) >numero: print ("O numero é menor que "+ Ad +" tente novamente" )
        else: 
            print ("O numero é maior que "+ Ad +" tente novamente" )  
    
    


