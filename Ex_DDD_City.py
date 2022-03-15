import time
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
    "Nova Viçosa", "Pau Brasil", "Piraí Do Norte", "Planaltino", "Porto Seguro", "Potiraguá", 
    "Prado", "Presidente Tancredo Neves", "Santa Cruz Cabrália",
    "Santa Cruz Da Vitória", "Santa Inês", "Santa Luzia", "São José Da Vitória", 
    "Teixeira De Freitas", "Teolândia", "Ubaitaba", "Ubatã", "Una", "Uruçuca", 
    "Vereda", "Wenceslau Guimarães"
    ]
ddd74 = [
    "América Dourada", "Andorinha", "Antônio Gonçalves", "Baixa Grande", "Barra", "Barra Do Mendes",
    "Barro Alto", "Caém", "Cafarnaum", "Caldeirão Grande", "Campo Alegre De Lourdes", "Campo Formoso",
    "Canarana", "Capim Grosso", "Casa Nova", "Central","Curaçá","Filadélfia","Gentio Do Ouro", "Ibipeba",
    "Ibititá", "Irecê", "Itaguaçu Da Bahia", "Itiúba", "Jacobina", "Jaguarari", "João Dourado",
    "Juazeiro", "Jussara", "Lapão", "Macajuba", "Mairi", "Miguel Calmon", "Mirangaba",
    "Morro Do Chapéu", "Mulungu Do Morro", "Mundo Novo", "Ourolândia", "Pilão Arcado", "Pindobaçu",
    "Piritiba", "Ponto Novo", "Presidente Dutra", "Quixabeira", "Remanso", "São Gabriel",
    "São José Do Jacuípe", "Saúde", "Senhor Do Bonfim", "Sento Sé", "Serrolândia", "Sobradinho",
    "Tapiramutá", "Uauá", "Uibaí", "Umburanas", "Várzea Da Roça", "Várzea Do Poço", "Várzea Nova",
    "Xique-Xique"
    ]
