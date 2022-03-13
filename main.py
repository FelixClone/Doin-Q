import BrazilFlag as Flag
import ListDataBase as Data
import Ex_DDD_City as Ex
import Options


print("----------")
print("De onde é?")
print("----------\n")

while True:

    search = input("\nO que gostaria de pesquisar?\n")
    if search == "estado":
    #Stades decision

        est_es = input("\npor favor digite o nome do estado:\n ")
        if est_es == "acre":
            print("O DDD correspondente ao Acre é:\nDDD 68")
        elif est_es == "alagoas":
            print("O DDD correspondente ao Alagoas é:\nDDD 82")
        elif est_es == "amapa":
            print("O DDD correspondente ao Amapá é:\nDDD 96")
        elif est_es == "amazonas":
            print("\nOs DDD's correspondente ao Amazonas são: ")
            Data.AM()

        elif est_es == "bahia": 
            print("\nOs DDD's correspondente a Bahia são: ")
            Data.BA()
        elif est_es == "ceara":
            print("\nOs DDD's correspondente ao Ceará são: ")
            Data.CE()
        elif est_es == "espirito santo":
            print("\nOs DDD's correspondente ao Esperíto Santo são: ")
            Data.ES()
        elif est_es == "goias":
            print("\nOs DDD's correspondente a Goias são: ")
            Data.ES()
        elif est_es == "maranhao":
            print("\nOs DDD's correspondente ao Maranhão são: ")
            Data.MA()
        elif est_es == "mato grosso":
            print("\nOs DDD's correspondente ao Mato Grosso são: ")
            Data.MT()
        elif est_es == "mato grosso do sul":
            print("O DDD correspondente ao Mato Grosso do Sul é:\nDDD 67")
        elif est_es == "minas gerais":
            print("\nOs DDD's correspondente a Minas Gerais são: ")
            Data.MG()
        elif est_es == "para":
            print("\nOs DDD's correspondente para o Pará são: ")
            Data.PA()
        elif est_es == "paraiba":
            print("O DDD correspondente ao Paraiba é:\nDDD 83")
        elif est_es == "parana":
            print("\nOs DDD's correspondente para o Parana são: ")
            Data.PN()
        elif est_es == "piaui":
            print("\nOs DDD's correspondente para o Piauí são: ")
            Data.PI()
        elif est_es == "rio de janeiro":
            print("\nOs DDD's correspondente a o Rio de Janeiro são: ")
            Data.RJ()
        elif est_es == "rio grande do norte":
            print("O DDD correspondente ao Rio Grande do Norte é:\nDDD 84")
        elif est_es == "rio grande do sul":
            print("\nOs DDD's correspondente a o Rio Grande do Sul são: ")
            Data.RS()
        elif est_es == "roraima":
            print("O DDD correspondente a Roraima é:\nDDD 95")
        elif est_es == "santa catarina":
            print("\nOs DDD's correspondente a Santa Catarina são: ")
            Data.SC()
        elif est_es == "sao paulo":
            print("\nOs DDD's correspondente a São Paulo são: ")
            Data.SP()
        elif est_es == "sergipe":
            print("O DDD correspondente a Sergipe é:\nDDD 79")
        elif est_es == "tocantins":
            print("O DDD correspondente a Tocantins é:\nDDD 63")
        else:
            print("Você escreveu algo errado ❌")
            est_lista2 = input("Gostaria de ver a lista? (s) ou (n): \n")
            if est_lista2 == "s":
                print("")
                Data.StatesList()
            elif est_lista2 == "n":
                print("Okay ✅")
            else:
                print("Você escreveu algo errado ❌")


