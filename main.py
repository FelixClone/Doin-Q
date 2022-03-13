import time



print("----------")
print("De onde é?")
print("----------\n")

estados = [
    "acre","alagoas","amapa","amazonas","bahia","ceara","espirito santo","goias","maranhão"
    ,"mato grosso","mato grosso do sul","minas gerais","para","paraiba","piaui","rio de janeiro",
    "rio grande do norte", "rio grande do sul", "roraima", "santa catarina", "sao paulo", "sergipe", 
    "tocantins"
]
ddd = [
    68, 82, 96, 92, 97, 71, 73, 74, 75, 77, 85, 88, 27, 28, 61, 62, 64, 98, 99, 65, 66,
    67, 31, 32, 33, 34, 35, 37, 91, 93, 94, 83, 41, 42, 43, 44, 45, 46, 86, 89, 21, 22,
    24, 84, 52, 53, 54, 55, 95, 47, 48, 49, 11, 12, 13, 14, 15, 16, 17, 18, 19, 79, 63
]

ddd92 = [
    "Autazes", "Barreirinha", "Boa Vista Do Ramos", "Borba", "Caapiranga", "Careiro	Amazonas",
    "Careiro Da Varzea", "Iranduba", "Itacoatiara", "Itapiranga", "Manacapuru", "Manaquiri",
    "Manaus", "Maues", "Nhamunda", "Nova Olinda Do Norte", "Novo Airão", "Parintins",
    "Presidente Figueiredo", "Rio Preto Da Eva", "São Sebastião Do Uatuma", "Silves"
    "Urucara", "Urucurituba"
]
ddd97 = [
    "Alvaraes", "Amatura", "Anama", "Anori", "Apui", "Atalaia Do Norte", "Barcelos",
    "Benjamin" "Constant", "Beruri", "Boca Do Acre", "Canutama", "Carauari",
    "Coari", "Codajas", "Eirunepe", "Envira", "Fonte Boa", "Guajara", "Humaita",
    "Ipixuna", "Itamarati", "Japura", "Jurua", "Jutai", "Labrea", "Manicore",
    "Maraa", "Novo Aripuana", "Pauini", "Santa Isabel Do Rio Negro",
    "Santo Antonio Do Ica", "São Gabriel Da Cachoeira", "São Paulo De Olivenca",
    "Tabatinga", "Tapaua", "Tefe", "Tonantins", "Uarini"
]
ddd71 = [
    "Camacari", "Candeias", "Catu", "Dias D'Avila", "Itaparica", "Lauro De Freitas",
    "Madre De Deus","Mata De São João", "Pojuca", "Salvador", "São Francisco Do Conde",
    "São Sebastião Do Passe", "Simões Filho", "Vera Cruz"
]
ddd73 = [
    "Aiquara", "Alcobaça", "Almadina", "Apuarema", "Arataca", "Aurelino Leal", 
    "Barra Do Rocha", "Barro Preto", "Belmonte", "Buerarema", "Camacan", "Camamu",
    "Canavieiras", "Caravelas", "Coaraci", "Cravolândia", "Dário Meira", "Eunápolis", 
    "Firmino Alves", "Floresta Azul", "Gandu", "Gongogi", "Guaratinga", "Ibicaraí",
    "Ibicuí", "Ibirapitanga", "Ibirapuã", "Ibirataia", "Igrapiúna", "Iguaí", "Ilhéus",
    "Ipiaú", "Irajuba", "Itabela", "Itabuna","Itacaré", "Itagi","Itagibá", "Itagimirim",
    "Itaju Do Colônia" "Itajuípe", "Itamaraju", "Itamari", "Itanhém", "Itapé", "Itapebi",
    "Itapitanga", "Itaquara", "Itarantim", "Itiruçu", "Itororó", "Ituberá", "Jaguaquara",
    "Jequié", "Jitaúna", "Jucuruçu", "Jussari", "Lafaiete Coutinho", "Lajedão", 
    "Lajedo Do Tabocal", "Manoel Vitorino", "Maracás", "Maraú", "Mascote", 
    "Medeiros Neto", "Mucuri", "Nilo Peçanha", "Nova Canaã", "Nova Ibiá", "Nova Itarana",
    "Nova Viçosa", "Pau Brasil", "Piraí Do Norte", "Planaltino", "Porto Seguro", "Potiraguá", "Prado", "Presidente Tancredo Neves", "Santa Cruz Cabrália",
    "Santa Cruz Da Vitória", "Santa Inês", "Santa Luzia", "São José Da Vitória", 
    "Teixeira De Freitas", "Teolândia", "Ubaitaba", "Ubatã", "Una", "Uruçuca", 
    "Vereda", "Wenceslau Guimarães"
]
ddd74 = [

]
ddd75 = [

]
ddd77 = [

]

