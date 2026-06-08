Somar = str("Somar")
Subtrair = str("Subtrair")
Multiplicar = str("Multiplicar")
Dividir = str("Dividir")
Tentar_Op = False

while not Tentar_Op:
    print(
    "Somar,   " \
    "Subtrair,  " \
    "Multiplicar,  " \
    "Dividir")
    Op = input("Escolha uma opção:")
    if Op == Somar:
        P1somar = input("Escolha o primeiro numero:")
        P2somar = input("Escolha o segundo numero:")
        if not P1somar.isdigit() or  not P2somar.isdigit():
            print( "Este caracter NÂO é valido")
        else:
            Rsomar = int(P1somar) + int(P2somar)
            print ("O resultado é: "+str(Rsomar))
            T_OP = input ("Escolher outra Opção?:(Y/N)")
            if T_OP == str("N"):
                Tentar_Op = True

    if Op == Subtrair:
        P1sub = input("Escolha o primeiro numero:")
        P2sub = input("Escolha o segundo numero:")
        if not P1sub.isdigit() or not P2sub.isdigit():
            print("Este caracter NÂO é valido")
        else:
            Rsub = int(P1sub) - int(P2sub)
            print ("O resultado é: "+str(Rsub))
            T_OP = input ("Escolher outra Opção?:(Y/N)")
            if T_OP == str("N"):
                Tentar_Op = True

    if Op == Multiplicar:
        P1M = input("Escolha o primeiro numero:")
        P2M = input("Escolha o segundo numero:")
        if not P1M.isdigit() or not P2M.isdigit():
            print( "Este caracter NÂO é valido") 
        else:
            RM = int(P1M) * int(P2M)
            print ("O resultado é: "+str(RM))
            T_OP = input ("Escolher outra Opção?:(Y/N)")
            if T_OP == str("N"):
                Tentar_Op = True

    if Op == Dividir:
        P1D = input("Escolha o primeiro numero:")
        P2D = input("Escolha o segundo numero:")
        if not P1D.isdigit() or not P2D.isdigit():
            print( "Este caracter NÂO é valido")
        else:
            RD = int(P1D) / int(P2D)
            print ("O resultado é: "+str(RD))
            T_OP = input ("Escolher outra Opção?:(Y/N)")
            if T_OP == str("N"):
                Tentar_Op = True
    if Op == str("N"):
        Tentar_Op = True