# DDD

    elif search == "ddd":
        ddd_again = int(input("\npor favor digite o ddd: "))
        if ddd_again == 92:
            print(" --------------------")
            print("|  Modo simples  [1] |")
            print("|  Modo avançado [2] |")
            print("|  Ajuda         [3] |")
            print(" --------------------")
            mod_menu = int(input("Escolha o modo a partir do numero:\n"))
            if mod_menu == 1:
                print("Esse DDD pertence ao Amazonas")
            elif mod_menu == 2:
                print("\nO ddd", ddd_again, "pertence a o Amazonas e suas respectivas cidades são: ")
                print("")
                Ex.ExDDD92()

            elif mod_menu == 3:
                print("[Modo ajuda]")
                print("O modo simples ele foi criado para ajudar o usuario a identificar o estado pelo ddd de modo mais simples e rapido")
                print("O modo avançado já é para aqueles que querem saber mais detalhes sobre o DDD como por exemplo a cidade")
            else:
                print("Você escreveu algo errado ❌")

        elif ddd_again == 97:
            print(" --------------------")
            print("|  Modo simples  [1] |")
            print("|  Modo avançado [2] |")
            print("|  Ajuda         [3] |")
            print(" --------------------")
            mod_menu = int(input("Escolha o modo a partir do numero:\n"))
            if mod_menu == 1:
                print("Esse DDD pertence ao Amazonas")
            elif mod_menu == 2:
                print("\nO ddd", ddd_again, "pertence a o Amazonas e suas respectivas cidades são: ")
                print("")
                Ex.ExDDD97()

            elif mod_menu == 3:
                print("[Modo ajuda]")
                print("O modo simples ele foi criado para ajudar o usuario a identificar o estado pelo ddd de modo mais simples e rapido")
                print("O modo avançado já é para aqueles que querem saber mais detalhes sobre o DDD como por exemplo a cidade")
            else:
                print("Você escreveu algo errado ❌")

        elif ddd_again == 71:
            print(" --------------------")
            print("|  Modo simples  [1] |")
            print("|  Modo avançado [2] |")
            print("|  Ajuda         [3] |")
            print(" --------------------")
            mod_menu = int(input("Escolha o modo a partir do numero:\n"))
            if mod_menu == 1:
                print("Esse DDD pertence a Bahia")
            elif mod_menu == 2:
                print("\nO ddd", ddd_again, "pertence a Bahia e suas respectivas cidades são: ")
                print("")
                Ex.ExDDD71()
            elif mod_menu == 3:
                print("[Modo ajuda]")
                print("O modo simples ele foi criado para ajudar o usuario a identificar o estado pelo ddd de modo mais simples e rapido")
                print("O modo avançado já é para aqueles que querem saber mais detalhes sobre o DDD como por exemplo a cidade")
            else:
                print("Você escreveu algo errado ❌")

        elif ddd_again == 73:
            print(" --------------------")
            print("|  Modo simples  [1] |")
            print("|  Modo avançado [2] |")
            print("|  Ajuda         [3] |")
            print(" --------------------")
            mod_menu = int(input("Escolha o modo a partir do numero:\n"))
            if mod_menu == 1:
                print("Esse DDD pertence a Bahia")
            elif mod_menu == 2:
                print("\nO ddd", ddd_again, "pertence a Bahia e seus respectivos estados são: ")
                print("")
                Ex.ExDDD73()
            elif mod_menu == 3:
                print("[Modo ajuda]")
                print("O modo simples ele foi criado para ajudar o usuario a identificar o estado pelo ddd de modo mais simples e rapido")
                print("O modo avançado já é para aqueles que querem saber mais detalhes sobre o DDD como por exemplo a cidade")
            else:
                print("Você escreveu algo errado ❌")

        else:
            print("Você escreveu algo errado ❌")

# Egg

    elif search == "bandeira":
        Flag.BrazilFlag()
    elif search == "--help":
        Options.OP()

# List ddd and states sequence 
    elif search == "sair":
        break

    elif search == "lista":
        ddes = input("Gostaria de ver a lista de estado ou de ddd?\n")
        if ddes == "ddd":
            print("")
            Data.DDDList()
        elif ddes == "estado":
            print("")
            Data.StatesList()

    else:
        print("Você escreveu algo errado 🤔")
        print("Não se preocupe, para saber as opções basta escrever: \n--help")


