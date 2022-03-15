import BrazilFlag as Flag
import ListDataBase as Data
import Ex_DDD_Function as ExF
import Options


print("--------------------------------------------------------------")
print("                           Doin-Q")
print("--------------------------------------------------------------\n")

while True:

    search = input("\nO que gostaria de pesquisar?\n")
    if search == "estado":

    #Stades decision

        state = input("\nPor favor digite o nome do estado:\n")
        if state == "acre":
            print("O DDD correspondente ao Acre é:\nDDD 68")
        elif state == "alagoas":
            print("O DDD correspondente ao Alagoas é:\nDDD 82")
        elif state == "amapa":
            print("O DDD correspondente ao Amapá é:\nDDD 96")
        elif state == "amazonas":
            print("\nOs DDD's correspondente ao Amazonas são: ")
            Data.AM()

        elif state == "bahia": 
            print("\nOs DDD's correspondente a Bahia são: ")
            Data.BA()
        elif state == "ceara":
            print("\nOs DDD's correspondente ao Ceará são: ")
            Data.CE()
        elif state == "espirito santo":
            print("\nOs DDD's correspondente ao Esperíto Santo são: ")
            Data.ES()
        elif state == "goias":
            print("\nOs DDD's correspondente a Goias são: ")
            Data.ES()
        elif state == "maranhao":
            print("\nOs DDD's correspondente ao Maranhão são: ")
            Data.MA()
        elif state == "mato grosso":
            print("\nOs DDD's correspondente ao Mato Grosso são: ")
            Data.MT()
        elif state == "mato grosso do sul":
            print("O DDD correspondente ao Mato Grosso do Sul é:\nDDD 67")
        elif state == "minas gerais":
            print("\nOs DDD's correspondente a Minas Gerais são: ")
            Data.MG()
        elif state == "para":
            print("\nOs DDD's correspondente para o Pará são: ")
            Data.PA()
        elif state == "paraiba":
            print("O DDD correspondente ao Paraiba é:\nDDD 83")
        elif state == "parana":
            print("\nOs DDD's correspondente para o Parana são: ")
            Data.PN()
        elif state == "piaui":
            print("\nOs DDD's correspondente para o Piauí são: ")
            Data.PI()
        elif state == "rio de janeiro":
            print("\nOs DDD's correspondente a o Rio de Janeiro são: ")
            Data.RJ()
        elif state == "rio grande do norte":
            print("O DDD correspondente ao Rio Grande do Norte é:\nDDD 84")
        elif state == "rio grande do sul":
            print("\nOs DDD's correspondente a o Rio Grande do Sul são: ")
            Data.RS()
        elif state == "roraima":
            print("O DDD correspondente a Roraima é:\nDDD 95")
        elif state == "santa catarina":
            print("\nOs DDD's correspondente a Santa Catarina são: ")
            Data.SC()
        elif state == "sao paulo":
            print("\nOs DDD's correspondente a São Paulo são: ")
            Data.SP()
        elif state == "sergipe":
            print("O DDD correspondente a Sergipe é:\nDDD 79")
        elif state == "tocantins":
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
            ExF.Function92()
        elif ddd_again == 97:
            ExF.Function97()
        elif ddd_again == 71:
            ExF.Function71()
        elif ddd_again == 73:
            ExF.Function73()
        elif ddd_again == 74:
            ExF.Function74()
        elif ddd_again == 75:
            ExF.Function75()
        elif ddd_again == 77:
            ExF.Function77()
        elif ddd_again == 85:
            ExF.Function85()
        elif ddd_again == 88:
            ExF.Function88()
        elif ddd_again == 27:
            ExF.Function27()
        elif ddd_again == 28:
            ExF.Function28()
        else:
            print(ddd_again, "não foi encontrado 🤔")
            print("Motivos: \nO ddd ainda não foi adicionado\nDDD não existe\nPor favor escreva lista ddd")
# Egg

    elif search == "bandeira":
        Flag.BrazilFlag()

# Options

    elif search == "--help":
        Options.OP()


    elif search == "sair":
        break

# List ddd and states sequence

    elif search == "ddd --list":
        print("")
        Data.DDDList()
    
    elif search == "estado --list":
        print("")
        Data.StatesList()
    else:
        print("Tem certeza que digitou,", search, " corretamente ou no lugar certo?")
        print("Você escreveu algo errado 🤔")
        print("Mas não se preocupe, para saber as opções basta escrever: \n--help")

