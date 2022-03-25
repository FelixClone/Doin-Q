import time
ddd92 = (
     "Autazes", "Barreirinha", "Boa Vista Do Ramos", "Borba", "Caapiranga", "Careiro	Amazonas",
    "Careiro Da Varzea", "Iranduba", "Itacoatiara", "Itapiranga", "Manacapuru", "Manaquiri",
    "Manaus", "Maues", "Nhamunda", "Nova Olinda Do Norte", "Novo Airão", "Parintins",
    "Presidente Figueiredo", "Rio Preto Da Eva", "São Sebastião Do Uatuma", "Silves"
    "Urucara", "Urucurituba",
)
ddd97 = (
    "Alvaraes", "Amatura", "Anama", "Anori", "Apui", "Atalaia Do Norte", "Barcelos",
    "Benjamin" "Constant", "Beruri", "Boca Do Acre", "Canutama", "Carauari",
    "Coari", "Codajas", "Eirunepe", "Envira", "Fonte Boa", "Guajara", "Humaita",
    "Ipixuna", "Itamarati", "Japura", "Jurua", "Jutai", "Labrea", "Manicore",
    "Maraa", "Novo Aripuana", "Pauini", "Santa Isabel Do Rio Negro",
    "Santo Antonio Do Ica", "São Gabriel Da Cachoeira", "São Paulo De Olivenca",
    "Tabatinga", "Tapaua", "Tefe", "Tonantins", "Uarini",
)
ddd71 = (
    'Camacari', 'Candeias', 'Catu', 'Dias D` Avila', 'Itaparica', 'Lauro De Freitas',
    'Madre De Deus','Mata De São João', 'Pojuca', 'Salvador', 'São Francisco Do Conde',
    'São Sebastião Do Passe', 'Simões Filho', 'Vera Cruz',
)
ddd73 = (
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
    "Vereda", "Wenceslau Guimarães",
)
ddd74 = (
    'América Dourada', 'Andorinha', 'Antônio Gonçalves', 'Baixa Grande', 'Barra', 'Barra Do Mendes',
    'Barro Alto', 'Caém', 'Cafarnaum', 'Caldeirão Grande', 'Campo Alegre De Lourdes', 'Campo Formoso',
    'Canarana', 'Capim Grosso', 'Casa Nova', 'Central','Curaçá','Filadélfia','Gentio Do Ouro', 'Ibipeba',
    'Ibititá', 'Irecê', 'Itaguaçu Da Bahia', 'Itiúba', 'Jacobina', 'Jaguarari', 'João Dourado',
    'Juazeiro', 'Jussara', 'Lapão', 'Macajuba', 'Mairi', 'Miguel Calmon', 'Mirangaba',
    'Morro Do Chapéu', 'Mulungu Do Morro', 'Mundo Novo', 'Ourolândia', 'Pilão Arcado', 'Pindobaçu',
    'Piritiba', 'Ponto Novo', 'Presidente Dutra', 'Quixabeira', 'Remanso', 'São Gabriel',
    'São José Do Jacuípe', 'Saúde', 'Senhor Do Bonfim', 'Sento Sé', 'Serrolândia', 'Sobradinho',
    'Tapiramutá', 'Uauá', 'Uibaí', 'Umburanas', 'Várzea Da Roça', 'Várzea Do Poço', 'Várzea Nova',
    'Xique-Xique',
)
ddd75 = (
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
    "Varzedo", "Wagner",
)
ddd77 = (
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
    "Urandi", "Vitória Da Conquista", "Wanderley",
)
ddd85 = (
    "Acarapé", "Apuiarés", "Aquiraz", "Aracoiaba", "Aratuba", "Barreira", "Baturité", "Beberibe", "Canindé",
    "Capistrano", "Caridade", "Cascavel", "Caucaia", "Chorozinho", "Eusébio", "Fortaleza","General Sampaio",
    "Guaiúba", "Guaramiranga", "Horizonte", "Itaitinga", "Itapagé", "Maracanaú", "Maranguape", "Mulungu",
    "Ocara", "Pacajus", "Pacatuba", "Pacoti", "Palmácia", "Paracuru", "Paraipaba", "Paramoti", "Pentecoste",
    "Pindoretama", "Redenção", "São Gonçalo Do Amarante", "São Luís Do Curu", "Tejuçuoca", "Trairi", "Tururu",
    "Umirim", "Uruburetama",
)
ddd88 = (
    "Abaiara", "Acaraú", "Acopiara", "Aiuaba", "Alcântaras", "Altaneira", "Alto Santo", "Amontada",
    "Antonina Do Norte", "Aracati", "Ararendá", "Araripe", "Arneiroz", "Assaré", "Aurora", "Baixio",
    "Banabuiú", "Barbalha", "Barro", "Barroquinha", "Bela Cruz", "Boa Viagem", "Brejo Santo", "Camocim",
    "Campos Sales", "Cariré", "Caririaçu", "Cariús", "Cariús", "Carnaubal", "Catarina", "Catunda",
    "Cedro", "Chaval", "Choró", "Coreaú", "Crateús", "Crato", "Croatá", "Cruz", "Deputado Irapuan Pinheiro",
    "Ererê", "Farias Brito", "Forquilha", "Fortim", "Frecheirinha", "Graça", "Granja", "Granjeiro", "Groaíras",
    "Guaraciaba Do Norte", "Hidrolândia", "Ibaretama", "Ibiapina", "Ibicuitinga", "Icapuí", "Icó", "Iguatu",
    "Independência", "Ipaporanga", "Ipaumirim", "Ipu", "Ipueiras", "Iracema","Irauçuba", "Itaiçaba", "Itapipoca",
    "Itapiúna", "Itarema", "Itatira", "Jaguaretama", "Jaguaribara", "Jaguaribe", "Jaguaruana", "Jardim", "Jati",
    "Jijoca De Jericoacoara", "Juazeiro Do Norte", "Jucás", "Lavras Da Mangabeira","Limoeiro Do Norte", "Madalena",
    "Marco", "Martinópole", "Massapê", "Meruoca", "Milagres", "Milhã", "Miraíma", "Missão Velha", "Mombaça",
    "Monsenhor Tabosa", "Morada Nova", "Moraújo", "Morrinhos", "Mucambo","Nova Olinda", "Nova Russas", "Novo Oriente",
    "Orós", "Pacujá", "Palhano", "Parambu", "Pedra Branca", "Penaforte", "Pereiro", "Piquet Carneiro", "Pires Ferreira",
    "Poranga", "Porteiras", "Potengi", "Potiretama","Quiterianópolis", "Quixadá", "Quixelô", "Quixeramobim", "Quixeré",
    "Reriutaba", "Russas", "Saboeiro", "Salitre", "Santa Quitéria", "Santana Do Acaraú", "Santana Do Cariri", "São Benedito",
    "São João Do Jaguaribe", "Senador Pompeu", "Senador Sá", "Sobral", "Solonópole", "Tabuleiro Do Norte", "Tamboril", "Tarrafas",
    "Tauá", "Tianguá", "Ubajara", "Umari", "Uruoca", "Varjota", "Várzea Alegre", "Viçosa Do Ceará",
)
ddd27 = (
    "Afonso Cláudio", "Água Doce Do Norte", "Águia Branca", "Alfredo Chaves", "Alto Rio Novo", "Aracruz",
    "Barra De São Francisco", "Boa Esperança", "Brejetuba", "Cariacica", "Colatina", "Conceição Da Barra",
    "Domingos Martins", "Ecoporanga", "Fundão", "Governador Lindenberg","Guarapari", "Ibiraçu", "Itaguaçu",
    "Itarana", "Jaguaré", "João Neiva", "Laranja Da Terra", "Linhares", "Mantenópolis", "Marechal Floriano",
    "Marilândia", "Montanha", "Mucurici", "Nova Venécia", "Pancas", "Pedro Canário","Pinheiros", "Ponto Belo",
    "Rio Bananal", "Santa Leopoldina", "Santa Maria De Jetibá", "Santa Teresa", "São Domingos Do Norte",
    "São Gabriel Da Palha", "São Mateus", "São Roque Do Canaã", "Serra", "Sooretama", "Viana", "Vila Pavão",
    "Vila Valério", "Vila Velha", "Vitória",
)
ddd28 = (
    "Alegre", "Anchieta", "Apiacá", "Atilio Vivacqua", "Bom Jesus Do Norte", "Cachoeiro De Itapemirim", "Castelo", "Conceição Do Castelo",
    "Divino De São Lourenço", "Dores Do Rio Preto", "Guaçuí", "Ibatiba", "Ibitirama", "Iconha", "Irupi", "Iúna","Jerônimo Monteiro",
    "Marataizes", "Mimoso Do Sul", "Muniz Freire", "Muqui", "Piúma", "Presidente Kennedy", "Rio Novo Do Sul", "São José Do Calçado",
    "Vargem Alta", "Venda Nova Do Imigrante"
)
ddd61 = (
    "Águas Lindas De Goiás – GO", "Brasília – DF", "Cabeceiras – GO", "Cidade Ocidental – GO", "Cristalina – GO",
    "Formosa – GO", "Luziânia – GO", "Novo Gama – GO", "Padre Bernardo – GO", "Planaltina – GO", "Santo Antônio Do Descoberto – GO",
    "Valparaíso De Goiás – GO", "Vila Boa – GO", "Ceilândia – DF", "Samambaia – DF", "Taguatinga – DF","Plano Piloto – DF",
    "Planaltina – DF", "Águas Claras – DF", "Recanto das Emas – DF", "Gama – DF", "Guará – DF", "Santa Maria – DF",
    "Sobradinho II – DF", "São Sebastião – DF", "Vicente Pires – DF", "Itapoã – DF", "Sobradinho – DF", "Sudoeste/Octagonal – DF",
    "Brazlândia – DF", "Riacho Fundo II – DF", "Paranoá – DF","Riacho Fundo – DF", "SCIA – DF", "Lago Norte – DF", "Cruzeiro – DF",
    "Lago Sul – DF", "Jardim Botânico – DF", "Núcleo Bandeirante – DF", "Park Way – DF", "Candangolândia – DF", "Varjão – DF",
    "Fercal – DF", "SIA - DF",
)
ddd62 = (
    "Abadia De Goiás", "Abadiânia", "Água Fria De Goiás", "Alexânia", "Alto Horizonte", "Alto Paraíso De Goiás",
    "Alvorada Do Norte", "Amaralina", "Anápolis", "Aparecida De Goiânia", "Araçu", "Aragoiânia", "Araguapaz",
    "Aruanã", "Barro Alto", "Bela Vista De Goiás","Bonfinópolis", "Bonópolis", "Brazabrantes", "Britânia",
    "Buritinópolis", "Caldazinha", "Campestre De Goiás", "Campinaçu", "Campinorte", "Campo Limpo De Goias",
    "Campos Belos", "Campos Verdes", "Carmo Do Rio Verde", "Caturaí", "Cavalcante", "Ceres","Cocalzinho De Goiás",
    "Colinas Do Sul", "Corumbá De Goiás", "Crixás", "Damianópolis", "Damolândia", "Divinópolis De Goiás",
    "Estrela Do Norte", "Faina", "Fazenda Nova", "Flores De Goiás", "Formoso", "Gameleira De Goias", "Goianápolis",
    "Goianésia", "Goiânia", "Goianira", "Goiás", "Guapó", "Guaraíta", "Guarani De Goiás", "Guarinos", "Heitoraí",
    "Hidrolândia", "Hidrolina", "Iaciara", "Inhumas", "Ipiranga De Goias", "Itaberaí", "Itaguari", "Itaguaru",
    "Itapaci","Itapirapuã", "Itapuranga", "Itauçu", "Jaraguá", "Jesúpolis", "Jussara", "Leopoldo De Bulhões",
    "Mambaí", "Mara Rosa", "Matrinchã", "Mimoso De Goiás", "Minaçu", "Monte Alegre De Goiás", "Montes Claros De Goiás",
    "Montividiu Do Norte", "Morro Agudo De Goiás", "Mozarlândia", "Mundo Novo", "Mutunópolis", "Nerópolis", "Niquelândia",
    "Nova América", "Nova Crixás", "Nova Glória", "Nova Iguaçu De Goiás", "Nova Roma", "Nova Veneza", "Novo Brasil",
    "Novo Planalto", "Ouro Verde De Goiás", "Petrolina De Goiás", "Pilar De Goiás","Pirenópolis", "Porangatu", "Posse",
    "Rialma", "Rianápolis", "Rubiataba", "Santa Bárbara De Goiás", "Santa Fé De Goiás", "Santa Isabel", "Santa Rita Do Novo Destino",
    "Santa Rosa De Goiás", "Santa Tereza De Goiás", "Santa Terezinha De Goiás", "Santo Antônio De Goiás", "São Domingos", "São Francisco De Goiás",
    "São João D’aliança", "São Luíz Do Norte", "São Miguel Do Araguaia", "São Miguel Do Passa Quatro", "São Patrício", "Senador Canedo",
    "Silvânia", "Simolândia", "Sítio D’abadia", "Taquaral De Goiás", "Teresina De Goiás", "Terezópolis De Goiás", "Trindade", "Trombas",
    "Uirapuru", "Uruaçu", "Uruana", "Uruana", "Vianópolis", "Vila Propicio",
)
ddd64 = (
    "Acreúna", "Adelândia", "Água Limpa", "Aloândia", "Americano Do Brasil", "Amorinópolis", "Anhanguera",
    "Anicuns", "Aparecida Do Rio Doce", "Aporé", "Aragarças", "Arenópolis", "Aurilândia", "Avelinópolis",
    "Baliza", "Bom Jardim De Goiás", "Bom Jesus", "Buriti Alegre", "Buriti De Goiás", "Cachoeira Alta",
    "Cachoeira De Goiás", "Cachoeira Dourada", "Caçu", "Caiapônia", "Caldas Novas", "Campo Alegre De Goiás",
    "Castelândia", "Catalão","Cezarina", "Chapadão Do Céu", "Córrego Do Ouro", "Corumbaíba", "Cristianópolis",
    "Cromínia", "Cumari", "Davinópolis", "Diorama", "Doverlândia", "Edealina", "Edéia", "Firminópolis", "Goiandira",
    "Goiatuba", "Gouvelândia", "Inaciolândia", "Indiara", "Ipameri", "Iporá", "Israelândia", "Itajá", "Itarumã", "Itumbiara",
    "Ivolândia", "Jandaia", "Jataí", "Jaupaci", "Joviânia", "Lagoa Santa", "Mairipotaba", "Marzagão", "Maurilândia", "Mineiros",
    "Moiporá", "Montividiu", "Morrinhos", "Mossâmedes", "Nazário", "Nova Aurora", "Orizona", "Ouvidor", "Palestina De Goiás",
    "Palmeiras De Goiás", "Palmelo", "Palminópolis", "Panamá", "Paranaiguara","Paraúna", "Perolândia", "Piracanjuba", "Piranhas",
    "Pires Do Rio", "Pontalina", "Porteirão", "Portelândia", "Professor Jamil", "Quirinópolis", "Rio Quente", "Rio Verde",
    "Sanclerlândia", "Santa Cruz De Goiás", "Santa Helena De Goiás", "Santa Rita Do Araguaia","Santo Antônio Da Barra",
    "São João Da Paraúna", "São Luís De Montes Belos", "São Simão", "Serranópolis", "Três Ranchos", "Turvânia", "Turvelândia",
    "Urutaí", "Vicentinópolis",
)
ddd98 = (
    "Afonso Cunha", "Água Doce Do Maranhão", "Alcântara", "Altamira Do Maranhão", "Alto Alegre Do Pindaré",
    "Amapá Do Maranhão", "Anajatuba", "Anapurus", "Apicum-Açu", "Araguanã", "Araioses", "Arari", "Axixá",
    "Bacabeira", "Bacuri", "Bacurituba", "Barreirinhas", "Bela Vista Do Maranhão", "Belágua", "Bequimão",
    "Boa Vista Do Gurupi", "Bom Jardim", "Bom Jesus Das Selvas", "Brejo", "Brejo De Areia", "Buriti",
    "Buriticupu", "Cachoeira Grande","Cajapió", "Cajari", "Cândido Mendes", "Cantanhede", "Carutapera",
    "Cedral", "Central Do Maranhão", "Centro Do Guilherme", "Centro Novo Do Maranhão", "Chapadinha",
    "Coelho Neto", "Conceição Do Lago-Açu", "Cururupu", "Duque Bacelar", "Godofredo Viana",
    "Governador Newton Bello","Governador Nunes Freire", "Guimarães", "Humberto De Campos", "Icatu",
    "Igarapé Do Meio", "Itapecuru Mirim", "Junco Do Maranhão", "Luís Domingues", "Magalhães De Almeida",
    "Maracaçumé", "Marajá Do Sena", "Maranhãozinho", "Mata Roma", "Matinha", "Matões Do Norte",
    "Milagres Do Maranhão", "Miranda Do Norte", "Mirinzal", "Monção", "Morros", "Nina Rodrigues",
    "Nova Olinda Do Maranhão", "Olho D’água Das Cunhãs", "Olinda Nova Do Maranhão", "Paço Do Lumiar",
    "Palmeirândia", "Paulino Neves", "Paulo Ramos", "Pedro Do Rosário", "Penalva", "Peri Mirim", "Pindaré Mirim",
    "Pinheiro", "Pio Xii", "Pirapemas", "Porto Rico Do Maranhão", "Presidente Juscelino", "Presidente Médici",
    "Presidente Sarney", "Presidente Vargas", "Primeira Cruz", "Raposa", "Rosário", "Santa Helena", "Santa Inês",
    "Santa Luzia", "Santa Luzia Do Paruá", "Santa Quitéria Do Maranhão","Santa Rita", "Santana Do Maranhão",
    "Santo Amaro Do Maranhão", "São Benedito Do Rio Preto", "São Bento", "São Bernardo", "São João Batista",
    "São João Do Carú", "São José De Ribamar", "São Luís", "São Vicente Ferrer", "Satubinha", "Serrano Do Maranhão",
    "Tufilândia", "Turiaçu", "Turilândia","Tutóia", "Urbano Santos", "Vargem Grande", "Viana", "Vitória Do Mearim",
    "Vitorino Freire", "Zé Doca",
)

