import csv 
import os
lista=[]
tipos=[]
def armas_por_tipo(listas_de_tipos, lista_do_csv):
    os.mkdir("armas")
    for tipo in listas_de_tipos:
        with open("armas/"+tipo+".csv","w") as armas:
            arquivo = csv.writer(armas)
            for i in lista_do_csv:
                if i[len(i)-2] ==tipo:
                    arquivo.writerow(i)
    return 0


with open("/home/emanuel/Área de Trabalho/elden-ring-data/weapons.csv") as arquivo:
    csv_a_ser_limpado = csv.reader(arquivo)
    for linha in csv_a_ser_limpado:
        del linha[0], linha[2], linha[1]
        lista.append(linha)


with open("novo_arquivo.csv","w") as novo_arquivo:
    n=csv.writer(novo_arquivo)
    for i in lista:
        n.writerow(i)
        if i[len(i)-1] not in tipos:
            tipos.append(i[len(i)-2])
tipos=list(dict.fromkeys(tipos))
del tipos[0]

armas_por_tipo(tipos, lista)
    