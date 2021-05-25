size = 5
aux   = [0,0,0,0,0]
auxid = [0,0,0,0,0]

linha0 = [0.18339294949329765,0.4104201562523273,0.9454417551120844,0.6016867835049312,0.21891206422382126]
linha1 = [0.6237964087456463,0.6369668909923013,0.3750047965656109,0.5626680520679972,0.9212366591425314]
linha2 = [0.5731378961861637,0.7577995382218699,0.4474042356951634,0.7334030065397699,0.9325341319456338]
linha3 = [0.20962506864998853,0.8714846044222877,0.30841029170726086,0.2021989888496174,0.004802974527161719]
linha4 = [0.7855354834686538,0.3078197725578612,0.05560069478267127,0.8962942996568719,0.509378481009926]
id0 = [1,0,0,0,0]
id1 = [0,1,0,0,0]
id2 = [0,0,1,0,0]
id3 = [0,0,0,1,0]
id4 = [0,0,0,0,1]

def inverte():
###########################  pivo linha0 #############################
###########################  CHECAGEM 0 #############################
    if ((linha0[0] == 0)):
        if(linha1[0] != 0):
            i = 0
            while (i < size):
                aux[i] = linha0[i]
                auxid[i] = id0[i]
                linha0[i] = linha1[i]
                id0[i] = id1[i]
                linha1[i] = aux[i]
                id1[i] = auxid[i]
                i += 1
        elif(linha2[0] != 0):
            i = 0
            while (i < size):
                aux[i] = linha0[i]
                auxid[i] = id0[i]
                linha0[i] = linha2[i]
                id0[i] = id2[i]
                linha2[i] = aux[i]
                id2[i] = auxid[i]
                i += 1
        elif(linha3[0] != 0):
            i = 0
            while (i < size):
                aux[i] = linha0[i]
                auxid[i] = id0[i]
                linha0[i] = linha3[i]
                id0[i] = id3[i]
                linha3[i] = aux[i]
                id3[i] = auxid[i]
                i += 1
        elif(linha4[0] != 0):
            i = 0
            while (i < size):
                aux[i] = linha0[i]
                auxid[i] = id0[i]
                linha0[i] = linha4[i]
                id0[i] = id4[i]
                linha4[i] = aux[i]
                id4[i] = auxid[i]
                i += 1
###########################  FIM CHECAGEM PIVO0 #############################
    pivo = linha0[0]
    i=0
    while(i < size):
        linha0[i] = linha0[i]/pivo
        id0[i] = id0[i]/pivo
        i += 1
    i=0
    cofator = linha1[0]
    while(i<size):
        linha1[i] = linha1[i] - cofator*linha0[i]
        id1[i] = id1[i] - cofator*id0[i]
        i += 1
    i=0
    cofator = linha2[0]
    while(i<size):
        linha2[i] = linha2[i] - cofator*linha0[i]
        id2[i] = id2[i] - cofator*id0[i]
        i += 1
    i=0
    cofator = linha3[0]
    while(i<size):
        linha3[i] = linha3[i] - cofator*linha0[i]
        id3[i] = id3[i] - cofator*id0[i]
        i += 1
    i=0
    cofator = linha4[0]
    while(i<size):
        linha4[i] = linha4[i] - cofator*linha0[i]
        id4[i] = id4[i] - cofator*id0[i]
        i += 1
###########################  pivo linha1 #############################
###########################  CHECAGEM 1 #############################
    if ((linha1[1] == 0)):
        if(linha2[1] != 0):
            i = 0
            while (i < size):
                aux[i] = linha1[i]
                auxid[i] = id1[i]
                linha1[i] = linha2[i]
                id1[i] = id2[i]
                linha2[i] = aux[i]
                id2[i] = auxid[i]
                i += 1
        elif(linha3[1] != 0):
            i = 0
            while (i < size):
                aux[i] = linha1[i]
                auxid[i] = id1[i]
                linha1[i] = linha3[i]
                id1[i] = id3[i]
                linha3[i] = aux[i]
                id3[i] = auxid[i]
                i += 1
        elif(linha4[1] != 0):
            i = 0
            while (i < size):
                aux[i] = linha1[i]
                auxid[i] = id1[i]
                linha1[i] = linha4[i]
                id1[i] = id4[i]
                linha4[i] = aux[i]
                id4[i] = auxid[i]
                i += 1
###########################  FIM CHECAGEM PIVO1 #############################
    pivo = linha1[1]
    i=0
    while(i < size):
        linha1[i] = linha1[i]/pivo
        id1[i] = id1[i]/pivo
        i += 1
    i=0
    cofator = linha0[1]
    while(i<size):
        linha0[i] = linha0[i] - cofator*linha1[i]
        id0[i] = id0[i] - cofator*id1[i]
        i += 1
    i=0
    cofator = linha2[1]
    while(i<size):
        linha2[i] = linha2[i] - cofator*linha1[i]
        id2[i] = id2[i] - cofator*id1[i]
        i += 1
    i=0
    cofator = linha3[1]
    while(i<size):
        linha3[i] = linha3[i] - cofator*linha1[i]
        id3[i] = id3[i] - cofator*id1[i]
        i += 1
    i=0
    cofator = linha4[1]
    while(i<size):
        linha4[i] = linha4[i] - cofator*linha1[i]
        id4[i] = id4[i] - cofator*id1[i]
        i += 1