ddd99 = (
    "Açailândia", "Aldeias Altas", "Alto Alegre Do Maranhão", "Alto Parnaíba", "Amarante Do Maranhão",
    "Arame", "Bacabal", "Balsas", "Barão De Grajaú", "Barra Do Corda", "Benedito Leite", "Bernardo Do Mearim",
    "Bom Lugar", "Buriti Bravo", "Buritirana", "Campestre Do Maranhão", "Capinzal Do Norte", "Carolina",
    "Caxias", "Cidelândia", "Codó", "Colinas", "Coroatá", "Davinópolis", "Dom Pedro", "Esperantinópolis",
    "Estreito", "Feira Nova Do Maranhão", "Fernando Falcão", "Formosa Da Serra Negra", "Fortaleza Dos Nogueiras",
    "Fortuna", "Gonçalves Dias", "Governador Archer", "Governador Edison Lobão", "Governador Eugênio Barros",
    "Governador Luiz Rocha", "Graça Aranha", "Grajaú", "Igarapé Grande", "Imperatriz", "Itaipava Do Grajaú",
    "Itinga Do Maranhão", "Jatobá", "Jenipapo Dos Vieiras", "João Lisboa", "Joselândia", "Lago Da Pedra",
    "Lago Do Junco", "Lago Dos Rodrigues", "Lago Verde", "Lagoa Do Mato", "Lagoa Grande Do Maranhão",
    "Lajeado Novo", "Lima Campos", "Loreto", "Matões", "Mirador", "Montes Altos", "Nova Colinas", "Nova Iorque",
    "Paraibano", "Parnarama", "Passagem Franca", "Pastos Bons", "Pedreiras", "Peritoró", "Poção De Pedras", "Porto Franco",
    "Presidente Dutra", "Riachão", "Ribamar Fiquene", "Sambaíba", "Santa Filomena Do Maranhão", "Santo Antônio Dos Lopes",
    "São Domingos Do Azeitão", "São Domingos Do Maranhão", "São Félix De Balsas", "São Francisco Do Brejão",
    "São Francisco Do Maranhão", "São João Do Paraíso", "São João Do Soter", "São João Dos Patos", "São José Dos Basílios",
    "São Luís Gonzaga Do Maranhão", "São Mateus Do Maranhão", "São Pedro Da Água Branca", "São Pedro Dos Crentes",
    "São Raimundo Das Mangabeiras", "São Raimundo Do Doca Bezerra", "São Roberto", "Senador Alexandre Costa", "Senador La Rocque",
    "Sítio Novo", "Sucupira Do Norte", "Sucupira Do Riachão", "Tasso Fragoso", "Timbiras", "Timon", "Trizidela Do Vale",
    "Tuntum", "Vila Nova Dos Martírios",
)
ddd65 = (
    "Acorizal", "Alto Paraguai", "Araputanga", "Arenápolis", "Barão De Melgaço", "Barra Do Bugres",
    "Cáceres", "Campo Novo Do Parecis", "Campos De Júlio", "Chapada Dos Guimarães", "Comodoro",
    "Conquista Do Oeste", "Cuiabá", "Curvelandia", "Denise", "Diamantino", "Figueirópolis D'oeste",
    "Glória D'oeste", "Indiavaí", "Itiquira", "Jangada", "Jauru", "Lambari D'oeste", "Lucas Do Rio Verde",
    "Mirassol D'oeste", "Nobres", "Nortelândia", "Nossa Senhora Do Livramento", "Nova Lacerda", "Nova Marilândia",
    "Nova Mutum", "Nova Olímpia", "Poconé", "Pontes E Lacerda", "Porto Esperidião", "Porto Estrela", "Reserva Do Cabaçal",
    "Rio Branco", "Rosário Oeste", "Salto Do Céu", "Santa Rita Do Trivelato", "Santo Afonso", "Santo Antônio Do Leverger",
    "São José Do Rio Claro", "São José Dos Quatro Marcos", "Sapezal", "Tangará Da Serra", "Vale De São Domingos", "Várzea Grande",
    "Vila Bela Da Santíssima Trindade",
)
ddd66 = (
    'Água Boa', 'Alta Floresta', 'Alto Araguaia', 'Alto Boa Vista', 'Alto Garças', 'Alto Taquari', 'Apiacás',
    'Araguaiana', 'Araguainha', 'Aripuanã', 'Barra Do Garças', 'Bom Jesus Do Araguaia', 'Brasnorte', 'Campinápolis',
    'Campo Verde', 'Canabrava Do Norte', 'Canarana', 'Carlinda', 'Castanheira', 'Cláudia', 'Cocalinho', 'Colíder',
    'Colniza', 'Confresa', 'Cotriguaçu', 'Dom Aquino', 'Feliz Natal', 'Gaúcha Do Norte', 'General Carneiro', 'Guarantã Do Norte',
    'Guiratinga', 'Itaúba', 'Jaciara', 'Juara', 'Juína', 'Juruena', 'Juscimeira', 'Luciára', 'Marcelândia', 'Matupá',
    'Nova Bandeirantes', 'Nova Brasilândia', 'Nova Canãa Do Norte', 'Nova Guarita', 'Nova Maringá', 'Nova Monte Verde',
    'Nova Nazaré', 'Nova Santa Helena', 'Nova Ubiratã', 'Nova Xavantina', 'Novo Horizonte Do Norte', 'Novo Mundo',
    'Novo Santo Antonio', 'Novo São Joaquim', 'Paranaíta', 'Paranatinga', 'Pedra Preta', 'Peixoto De Azevedo',
    'Planalto Da Serra', 'Pontal Do Araguaia', 'Ponte Branca', 'Porto Alegre Do Norte', 'Porto Dos Gaúchos',
    'Poxoréo', 'Primavera Do Leste', 'Querência', 'Ribeirão Cascalheira', 'Ribeirãozinho', 'Rondolandia',
    'Rondonópolis', 'Santa Carmem', 'Santa Cruz Do Xingu', 'Santa Terezinha', 'Santo Antonio Do Leste',
    'São Félix Do Araguaia', 'São José Do Povo', 'São José Do Xingu', 'São Pedro Da Cipa', 'Serra Nova Dourada',
    'Sinop', 'Sorriso', 'Tabaporã', 'Tapurah', 'Terra Nova Do Norte', 'Tesouro', 'Torixoréu', 'União Do Sul',
    'Vera', 'Vila Rica',
)