Amazonas = [92, 97]
Bahia = [71, 73, 74, 75, 77]
Ceara = [85, 88]
Espirito_Santo = [27, 28]
Goias = [61, 62, 64]
Maranhao = [98, 99]
Mato_Grosso = [65, 66]
Minas_Gerais = [31, 32, 33, 34, 35, 37]
Para = [91, 93, 94]
Parana = [41, 42, 43, 44, 45, 46]
Piaui = [86, 89]
Rio_de_Janeiro = [21, 22, 24]
Rio_Grande_do_Sul = [52, 53, 54, 55]
Santa_Catarina = [47, 48, 49]
Sao_Paulo = [11, 12, 13, 14, 15, 16, 17, 18, 19]


while True:

    fd = input("\nO que gostaria de pesquisar?\n")
    if fd == "estado":
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
            for i in range(len(Amazonas)):
                print("DDD ",Amazonas[i])
        elif est_es == "bahia": 
            print("\nOs DDD's correspondente a Bahia são: ")
            for i in range(len(Bahia)):
                print("DDD ",Bahia[i])
        elif est_es == "ceara":
            print("\nOs DDD's correspondente ao Ceará são: ")
            for i in range(len(Ceara)):
                print("DDD ",Ceara[i])
        elif est_es == "espirito santo":
            print("\nOs DDD's correspondente ao Esperíto Santo são: ")
            for i in range(len(Espirito_Santo)):
                print("DDD ",Espirito_Santo[i])
        elif est_es == "goias":
            print("\nOs DDD's correspondente a Goias são: ")
            for i in range(len(Goias)):
                print("DDD ",Goias[i])
        elif est_es == "maranhao":
            print("\nOs DDD's correspondente ao Maranhão são: ")
            for i in range(len(Maranhao)):
                print("DDD ",Maranhao[i])
        elif est_es == "mato grosso":
            print("\nOs DDD's correspondente ao Mato Grosso são: ")
            for i in range(len(Mato_Grosso)):
                print("DDD ",Mato_Grosso[i])
        elif est_es == "mato grosso do sul":
            print("O DDD correspondente ao Mato Grosso do Sul é:\nDDD 67")
        elif est_es == "minas gerais":
            print("\nOs DDD's correspondente a Minas Gerais são: ")
            for i in range(len(Minas_Gerais)):
                print("DDD ", Minas_Gerais[i])
        elif est_es == "para":
            print("\nOs DDD's correspondente para o Pará são: ")
            for i in range(len(Para)):
                print("DDD ", Para[i])
        elif est_es == "paraiba":
            print("O DDD correspondente ao Paraiba é:\nDDD 83")
        elif est_es == "parana":
            print("\nOs DDD's correspondente para o Parana são: ")
            for i in range(len(Parana)):
                print("DDD ", Parana[i])
        elif est_es == "piaui":
            print("\nOs DDD's correspondente para o Piauí são: ")
            for i in range(len(Piaui)):
                print("DDD ", Piaui[i])
        elif est_es == "rio de janeiro":
            print("\nOs DDD's correspondente a o Rio de Janeiro são: ")
            for i in range(len(Rio_de_Janeiro)):
                print("DDD ", Rio_de_Janeiro[i])
        elif est_es == "rio grande do norte":
            print("O DDD correspondente ao Rio Grande do Norte é:\nDDD 84")
        elif est_es == "rio grande do sul":
            print("\nOs DDD's correspondente a o Rio Grande do Sul são: ")
            for i in range(len(Rio_Grande_do_Sul)):
                print("DDD ", Rio_Grande_do_Sul[i])
        elif est_es == "roraima":
            print("O DDD correspondente a Roraima é:\nDDD 95")
        elif est_es == "santa catarina":
            print("\nOs DDD's correspondente a Santa Catarina são: ")
            for i in range(len(Santa_Catarina)):
                print("DDD ", Santa_Catarina[i])
        elif est_es == "sao paulo":
            print("\nOs DDD's correspondente a São Paulo são: ")
            for i in range(len(Sao_Paulo)):
                print("DDD ", Sao_Paulo[i])
        elif est_es == "sergipe":
            print("O DDD correspondente a Sergipe é:\nDDD 79")
        elif est_es == "tocantins":
            print("O DDD correspondente a Tocantins é:\nDDD 63")
        else:
            print("Você escreveu algo errado ❌")
            est_lista2 = input("Gostaria de ver a lista? (s) ou (n)")
            if est_lista2 == "s":
                print("")
                for i in range(len(estados)):
                    print(estados[i])
            elif est_lista2 == "n":
                print("Okay ✅")
            else:
                print("Você escreveu algo errado ❌")


