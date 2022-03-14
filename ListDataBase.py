import time

estados = [
    "acre","alagoas","amapa","amazonas","bahia","ceara","espirito santo","goias","maranhão"
    "mato grosso","mato grosso do sul","minas gerais","para","paraiba","piaui","rio de janeiro",
    "rio grande do norte", "rio grande do sul", "roraima", "santa catarina", "sao paulo", "sergipe", 
    "tocantins"
]


ddd = [
    68, 82, 96, 92, 97, 71, 73, 74, 75, 77, 85, 88, 27, 28, 61, 62, 64, 98, 99, 65, 66,
    67, 31, 32, 33, 34, 35, 37, 91, 93, 94, 83, 41, 42, 43, 44, 45, 46, 86, 89, 21, 22,
    24, 84, 52, 53, 54, 55, 95, 47, 48, 49, 11, 12, 13, 14, 15, 16, 17, 18, 19, 79, 63
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

# States

def AM():
    for i in range(len(Amazonas)):
        print("DDD ",Amazonas[i])
        time.sleep(0.01)
def BA():
    for i in range(len(Bahia)):
        print("DDD ",Bahia[i])
        time.sleep(0.01)
def CE():
    for i in range(len(Ceara)):
        print("DDD ",Ceara[i])
        time.sleep(0.01)
def ES():
    for i in range(len(Espirito_Santo)):
        print("DDD ",Espirito_Santo[i])
        time.sleep(0.01)
def GO():
    for i in range(len(Goias)):
        print("DDD ",Goias[i])
        time.sleep(0.01)
def MA():
    for i in range(len(Maranhao)):
        print("DDD ",Maranhao[i])
        time.sleep(0.01)
def MT():
    for i in range(len(Mato_Grosso)):
        print("DDD ",Mato_Grosso[i])
        time.sleep(0.01)
def MG():
    for i in range(len(Minas_Gerais)):
        print("DDD ",Minas_Gerais[i])
        time.sleep(0.01)
def PA():
    for i in range(len(Para)):
        print("DDD ",Para[i])
        time.sleep(0.01)
def PN():
    for i in range(len(Parana)):
        print("DDD ",Parana[i])
        time.sleep(0.01)
def PI():
    for i in range(len(Piaui)):
        print("DDD ",Piaui[i])
        time.sleep(0.01)
def RJ():
    for i in range(len(Rio_de_Janeiro)):
        print("DDD ",Rio_de_Janeiro[i])
        time.sleep(0.01)
def RS():
    for i in range(len(Rio_Grande_do_Sul)):
        print("DDD ",Rio_Grande_do_Sul[i])
        time.sleep(0.01)
def SC():
    for i in range(len(Santa_Catarina)):
        print("DDD ",Santa_Catarina[i])
        time.sleep(0.01)
def SP():
    for i in range(len(Sao_Paulo)):
        print("DDD ",Sao_Paulo[i])
        time.sleep(0.01)

# States and DDD
def StatesList():
    for i in range(len(estados)):
        print(estados[i])
        time.sleep(0.01)
def DDDList():
    for i in range(len(ddd)):
        print(ddd[i])
        time.sleep(0.01)