ddd31 = (
    'Abre Campo', 'Acaiaca', 'Alvinópolis', 'Alvorada De Minas', 'Amparo Do Serra', 'Antônio Dias',
    'Araçaí', 'Araponga', 'Baldim', 'Barão De Cocais', 'Barra Longa', 'Bela Vista De Minas',
    'Belo Horizonte', 'Belo Oriente', 'Belo Vale', 'Betim', 'Bom Jesus Do Amparo', 'Bonfim',
    'Brumadinho', 'Cachoeira Da Prata', 'Caetanópolis', 'Caeté', 'Cajuri', 'Canaã', 'Capela Nova',
    'Capim Branco', 'Caputira', 'Caranaíba', 'Carmésia', 'Casa Grande', 'Catas Altas', 'Catas Altas Da Noruega',
    'Conceição Do Mato Dentro', 'Confins', 'Congonhas', 'Congonhas Do Norte', 'Conselheiro Lafaiete', 'Contagem',
    'Cordisburgo', 'Coronel Fabriciano', 'Cristiano Otoni', 'Crucilândia', 'Desterro De Entre Rios', 'Diogo De Vasconcelos',
    'Dionísio', 'Dom Joaquim', 'Dom Silvério', 'Entre Rios De Minas', 'Esmeraldas', 'Ferros', 'Florestal', 'Fortuna De Minas',
    'Funilândia', 'Guaraciaba', 'Ibirité', 'Igarapé', 'Inhaúma', 'Ipaba', 'Ipatinga', 'Itabira', 'Itabirito', 'Itaguara',
    'Itambé Do Mato Dentro', 'Itatiaiuçu', 'Itaverava', 'Jaboticatubas', 'Jaguaraçu', 'Jeceaba', 'Jequeri', 'Jequitibá',
    'João Monlevade', 'Juatuba', 'Lagoa Santa', 'Lamim', 'Mariana', 'Mário Campos', 'Marliéria', 'Mateus Leme', 'Matipó',
    'Matozinhos', 'Moeda', 'Morro Do Pilar', 'Nova Era', 'Nova Lima', 'Nova União', 'Oratórios', 'Ouro Branco', 'Ouro Preto',
    'Paraopeba', 'Passabém', 'Pedra Bonita', 'Pedra Do Anta', 'Pedro Leopoldo', 'Piedade De Ponte Nova', 'Piedade Dos Gerais',
    'Piranga', 'Ponte Nova', 'Porto Firme', 'Prudente De Morais', 'Queluzita', 'Raposos', 'Ribeirão Das Neves', 'Rio Acima',
    'Rio Casca', 'Rio Doce', 'Rio Espera', 'Rio Manso', 'Rio Piracicaba', 'Sabará', 'Santa Bárbara', 'Santa Cruz Do Escalvado',
    'Santa Luzia', 'Santa Margarida', 'Santa Maria De Itabira', 'Santana De Pirapama', 'Santana Do Paraíso', 'Santana Do Riacho',
    'Santana Dos Montes', 'Santo Antônio Do Grama', 'Santo Antônio Do Rio Abaixo', 'São Brás Do Suaçuí', 'São Domingos Do Prata',
    'São Gonçalo Do Rio Abaixo', 'São Joaquim De Bicas', 'São José Da Lapa', 'São José Do Goiabal', 'São Miguel Do Anta',
    'São Sebastião Do Rio Preto', 'Sarzedo', 'Sem-Peixe', 'Senhora De Oliveira', 'Sericita', 'Sete Lagoas', 'Taquaraçu De Minas',
    'Teixeiras', 'Timóteo', 'Urucânia', 'Vespasiano', 'Viçosa',
)

