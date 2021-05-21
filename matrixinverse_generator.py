tamanho = 97

f = open("Output_gerador.py", "w")
# i serve para o número de checagens de pivo -> tamanho-1
for i in range(tamanho-1):
    f.write("def check_pivo_linha{i}(): \n".format(i=i)) 
    f.write("    if ((linha{i}[{i}] == 0)):\n".format(i=i))
    f.write("        aux   = [0,0,0]\n")## otimizar isso aqui
    f.write("        auxid = [0,0,0]\n")   
    flag1 = 0
    flag2 = 0
    # para percorrer o as linhas da matriz, zerando em cima e embaixo do pivo.
    for j in range(tamanho):
        
        if(j<=i):         
            continue
        else:
                        
            if(flag1 == 0):# esse if é para escrever o elseif depois da primeira iteração em cima do j
                flag1 = 1
                f.write("        if(linha{j}[{i}] != 0):\n".format(j=j, i=i))
                f.write("            i = 0\n")
                f.write("            while (i < size):\n")
                f.write("                aux[i] = linha{i}[i]\n".format(i=i)) 
                f.write("                auxid[i] = id{i}[i]\n".format(i=i)) 
                f.write("                linha{i}[i] = linha{j}[i]\n".format(i=i, j=j))
                f.write("                id{i}[i] = id{j}[i]\n".format(i=i, j=j))
                f.write("                linha{j}[i] = aux[i]\n".format(i=i, j=j))
                f.write("                id{j}[i] = auxid[i]\n".format(i=i, j=j))
                f.write("                i += 1\n")
             
            else:
                f.write("        elif(linha{j}[{i}] != 0):\n".format(j=j, i=i))   
                f.write("            i = 0\n")
                f.write("            while (i < size):\n")
                f.write("                aux[i] = linha{i}[i]\n".format(i=i))
                f.write("                auxid[i] = id{i}[i]\n".format(i=i))
                f.write("                linha{i}[i] = linha{j}[i]\n".format(i=i, j=j))
                f.write("                id{i}[i] = id{j}[i]\n".format(i=i, j=j))
                f.write("                linha{j}[i] = aux[i]\n".format(i=i, j=j))
                f.write("                id{j}[i] = auxid[i]\n".format(i=i, j=j))
                f.write("                i += 1\n") 

f.write("def inverte():\n")
for i in range(tamanho):
    f.write("###########################  pivo linha{i} #############################\n".format(i=i))
    if( i != tamanho-1):
        f.write("    check_pivo_linha{i}()\n".format(i=i))
    f.write("    pivo = linha{i}[{i}]\n".format(i=i))
    f.write("    i=0\n")
    f.write("    while(i < size):\n")
    f.write("        linha{i}[i] = linha{i}[i]/pivo\n".format(i=i))
    f.write("        id{i}[i] = id{i}[i]/pivo\n".format(i=i))
    f.write("        i += 1\n")
    for j in range(tamanho):
        if(j == i):
            continue
        else:
            f.write("    i=0\n")
            f.write("    cofator = linha{j}[{i}]\n".format(j=j, i=i))
            f.write("    while(i<size):\n")
            f.write("        linha{j}[i] = linha{j}[i] - cofator*linha{i}[i]\n".format(j=j, i=i))
            f.write("        id{j}[i] = id{j}[i] - cofator*id{i}[i]\n".format(j=j, i=i))
            f.write("        i += 1\n") 
        