ddd75 = [
    "Abaré", "Acajutiba", "Adustina", "Água Fria", "Alagoinhas", "Amargosa", "Amélia Rodrigues", "Andaraí",
    "Anguera", "Antas", "Antônio Cardoso", "Aporá", "Araças", "Araci", "Aramari", "Aratuípe", "Banzaê",
    "Barrocas", "Biritinga", "Boa Vista Do Tupim", "Boninal", "Bonito", "Brejões", "Cabaceiras Do Paraguaçu",
    "Cachoeira", "Cairu", "Candeal", "Cansanção", "Canudos", "Capela Do Alto Alegre", "Cardeal Da Silva",
    "Castro Alves", "Chorrochó", "Cícero Dantas", "Cipó", "Conceição Da Feira", "Conceição Do Almeida",
    "Conceição Do Coité", "Conceição Do Jacuípe", "Conde", "Coração De Maria", "Coronel João Sá",
    "Crisópolis", "Cruz Das Almas", "Dom Macedo Costa", "Elísio Medrado", "Entre Rios", "Esplanada",
    "Euclides Da Cunha", "Fátima", "Feira De Santana", "Gavião", "Glória", "Governador Mangabeira",
    "Heliópolis", "Iaçu", "Ibiquera", "Ichu", "Inhambupe", "Ipecaetá", "Ipirá", "Iraquara", "rará",
    "Itaberaba", "Itaeté", "Itanagra", "Itapicuru", "Itatim", "Jaguaripe", "Jandaíra", "eremoabo",
    "Jiquiriçá", "Laje", "Lajedinho", "Lamarão", "Lençóis", "Macururé", "Maragogipe", "Marcionílio Souza",
    "Milagres", "Monte Santo", "Mucugê", "Muniz Ferreira", "Muritiba", "Mutuípe", "Nazaré", "Nordestina",
    "Nova Fátima", "Nova Redenção", "Nova Soure", "Novo Triunfo", "Olindina", "Ouriçangas", "Palmeiras",
    "Paripiranga", "Paulo Afonso", "Pé De Serra", "Pedrão", "Pedro Alexandre", "Pintadas", "Queimadas",
    "Quijingue", "Rafael Jambeiro", "Retirolândia", "Riachão Do Jacuípe", "Ribeira Do Amparo",
    "Ribeira Do Pombal","Rio Real", "Rodelas", "Ruy Barbosa", "Salinas Da Margarida", "Santa Bárbara",
    "Santa Brígida", "Santa Teresinha", "Santaluz", "Santanópolis", "Santo Amaro", "Santo Antônio De Jesus",
    "Santo Estêvão", "São Domingos", "São Felipe", "São Félix", "São Gonçalo Dos Campos", "São Miguel Das Matas",
    "Sapeaçu", "Sátiro Dias", "Seabra", "Serra Preta", "Serrinha", "Sítio Do Quinto", "Souto Soares", "Tanquinho",
    "Taperoá", "Teodoro Sampaio", "Teofilândia", "Terra Nova", "Tucano", "Ubaíra", "Utinga", "Valença", "Valente",
    "Varzedo", "Wagner"
]
ddd77 = [
    "Abaíra", "Anagé", "Angical", "Aracatu", "Baianópolis", "Barra Da Estiva", "Barra Do Choça", "Barreiras",
    "Belo Campo", "Boa Nova", "Bom Jesus Da Lapa", "Bom Jesus Da Serra", "Boquira", "Botuporã", "Brejolândia",
    "Brotas De Macaúbas","Brumado", "Buritirama", "Caatiba", "Caculé", "Caetanos", "Caetité", "Canápolis",
    "Candiba", "Cândido Sales", "Caraíbas", "Carinhanha", "Catolândia", "Caturama", "Cocos", "Condeúba",
    "Contendas Do Sincorá", "Cordeiros", "Coribe", "Correntina", "Cotegipe", "Cristópolis", "Dom Basílio",
    "Encruzilhada", "Érico Cardoso", "Feira Da Mata", "Formosa Do Rio Preto", "Guajeru", "Guanambi",
    "Ibiassucê", "Ibicoara", "Ibipitanga", "Ibitiara","Ibotirama", "Igaporã", "Ipupiara", "Iramaia",
    "Itambé", "Itapetinga", "Ituaçu", "Iuiú", "Jaborandi", "Jacaraci", "Jussiape", "Lagoa Real",
    "Licínio De Almeida", "Livramento Do Brumado", "Luis Eduardo Magalhaes", "Macarani", "Macaúbas",
    "Maetinga", "Maiquinique", "Malhada", "Malhada De Pedras", "Mansidão", "Matina", "Mirante",
    "Morpará", "Mortugaba", "Muquém De São Francisco", "Novo Horizonte", "Oliveira Dos Brejinhos",
    "Palmas De Monte Alto", "Paramirim", "Paratinga", "Piatã", "Pindaí", "Piripá", "Planalto",
    "Poções", "Presidente Jânio Quadros", "Riachão Das Neves", "Riacho De Santana", "Ribeirão Do Largo",
    "Rio De Contas", "Rio Do Antônio", "Rio Do Pires", "Santa Maria Da Vitória", "Santa Rita De Cássia",
    "Santana", "São Desidério","São Félix Do Coribe", "Sebastião Laranjeiras", "Serra Do Ramalho",
    "Serra Dourada", "Sítio Do Mato", "Tabocas Do Brejo Velho", "Tanhaçu", "Tanque Novo", "Tremedal",
    "Urandi", "Vitória Da Conquista", "Wanderley"
    ]
ddd85 = [
    "Acarapé", "Apuiarés", "Aquiraz", "Aracoiaba", "Aratuba", "Barreira", "Baturité", "Beberibe", "Canindé",
    "Capistrano", "Caridade", "Cascavel", "Caucaia", "Chorozinho", "Eusébio", "Fortaleza","General Sampaio",
    "Guaiúba", "Guaramiranga", "Horizonte", "Itaitinga", "Itapagé", "Maracanaú", "Maranguape", "Mulungu",
    "Ocara", "Pacajus", "Pacatuba", "Pacoti", "Palmácia", "Paracuru", "Paraipaba", "Paramoti", "Pentecoste",
    "Pindoretama", "Redenção", "São Gonçalo Do Amarante", "São Luís Do Curu", "Tejuçuoca", "Trairi", "Tururu",
    "Umirim", "Uruburetama"
]

def ExDDD92():
    for i in range(len(ddd92)):
        print(ddd92[i])
        time.sleep(0.01)
def ExDDD97():
    for i in range(len(ddd97)):
        print(ddd97[i])
        time.sleep(0.01)
def ExDDD71():
    for i in range(len(ddd71)):
        print(ddd71[i])
        time.sleep(0.01)
def ExDDD73():
    for i in range(len(ddd73)):
        print(ddd73[i])
        time.sleep(0.01)
def ExDDD74():
    for i in range(len(ddd74)):
        print(ddd74[i])
        time.sleep(0.01)
def ExDDD75():
    for i in range(len(ddd75)):
        print(ddd75[i])
        time.sleep(0.01)
def ExDDD77():
    for i in range(len(ddd77)):
        print(ddd77[i])
        time.sleep(0.01)
def ExDDD85():
    for i in range(len(ddd85)):
        print(ddd85[i])
        time.sleep(0.01)