ddd32 = (
    'Além Paraíba', 'Alfredo Vasconcelos', 'Alto Caparaó', 'Alto Rio Doce', 'Antônio Carlos', 'Antônio Prado De Minas',
    'Aracitaba', 'Arantina', 'Argirita', 'Astolfo Dutra', 'Barão De Monte Alto', 'Barbacena', 'Barroso', 'Bias Fortes',
    'Bicas', 'Bocaina De Minas', 'Bom Jardim De Minas', 'Brás Pires', 'Caiana', 'Caparaó', 'Carandaí', 'Carangola',
    'Cataguases', 'Chácara', 'Chiador', 'Cipotânea', 'Coimbra', 'Conceição Da Barra De Minas', 'Coronel Pacheco',
    'Coronel Xavier Chaves', 'Descoberto', 'Desterro Do Melo', 'Divinésia', 'Divino', 'Dona Euzébia', 'Dores De Campos',
    'Dores Do Turvo', 'Ervália', 'Espera Feliz', 'Estrela Dalva', 'Eugenópolis', 'Ewbank Da Câmara', 'Faria Lemos',
    'Fervedouro', 'Goianá', 'Guarani', 'Guarará', 'Guidoval', 'Guiricema', 'Ibertioga', 'Itamarati De Minas', 'Juiz De Fora',
    'Lagoa Dourada', 'Laranjal', 'Leopoldina', 'Liberdade', 'Lima Duarte', 'Madre De Deus De Minas', 'Mar De Espanha',
    'Maripá De Minas', 'Matias Barbosa', 'Mercês', 'Miradouro', 'Miraí', 'Muriaé', 'Olaria', 'Oliveira Fortes', 'Orizânia',
    'Paiva', 'Palma', 'Passa Vinte', 'Patrocínio Do Muriaé', 'Paula Cândido', 'Pedra Dourada', 'Pedro Teixeira', 'Pequeri',
    'Piau', 'Piedade Do Rio Grande', 'Pirapetinga', 'Piraúba', 'Prados', 'Presidente Bernardes', 'Recreio', 'Resende Costa',
    'Ressaquinha', 'Rio Novo', 'Rio Pomba', 'Rio Preto', 'Ritápolis', 'Rochedo De Minas', 'Rodeiro', 'Rosário Da Limeira',
    'Santa Bárbara Do Monte Verde', 'Santa Bárbara Do Tugúrio', 'Santa Cruz De Minas', 'Santa Rita De Ibitipoca',
    'Santa Rita De Jacutinga', 'Santana De Cataguases', 'Santana Do Deserto', 'Santana Do Garambéu', 'Santo Antônio Do Aventureiro',
    'Santos Dumont', 'São Francisco Do Glória', 'São Geraldo', 'São João Del Rei', 'São João Nepomuceno', 'São Sebastião Da Vargem Alegre',
    'São Tiago', 'Senador Cortes', 'Senador Firmino', 'Senhora Dos Remédios', 'Silveirânia', 'Simão Pereira', 'Tabuleiro', 'Tiradentes',
    'Tocantins', 'Tombos', 'Ubá', 'Vieiras', 'Visconde Do Rio Branco', 'Volta Grande',
)

