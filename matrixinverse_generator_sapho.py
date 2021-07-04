import random
tamanho = 3
f = open("Output_gerador_sapho.c", "w")


f.write("void inverte() {\n")
for i in range(tamanho):
    if (i == 0):
        for count in range(tamanho):
            f.write("float id{count}[97]; ".format(count = count))
        f.write("\n") 
        for sm in range(tamanho):   
            for index in range(tamanho):
                if sm == index:
                    if(index == 2):
                        f.write("id{sm}[{index}] = 1.0;\n".format(sm = sm, index = index))
                    else:
                        f.write("id{sm}[{index}] = 1.0;".format(sm = sm, index = index))
                            

                else:
                    if(index == 2): 
                        f.write("id{sm}[{index}] = 0.0;\n ".format(sm = sm, index = index))
                    else:
                        f.write("id{sm}[{index}] = 0.0;".format(sm = sm, index = index))


        f.write("\n")
        f.write("int i; ")

        f.write("size = {tamanho};\n".format(tamanho = tamanho)) 
        f.write("float aux[97];  float auxid[97];\n")
    for h in range(tamanho):
        f.write("aux[{tamanho}] = 0; ".format(tamanho = h))
    f.write("\n")
    for h in range(tamanho):    
        f.write("auxid[{tamanho}] = 0; ".format(tamanho = h))
        # para escrever o vetor auxiliar da id


        
        

    f.write("\n/////////////////////////  pivo soma_{i} /////////////////////////\n".format(i=i))
    if( i != tamanho-1):
        f.write("/////////////////////////  CHECAGEM {i} /////////////////////////\n".format(i=i))
        f.write("    if ((soma_{i}[{i}] == 0)) {cb}\n".format(i=i, cb = '{'))
        flag = 0
        for j in range(tamanho):
            if(j <= i):
                continue
            else:
                if(flag == 0):
                    flag = 1

                    if((j != tamanho-1) and (i != tamanho -2)):
                        f.write("        if(soma_{j}[{i}] != 0) {cb}\n".format(j=j, i=i, cb = '{'))
                        f.write("            i = 0;\n")
                        f.write("            while (i < size) {\n")
                        f.write("                aux[i] = soma_{i}[i];\n".format(i=i)) 
                        f.write("                auxid[i] = id{i}[i];\n".format(i=i)) 
                        f.write("                soma_{i}[i] = soma_{j}[i];\n".format(i=i, j=j))
                        f.write("                id{i}[i] = id{j}[i];\n".format(i=i, j=j))
                        f.write("                soma_{j}[i] = aux[i];\n".format(i=i, j=j))
                        f.write("                id{j}[i] = auxid[i];\n".format(i=i, j=j))
                        f.write("                i = i + 1;} }\n")
                    else:
                        f.write("        if(soma_{j}[{i}] != 0) {cb}\n".format(j=j, i=i, cb = '{'))
                        f.write("            i = 0;\n")
                        f.write("            while (i < size) {\n")
                        f.write("                aux[i] = soma_{i}[i];\n".format(i=i)) 
                        f.write("                auxid[i] = id{i}[i];\n".format(i=i)) 
                        f.write("                soma_{i}[i] = soma_{j}[i];\n".format(i=i, j=j))
                        f.write("                id{i}[i] = id{j}[i];\n".format(i=i, j=j))
                        f.write("                soma_{j}[i] = aux[i];\n".format(i=i, j=j))
                        f.write("                id{j}[i] = auxid[i];\n".format(i=i, j=j))
                        f.write("                i = i + 1;} } }\n")

                else:
                    f.write("        else if(soma_{j}[{i}] != 0) {cb}\n".format(j=j, i=i, cb = '{'))   
                    f.write("            i = 0;\n")
                    f.write("            while (i < size) {\n")
                    f.write("                aux[i] = soma_{i}[i];\n".format(i=i))
                    f.write("                auxid[i] = id{i}[i];\n".format(i=i))
                    f.write("                soma_{i}[i] = soma_{j}[i];\n".format(i=i, j=j))
                    f.write("                id{i}[i] = id{j}[i];\n".format(i=i, j=j))
                    f.write("                soma_{j}[i] = aux[i];\n".format(i=i, j=j))
                    f.write("                id{j}[i] = auxid[i];\n".format(i=i, j=j))
                    f.write("                i = i + 1; } } } \n") 

        f.write("///////////////////////////  FIM CHECAGEM PIVO{i} ////////////////////////////\n".format(i=i))

    f.write("    pivo = soma_{i}[{i}];\n".format(i=i))
    f.write("    i=0;\n")
    f.write("    while(i < size){\n")
    f.write("        soma_{i}[i] = soma_{i}[i]/pivo;\n".format(i=i))
    f.write("        id{i}[i] = id{i}[i]/pivo;\n".format(i=i))
    f.write("        i = i + 1;}\n")
    for j in range(tamanho):
        if(j == i):
            continue
        else:
            f.write("    i=0;\n")
            f.write("    cofator = soma_{j}[{i}];\n".format(j=j, i=i))
            f.write("    while (i<size) {\n")
            f.write("        soma_{j}[i] = soma_{j}[i] - cofator*soma_{i}[i];\n".format(j=j, i=i))
            f.write("        id{j}[i] = id{j}[i] - cofator*id{i}[i];\n".format(j=j, i=i))
            f.write("        i = i + 1; }\n") 

f.write("\n\ninverte();")          