###########################  pivo linha2 #############################
###########################  CHECAGEM 2 #############################
    if ((linha2[2] == 0)):
        if(linha3[2] != 0):
            i = 0
            while (i < size):
                aux[i] = linha2[i]
                auxid[i] = id2[i]
                linha2[i] = linha3[i]
                id2[i] = id3[i]
                linha3[i] = aux[i]
                id3[i] = auxid[i]
                i += 1
        elif(linha4[2] != 0):
            i = 0
            while (i < size):
                aux[i] = linha2[i]
                auxid[i] = id2[i]
                linha2[i] = linha4[i]
                id2[i] = id4[i]
                linha4[i] = aux[i]
                id4[i] = auxid[i]
                i += 1
###########################  FIM CHECAGEM PIVO2 #############################
    pivo = linha2[2]
    i=0
    while(i < size):
        linha2[i] = linha2[i]/pivo
        id2[i] = id2[i]/pivo
        i += 1
    i=0
    cofator = linha0[2]
    while(i<size):
        linha0[i] = linha0[i] - cofator*linha2[i]
        id0[i] = id0[i] - cofator*id2[i]
        i += 1
    i=0
    cofator = linha1[2]
    while(i<size):
        linha1[i] = linha1[i] - cofator*linha2[i]
        id1[i] = id1[i] - cofator*id2[i]
        i += 1
    i=0
    cofator = linha3[2]
    while(i<size):
        linha3[i] = linha3[i] - cofator*linha2[i]
        id3[i] = id3[i] - cofator*id2[i]
        i += 1
    i=0
    cofator = linha4[2]
    while(i<size):
        linha4[i] = linha4[i] - cofator*linha2[i]
        id4[i] = id4[i] - cofator*id2[i]
        i += 1
###########################  pivo linha3 #############################
###########################  CHECAGEM 3 #############################
    if ((linha3[3] == 0)):
        if(linha4[3] != 0):
            i = 0
            while (i < size):
                aux[i] = linha3[i]
                auxid[i] = id3[i]
                linha3[i] = linha4[i]
                id3[i] = id4[i]
                linha4[i] = aux[i]
                id4[i] = auxid[i]
                i += 1
###########################  FIM CHECAGEM PIVO3 #############################
    pivo = linha3[3]
    i=0
    while(i < size):
        linha3[i] = linha3[i]/pivo
        id3[i] = id3[i]/pivo
        i += 1
    i=0
    cofator = linha0[3]
    while(i<size):
        linha0[i] = linha0[i] - cofator*linha3[i]
        id0[i] = id0[i] - cofator*id3[i]
        i += 1
    i=0
    cofator = linha1[3]
    while(i<size):
        linha1[i] = linha1[i] - cofator*linha3[i]
        id1[i] = id1[i] - cofator*id3[i]
        i += 1
    i=0
    cofator = linha2[3]
    while(i<size):
        linha2[i] = linha2[i] - cofator*linha3[i]
        id2[i] = id2[i] - cofator*id3[i]
        i += 1
    i=0
    cofator = linha4[3]
    while(i<size):
        linha4[i] = linha4[i] - cofator*linha3[i]
        id4[i] = id4[i] - cofator*id3[i]
        i += 1
###########################  pivo linha4 #############################
    pivo = linha4[4]
    i=0
    while(i < size):
        linha4[i] = linha4[i]/pivo
        id4[i] = id4[i]/pivo
        i += 1
    i=0
    cofator = linha0[4]
    while(i<size):
        linha0[i] = linha0[i] - cofator*linha4[i]
        id0[i] = id0[i] - cofator*id4[i]
        i += 1
    i=0
    cofator = linha1[4]
    while(i<size):
        linha1[i] = linha1[i] - cofator*linha4[i]
        id1[i] = id1[i] - cofator*id4[i]
        i += 1
    i=0
    cofator = linha2[4]
    while(i<size):
        linha2[i] = linha2[i] - cofator*linha4[i]
        id2[i] = id2[i] - cofator*id4[i]
        i += 1
    i=0
    cofator = linha3[4]
    while(i<size):
        linha3[i] = linha3[i] - cofator*linha4[i]
        id3[i] = id3[i] - cofator*id4[i]
        i += 1


    print(linha0, id0)
    print(linha1, id1)
    print(linha2, id2)
    print(linha3, id3)
    print(linha4, id4)


inverte()