ddd33 = (
    'Açucena', 'Água Boa', 'Águas Formosas', 'Águas Vermelhas', 'Aimorés', 'Almenara', 'Alpercata', 'Alto Jequitibá',
    'Alvarenga','Angelândia', 'Araçuaí', 'Ataléia', 'Bandeira', 'Berilo', 'Bertópolis', 'Bom Jesus Do Galho', 'Braúnas',
    'Bugre', 'Cachoeira De Pajeú','Campanário', 'Cantagalo', 'Capelinha', 'Capitão Andrade', 'Caraí', 'Caratinga',
    'Carlos Chagas', 'Catuji', 'Central De Minas', 'Chalé', 'Chapada Do Norte', 'Coluna', 'Comercinho', 'Conceição De Ipanema',
    'Conselheiro Pena', 'Coroaci', 'Coronel Murta', 'Córrego Novo', 'Crisólita', 'Cuparaque', 'Curral De Dentro', 'Divino Das Laranjeiras',
    'Divinolândia De Minas', 'Divisa Alegre', 'Divisópolis', 'Dom Cavati', 'Dores De Guanhães', 'Durandé', 'Engenheiro Caldas',
    'Entre Folhas', 'Felisburgo', 'Fernandes Tourinho', 'Francisco Badaró', 'Franciscópolis', 'Frei Gaspar', 'Frei Inocêncio',
    'Frei Lagonegro', 'Fronteira Dos Vales', 'Galiléia', 'Goiabeira', 'Gonzaga', 'Governador Valadares', 'Guanhães', 'Iapu',
    'Imbé De Minas', 'Inhapim', 'Ipanema', 'Itabirinha De Mantena', 'Itaipé', 'Itambacuri', 'Itanhomi', 'Itaobim', 'Itinga',
    'Itueta', 'Jacinto', 'Jampruca', 'Jenipapo De Minas', 'Jequitinhonha', 'Joaíma', 'Joanésia', 'Jordânia', 'José Gonçalves De Minas',
    'José Raydan', 'Ladainha', 'Lajinha', 'Leme Do Prado', 'Luisburgo', 'Machacalis', 'Malacacheta', 'Manhuaçu', 'Manhumirim',
    'Mantena', 'Marilac', 'Martins Soares', 'Mata Verde', 'Materlândia', 'Mathias Lobato', 'Medina', 'Mendes Pimentel',
    'Mesquita', 'Minas Novas', 'Monte Formoso', 'Mutum', 'Nacip Raydan', 'Nanuque', 'Naque', 'Nova Belém', 'Nova Módica',
    'Novo Cruzeiro', 'Novo Oriente De Minas', 'Ouro Verde De Minas', 'Padre Paraíso', 'Palmópolis', 'Paulistas', 'Pavão',
    'Peçanha', 'Pedra Azul', 'Periquito', 'Pescador', 'Piedade De Caratinga', 'Pingo D’água', 'Pocrane', 'Ponto Dos Volantes',
    'Poté', 'Raul Soares', 'Reduto', 'Resplendor', 'Rio Do Prado', 'Rio Vermelho', 'Rubim', 'Sabinópolis', 'Salto Da Divisa',
    'Santa Bárbara Do Leste', 'Santa Efigênia De Minas', 'Santa Helena De Minas', 'Santa Maria Do Salto', 'Santa Maria Do Suaçuí',
    'Santa Rita De Minas', 'Santa Rita Do Itueto', 'Santana Do Manhuaçu', 'Santo Antônio Do Itambé', 'Santo Antônio Do Jacinto',
    'São Domingos Das Dores', 'São Félix De Minas', 'São Geraldo Da Piedade', 'São Geraldo Do Baixio', 'São João Do Manhuaçu',
    'São João Do Manteninha', 'São João Do Oriente', 'São João Evangelista', 'São José Da Safira', 'São José Do Divino',
    'São José Do Jacuri', 'São José Do Mantimento', 'São Pedro Do Suaçuí', 'São Pedro Dos Ferros', 'São Sebastião Do Anta',
    'São Sebastião Do Maranhão', 'Sardoá', 'Senhora Do Porto', 'Serra Dos Aimorés', 'Setubinha', 'Simonésia', 'Sobrália',
    'Taparuba', 'Tarumirim', 'Teófilo Otoni', 'Tumiritinga', 'Ubaporanga', 'Umburatiba', 'Vargem Alegre', 'Vermelho Novo',
    'Virgem Da Lapa', 'Virginópolis', 'Virgolândia',    
)