# DDD

    elif fd == "ddd":
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
                for i in range(len(ddd92)):
                    print(ddd92[i])
                    time.sleep(0.01)
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
                for i in range(len(ddd97)):
                    print(ddd97[i])
                    time.sleep(0.01)
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
                for i in range(len(ddd71)):
                    print(ddd71[i])
                    time.sleep(0.01)
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
                for i in range(len(ddd73)):
                    print(ddd73[i])
                    time.sleep(0.01)
            elif mod_menu == 3:
                print("[Modo ajuda]")
                print("O modo simples ele foi criado para ajudar o usuario a identificar o estado pelo ddd de modo mais simples e rapido")
                print("O modo avançado já é para aqueles que querem saber mais detalhes sobre o DDD como por exemplo a cidade")
            else:
                print("Você escreveu algo errado ❌")

        else:
            print("Você escreveu algo errado ❌")

# Egg

    elif fd == "bandeira":
        print("[.............]")
        time.sleep(0.1)
        print("[####.........]")
        time.sleep(0.1)
        print("[###########..]")
        time.sleep(0.1)
        print("[#############]")
        time.sleep(0.1)
        print("                            .''")
        time.sleep(0.1)
        print("                         .,lO00kl,.")
        time.sleep(0.1)
        print("                      .;ooc,'..',col,.")
        time.sleep(0.1)
        print("                   .;dk;.          .:ko,.")
        time.sleep(0.1)
        print("                .;d00o.              .x0Od;.")
        time.sleep(0.1)
        print("             .:x00000dlloooddllclc,.. .O0000d;.")
        time.sleep(0.1)
        print("           .l0000000klc;;;,;:::coodk0000000000Oc.")
        time.sleep(0.1)
        print("             .:x0000k.. .. .  .     .'l00000d:.")
        time.sleep(0.1)
        print("                .:d00d. . .. ... ....'x0Od;.")
        time.sleep(0.1)
        print("                   .;dk;.  .      .':ko;.")
        time.sleep(0.1)
        print("                      .;ooc,'..',col,.")
        time.sleep(0.1)
        print("                         .,lO00kl,.")
        time.sleep(0.1)
        print("                            .''")
        time.sleep(0.1)
        time.sleep(0.1)
        print("#")
        time.sleep(0.1)
        print("#1")
        time.sleep(0.1)
        print("#11")
        time.sleep(0.1)
        print("#110")
        time.sleep(0.1)
        print("#1101")
        time.sleep(0.1)
        print("bandeira")
        time.sleep(0.1)
        print("bandeira do")
        time.sleep(0.1)
        print("bandeira do BRASIL")
        time.sleep(0.1)
        print("bandeira do BRASIL finalizada")
        time.sleep(0.1)
        print("bandeira do BRASIL finalizada :)")

    elif fd == "--help":
        print("")
        print(" ---------------------------------------")
        print("|                OPÇÕES                 |")
        print(" --------------------------------------- ")
        print("|    FUNÇÃO             |  COMANDO      |")
        print(" --------------------------------------- ")
        print("|  PESQUISAR POR ESTADO | estado        |")
        print("|  PESQUISAR POR DDD    | ddd           |")
        print("|  BANDEIRA DO BRASIL   | bandeira      |")
        print("|  SAIR DO APP          | sair          |")
        print("|  LISTAS               | lista         |")
        print(" --------------------------------------- ")

# List ddd and states sequence 
    elif fd == "sair":
        break

    elif fd == "lista":
        ddes = input("Gostaria de ver a lista de estado ou de ddd?\n")
        if ddes == "ddd":
            print("")
            for i in range(len(ddd)):
                print(ddd[i])
                time.sleep(0.01)
        elif ddes == "estado":
            print("")
            for i in range(len(estados)):
                print(estados[i])
                time.sleep(0.01)
    else:
        print("Você escreveu algo errado 🤔")
        print("Não se preocupe, para saber as opções basta escrever: \n--help")


