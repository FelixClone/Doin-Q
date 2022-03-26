import BrazilFlag as Flag
import ListDataBase as Data
import Ex_DDD_Function as ExF
import Options


print("--------------------------------------------------------------")
print("                        #Doin-cli")
print("--------------------------------------------------------------\n")

while True:

    search = input("\nO que gostaria de pesquisar?\n")
    if search == "estado":

    #States decision

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
            print("\nO estado",state, "não foi encontrado 🤔\nMotivos: \n1- Esse estado não existe\n2- O nome do estado esta errado")
            state_list = input("Gostaria de ver a lista? (s) ou (n): \n")
            if state_list == "s":
                print("")
                Data.StatesList()
            elif state_list == "n":
                print("\nOkay ✅")
            else:
                print("\nVocê escreveu algo errado ❌")

# area code

    elif search == "ddd":
        ddd_again = int(input("\npor favor digite o ddd: "))
        if ddd_again == 27:
            ExF.Function27()
        elif ddd_again == 28:
            ExF.Function28()
        elif ddd_again == 32:
            ExF.Function32()
        elif ddd_again == 33:
            ExF.Function33()
        elif ddd_again == 34:
            ExF.Function34()
        elif ddd_again == 35:
            ExF.Function35()
        elif ddd_again == 37:
            ExF.Function37()
        elif ddd_again == 41:
            ExF.Function41()
        elif ddd_again == 42:
            ExF.Function42()
        elif ddd_again == 43:
            ExF.Function43()
        elif ddd_again == 44:
            ExF.Function44()
        elif ddd_again == 45:
            ExF.Function45()
        elif ddd_again == 46:
            ExF.Function46()
        elif ddd_again == 61:
            ExF.Function61()
        elif ddd_again == 62:
            ExF.Function62()
        elif ddd_again == 64:
            ExF.Function64()
        elif ddd_again == 65:
            ExF.Function65()
        elif ddd_again == 66:
            ExF.Function66()
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
        elif ddd_again == 86:
            ExF.Function86()
        elif ddd_again == 88:
            ExF.Function88()
        elif ddd_again == 89:
            ExF.Function89()
        elif ddd_again == 91:
            ExF.Function91()
        elif ddd_again == 92:
            ExF.Function92()
        elif ddd_again == 93:
            ExF.Function93()
        elif ddd_again == 94:
            ExF.Function94()
        elif ddd_again == 97:
            ExF.Function97()
        elif ddd_again == 98:
            ExF.Function98()
        elif ddd_again == 99:
            ExF.Function99()
        else:
            print("\nO ddd",ddd_again, "não foi encontrado 🤔")
            print("Motivos: \n1 - O ddd ainda não foi adicionado\n2 - DDD não existe\n")
            area_code_list = input("Gostaria de ver a lista? (s) ou (n): \n")
            if area_code_list == "s":
                print("")
                Data.DDDList()
            elif area_code_list == "n":
                print("\nOkay ✅")
            else:
                print("\nVocê escreveu algo errado ❌")

# Egg

    elif search == "bandeira":
        Flag.BrazilFlag()

# Options

    elif search == "--help":
        Options.OP()


    elif search == "sair":
        break

    elif search == "--version":
        print("Doin-Q - 0.1")
# List ddd and states sequence

    elif search == "ddd --list":
        print("")
        Data.DDDList()
    
    elif search == "estado --list":
        print("")
        Data.StatesList()
    else:
        print("\nTem certeza que digitou,", search, " corretamente ou no lugar certo?")
        print("Você escreveu algo errado 🤔")
        print("Mas não se preocupe, para saber as opções basta escrever: \n--help")