ddd34 = (
    'Abadia Dos Dourados', 'Água Comprida', 'Araguari', 'Araporã', 'Arapuá', 'Araxá', 'Cachoeira Dourada',
    'Campina Verde', 'Campo Florido', 'Canápolis', 'Capinópolis', 'Carmo Do Paranaíba', 'Carneirinho',
    'Cascalho Rico', 'Centralina', 'Claraval', 'Comendador Gomes', 'Conceição Das Alagoas', 'Conquista',
    'Coromandel', 'Cruzeiro Da Fortaleza', 'Delta', 'Douradoquara', 'Estrela Do Sul', 'Fronteira',
    'Frutal', 'Grupiara', 'Guimarânia', 'Gurinhatã', 'Ibiá', 'Indianópolis', 'Ipiaçu', 'Iraí De Minas',
    'Itapagipe', 'Ituiutaba', 'Iturama', 'Lagamar', 'Lagoa Formosa', 'Lagoa Grande', 'Limeira Do Oeste',
    'Matutina', 'Monte Alegre De Minas', 'Monte Carmelo', 'Nova Ponte', 'Patos De Minas', 'Patrocínio',
    'Pedrinópolis', 'Perdizes', 'Pirajuba', 'Planura', 'Prata', 'Pratinha', 'Presidente Olegário',
    'Rio Paranaíba', 'Romaria', 'Sacramento', 'Santa Juliana', 'Santa Rosa Da Serra', 'Santa Vitória',
    'São Francisco De Sales', 'São Gotardo', 'Serra Do Salitre', 'Tapira', 'Tiros', 'Tupaciguara',
    'Uberaba', 'Uberlândia', 'União De Minas', 'Vazante', 'Veríssimo',
)

ddd35 = (
    'Aguanil', 'Aiuruoca', 'Alagoa', 'Albertina', 'Alfenas', 'Alpinópolis', 'Alterosa', 'Andradas',
    'Andrelândia', 'Arceburgo', 'Areado', 'Baependi', 'Bandeira Do Sul', 'Boa Esperança', 'Bom Jesus Da Penha',
    'Bom Repouso', 'Bom Sucesso', 'Borda Da Mata', 'Botelhos', 'Brasópolis', 'Bueno Brandão', 'Cabo Verde',
    'Cachoeira De Minas', 'Caldas', 'Camanducaia', 'Cambuí', 'Cambuquira', 'Campanha', 'Campestre', 'Campo Belo',
    'Campo Do Meio', 'Campos Gerais', 'Cana Verde', 'Candeias', 'Capetinga', 'Careaçu', 'Carmo Da Cachoeira',
    'Carmo De Minas', 'Carmo Do Rio Claro', 'Carrancas', 'Carvalhópolis', 'Carvalhos', 'Cássia', 'Caxambu',
    'Conceição Da Aparecida', 'Conceição Das Pedras', 'Conceição Do Rio Verde', 'Conceição Dos Ouros',
    'Congonhal', 'Consolação', 'Coqueiral', 'Cordislândia', 'Córrego Do Bom Jesus', 'Cristais', 'Cristina',
    'Cruzília', 'Delfim Moreira', 'Delfinópolis', 'Divisa Nova', 'Dom Viçoso', 'Elói Mendes',
    'Espírito Santo Do Dourado', 'Estiva', 'Extrema', 'Fama', 'Fortaleza De Minas', 'Gonçalves', 'Guapé',
    'Guaranésia', 'Guaxupé', 'Heliodora', 'Ibiraci', 'Ibitiúra De Minas', 'Ibituruna', 'Ijaci', 'Ilicínea',
    'Inconfidentes', 'Ingaí', 'Ipuiúna', 'Itajubá', 'Itamogi', 'Itamonte', 'Itanhandu', 'Itapeva', 'Itaú De Minas',
    'Itumirim', 'Itutinga', 'Jacuí', 'Jacutinga', 'Jesuânia', 'Juruaia', 'Lambari', 'Lavras', 'Luminárias',
    'Machado', 'Maria Da Fé', 'Marmelópolis', 'Minduri', 'Monsenhor Paulo', 'Monte Belo', 'Monte Santo De Minas',
    'Monte Sião', 'Munhoz', 'Muzambinho', 'Natércia', 'Nazareno', 'Nepomuceno', 'Nova Resende', 'Olímpio Noronha',
    'Ouro Fino', 'Paraguaçu', 'Paraisópolis', 'Passa Quatro', 'Passos', 'Pedralva', 'Perdões', 'Piranguçu',
    'Piranguinho', 'Poço Fundo', 'Poços De Caldas', 'Pouso Alegre', 'Pouso Alto', 'Pratápolis', 'Ribeirão Vermelho',
    'Santa Rita De Caldas', 'Santa Rita Do Sapucaí', 'Santana Da Vargem', 'Santana Do Jacaré', 'Santo Antônio Do Amparo',
    'São Bento Abade', 'São Gonçalo Do Sapucaí', 'São João Batista Do Glória', 'São João Da Mata', 'São José Da Barra',
    'São José Do Alegre', 'São Lourenço', 'São Pedro Da União', 'São Sebastião Da Bela Vista', 'São Sebastião Do Paraíso',
    'São Sebastião Do Rio Verde', 'São Thome Das Letras', 'São Tomás De Aquino', 'São Vicente De Minas', 'Sapucaí-Mirim',
    'Senador Amaral', 'Senador José Bento', 'Seritinga', 'Serrania', 'Serranos', 'Silvianópolis', 'Soledade De Minas',
    'Tocos Do Mogi', 'Toledo', 'Três Corações', 'Três Pontas', 'Turvolândia', 'Varginha', 'Virgínia', 'Wenceslau Braz',
)

