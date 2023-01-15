import csv 



def rank(lista, escabilidade):
    ordem =[]
    dic ={
        "s":[],
        "a":[],
        "b":[],
        "c":[],
        "d":[],
        "e":[]
    }
    for i in lista:
        aux={}
        escala = i[len(i)-4]
        escala =escala.replace("[","");escala =escala.replace("]","")
        escala =escala.replace("{","");escala =escala.replace("}","")
        escala =escala.replace("'","")
        escala = escala.split(", ") 
        for j in escala:
            j = j.split(": ")
            
            if len(aux)<2:
                aux[j[0]]=j[1]
            else:
                
                aux={}
                aux[j[0]]=j[1]
        print(aux)
        ordem.append(aux)

         
    return ordem

def triagem_das_armas(qualidades):
    lista=[]
    tipo= qualidades[0]
    peso=qualidades[1]
    multiplicador=qualidades[2]

    with open("armas/"+tipo+".csv", "r") as arquivo:
        armas = csv.reader(arquivo)
        for arma in armas:
             if float(arma[len(arma)-1])<= peso:
                lista.append(arma)
    rank(lista, multiplicador)

    return lista

def main ():
    peso_maximo = 4 #input("digite o peso maximo da arma: ") 
    tipo_de_arma ="Bow" #input("digite o tipo de arma que vc quer: ")
    mult_da_arma ="1" #input("digite o multiplicador da arma :")
    qualidades=[tipo_de_arma,peso_maximo,mult_da_arma]
    triagem_das_armas(qualidades)
     
    return 0

main()