ddd37 = (
    "Abaeté", "Araújos", "Arcos", "Bambuí", "Biquinhas", "Bom Despacho", "Camacho", "Campos Altos", "Capitólio",
    "Carmo Da Mata", "Carmo Do Cajuru", "Carmópolis De Minas", "Cedro Do Abaeté", "Cláudio", "Conceição Do Pará",
    "Córrego Danta", "Córrego Fundo", "Divinópolis", "Dores Do Indaiá", "Doresópolis", "Estrela Do Indaiá",
    "Formiga", "Igaratinga", "Iguatama", "Itapecerica", "Itaúna", "Japaraíba", "Lagoa Da Prata", "Leandro Ferreira",
    "Luz", "Maravilhas", "Martinho Campos", "Medeiros", "Moema", "Morada Nova De Minas", "Nova Serrana", "Oliveira",
    "Onça De Pitangui", "Paineiras", "Pains", "Papagaios", "Pará De Minas", "Passa Tempo", "Pedra Do Indaiá", "Pequi",
    "Perdigão", "Pimenta", "Piracema", "Pitangui", "Piuí", "Pompéu", "Quartel Geral", "Santo Antônio Do Monte",
    "São Francisco De Paula", "São Gonçalo Do Pará", "São José Da Varginha", "São Roque De Minas", "São Sebastião Do Oeste",
    "Serra Da Saudade", "Tapiraí", "Vargem Bonita",
)

ddd41 = (
    'Adrianópolis', 'Agudos Do Sul', 'Almirante Tamandaré', 'Antonina', 'Araucária', 'Balsa Nova',
    'Bocaiúva Do Sul', 'Campina Grande Do Sul', 'Campo Do Tenente', 'Campo Largo', 'Campo Magro',
    'Cerro Azul', 'Colombo', 'Contenda', 'Curitiba', 'Doutor Ulysses', 'Fazenda Rio Grande',
    'Guaraqueçaba', 'Guaratuba', 'Itaperuçu', 'Lapa', 'Mandirituba', 'Matinhos', 'Morretes',
    'Paranaguá', 'Piên', 'Pinhais', 'Piraquara', 'Pontal Do Paraná', 'Quatro Barras',
    'Quitandinha', 'Rio Branco Do Sul', 'Rio Negro', 'São José Dos Pinhais', 'Tijucas Do Sul',
    'Tunas Do Paraná',
)

ddd42 = ( #Remember: Sc this mixed with Pr
    'Antônio Olinto', 'Bituruna', 'Boa Ventura De São Roque', 'Campina Do Simão', 'Candói', 'Cantagalo',
    'Carambeí', 'Castro', 'Cruz Machado', 'Fernandes Pinheiro', 'Foz Do Jordão', 'General Carneiro',
    'Goioxim', 'Guamiranga', 'Guarapuava', 'Imbaú', 'Imbituva', 'Inácio Martins', 'Ipiranga', 'Irati',
    'Ivaí', 'Laranjal', 'Laranjeiras Do Sul', 'Mallet', 'Marquinho', 'Mato Rico', 'Nova Laranjeiras',
    'Nova Tebas', 'Ortigueira', 'Palmeira', 'Palmital', 'Paula Freitas', 'Paulo Frontin', 'Pinhão',
    'Piraí Do Sul', 'Pitanga', 'Ponta Grossa', 'Porto Amazonas', 'Porto Barreiro', 'Porto União – SC',
    'Porto Vitória', 'Prudentópolis', 'Rebouças', 'Reserva', 'Reserva Do Iguaçu', 'Rio Azul',
    'Rio Bonito Do Iguaçu', 'Santa Maria Do Oeste', 'São João Do Triunfo', 'São Mateus Do Sul',
    'Teixeira Soares', 'Telêmaco Borba', 'Tibagi', 'Turvo', 'União Da Vitória', 'Ventania', 'Virmond',
)

ddd45 = (
    'Anahy', 'Boa Vista Da Aparecida', 'Braganey', 'Cafelândia', 'Campo Bonito', 'Capitão Leônidas Marques', 'Cascavel',
    'Catanduvas', 'Céu Azul', 'Corbélia', 'Diamante Do Sul', 'Diamante D’oeste', 'Entre Rios Do Oeste',
    'Foz Do Iguaçu', 'Guaraniaçu', 'Ibema', 'Iguatu', 'Itaipulândia', 'Lindoeste', 'Marechal Cândido Rondon',
    'Matelândia', 'Medianeira', 'Mercedes', 'Missal', 'Nova Aurora', 'Nova Santa Rosa', 'Ouro Verde Do Oeste',
    'Pato Bragado', 'Quatro Pontes', 'Ramilândia', 'Santa Helena', 'Santa Lúcia', 'Santa Tereza Do Oeste',
    'Santa Terezinha De Itaipu', 'São José Das Palmeiras', 'São Miguel Do Iguaçu', 'São Pedro Do Iguaçu',
    'Serranópolis Do Iguaçu', 'Toledo', 'Três Barras Do Paraná', 'Vera Cruz Do Oeste',
)

ddd46 = (
    'Ampére', 'Barracão', 'Bela Vista Da Caroba', 'Boa Esperança Do Iguaçu', 'Bom Jesus Do Sul',
    'Bom Sucesso Do Sul', 'Capanema', 'Chopinzinho', 'Clevelândia', 'Coronel Domingos Soares', 'Coronel Vivida',
    'Cruzeiro Do Iguaçu', 'Dois Vizinhos', 'Enéas Marques', 'Espigão Alto Do Iguaçu', 'Flor Da Serra Do Sul',
    'Francisco Beltrão', 'Honório Serpa', 'Itapejara D’oeste', 'Manfrinópolis', 'Mangueirinha', 'Mariópolis',
    'Marmeleiro', 'Nova Esperança Do Sudoeste', 'Nova Prata Do Iguaçu', 'Palmas', 'Pato Branco', 'Pérola D`oeste',
    'Pinhal De São Bento', 'Planalto', 'Pranchita', 'Quedas Do Iguaçu', 'Realeza', 'Renascença', 'Salgado Filho',
    'Salto Do Lontra', 'Santa Izabel Do Oeste', 'Santo Antônio Do Sudoeste', 'São João', 'São Jorge D`oeste',
    'Saudade Do Iguaçu', 'Sulina', 'Verê', 'Vitorino',
)

ddd91 = (
    'Abaetetuba', 'Acará', 'Acará', 'Anajás', 'Ananindeua', 'Anapu', 'Augusto Corrêa', 'Aurora Do Pará',
    'Bagre', 'Baião', 'Barcarena', 'Belém', 'Benevides', 'Bonito', 'Bragança', 'Breves', 'Bujaru',
    'Cachoeira Do Arari', 'Cachoeira Do Piriá', 'Cametá', 'Capanema', 'Capitão Poço', 'Castanhal',
    'Chaves', 'Colares', 'Concórdia Do Pará', 'Curralinho', 'Curuçá', 'Garrafão Do Norte',
    'Gurupá', 'Igarapé-Açu', 'Igarapé-Miri', 'Inhangapi', 'Ipixuna Do Pará', 'Irituia',
    'Limoeiro Do Ajuru', 'Mãe Do Rio', 'Magalhães Barata', 'Maracanã', 'Marapanim',
    'Marituba', 'Melgaço', 'Mocajuba', 'Moju', 'Muaná', 'Nova Esperança Do Piriá',
    'Nova Timboteua', 'Oeiras Do Pará', 'Ourém', 'Pacajá', 'Paragominas', 'Peixe-Boi',
    'Ponta De Pedras', 'Portel', 'Primavera', 'Quatipuru', 'Salinópolis', 'Salvaterra',
    'Santa Bárbara Do Pará', 'Santa Cruz Do Arari', 'Santa Isabel Do Pará',
    'Santa Luzia Do Pará', 'Santa Maria Do Pará', 'Santarém Novo', 'Santo Antônio Do Tauá',
    'São Caetano De Odivelas', 'São Domingos Do Capim', 'São Francisco Do Pará',
    'São João Da Ponta', 'São João De Pirabas', 'São Miguel Do Guamá',
    'São Sebastião Da Boa Vista', 'Senador José Porfírio', 'Soure', 'Tailândia',
    'Terra Alta', 'Tomé-Açu', 'Tracuateua', 'Ulianópolis', 'Vigia', 'Viseu',
)

ddd93 = (
    'Alenquer', 'Almeirim', 'Altamira', 'Aveiro', 'Belterra', 'Brasil Novo', 'Curuá', 'Faro', 'Itaituba',
    'Jacareacanga', 'Juruti', 'Medicilândia', 'Mojuí Dos Campos', 'Monte Alegre', 'Novo Progresso', 'Óbidos',
    'Oriximiná', 'Placas', 'Porto De Moz', 'Prainha', 'Rurópolis', 'Santarém', 'Terra Santa', 'Trairão',
    'Uruará', 'Vitória Do Xingu'
)

ddd94 = (
    'Abel Figueiredo', 'Água Azul Do Norte', 'Bannach', 'Bom Jesus Do Tocantins', 'Brejo Grande Do Araguaia',
    'Brejo Grande Do Araguaia', 'Breu Branco', 'Canaã Dos Carajás', 'Conceição Do Araguaia', 'Cumaru Do Norte',
    'Curionópolis', 'Dom Eliseu', 'Eldorado Dos Carajás', 'Floresta Do Araguaia', 'Goianésia Do Pará',
    'Itupiranga', 'Jacundá', 'Marabá', 'Nova Ipixuna', 'Novo Repartimento', 'Ourilândia Do Norte',
    'Palestina Do Pará', 'Parauapebas', 'Pau D`arco', 'Piçarra', 'Redenção', 'Rio Maria', 'Rondon Do Pará',
    'Santa Maria Das Barreiras', 'Santana Do Araguaia', 'São Domingos Do Araguaia', 'São Félix Do Xingu',
    'São Geraldo Do Araguaia', 'São João Do Araguaia', 'Sapucaia', 'Tucumã', 'Tucuruí', 'Xinguara',
)

# cities identified by area code

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
def ExDDD88():
    for i in range(len(ddd88)):
        print(ddd88[i])
        time.sleep(0.01)
def ExDDD27():
    for i in range(len(ddd27)):
        print(ddd27[i])
        time.sleep(0.01)
def ExDDD28():
    for i in range(len(ddd28)):
        print(ddd28[i])
        time.sleep(0.01)
def ExDDD61():
    for i in range(len(ddd61)):
        print(ddd61[i])
        time.sleep(0.01)
def ExDDD62():
    for i in range(len(ddd62)):
        print(ddd62[i])
        time.sleep(0.01)
def ExDDD64():
    for i in range(len(ddd64)):
        print(ddd64[i])
        time.sleep(0.01)
def ExDDD98():
    for i in range(len(ddd98)):
        print(ddd98[i])
        time.sleep(0.01)
def ExDDD99():
    for i in range(len(ddd99)):
        print(ddd99[i])
        time.sleep(0.01)
def ExDDD65():
    for i in range(len(ddd65)):
        print(ddd65[i])
        time.sleep(0.01)
def ExDDD66():
    for i in range(len(ddd66)):
        print(ddd66[i])
        time.sleep(0.01)
def ExDDD31():
    for i in range(len(ddd31)):
        print(ddd31[i])
        time.sleep(0.01)
def ExDDD32():
    for i in range(len(ddd32)):
        print(ddd32[i])
        time.sleep(0.01)
def ExDDD33():
    for i in range(len(ddd33)):
        print(ddd33[i])
        time.sleep(0.01)
def ExDDD34():
    for i in range(len(ddd34)):
        print(ddd34[i])
        time.sleep(0.01)
def ExDDD35():
    for i in range(len(ddd35)):
        print(ddd35[i])
        time.sleep(0.01)
def ExDDD37():
    for i in range(len(ddd37)):
        print(ddd37[i])
        time.sleep(0.01)
def ExDDD41():
    for i in range(len(ddd41)):
        print(ddd41[i])
        time.sleep(0.01)
def ExDDD42():
    for i in range(len(ddd42)):
        print(ddd42[i])
        time.sleep(0.01)
def ExDDD45():
    for i in range(len(ddd45)):
        print(ddd45[i])
        time.sleep(0.01)
def ExDDD46():
    for i in range(len(ddd46)):
        print(ddd46[i])
        time.sleep(0.01)
def ExDDD91():
    for i in range(len(ddd91)):
        print(ddd91[i])
        time.sleep(0.01)
def ExDDD93():
    for i in range(len(ddd93)):
        print(ddd93[i])
        time.sleep(0.01)
def ExDDD94():
    for i in range(len(ddd94)):
        print(ddd94[i])
        time.sleep(0.01)