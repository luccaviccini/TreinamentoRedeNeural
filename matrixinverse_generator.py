tamanho = 3

f = open("Output_gerador.py", "w")
# i serve para o número de checagens de pivo -> tamanho-1
for i in range(tamanho-1):
    f.write("def check_pivo_linha{i}(): \n".format(i=i)) 
    f.write("   if ((linha{i}[{i}] == 0)):\n".format(i=i))
    f.write("       aux   = [0,0,0]\n")
    f.write("       auxid = [0,0,0]\n")   
    flag = 0
    # para percorrer o as linhas da matriz, zerando em cima e embaixo do pivo.
    for j in range(tamanho):
        
        if(j<=i):         
            continue
        else:            
            if(flag == 0):
                flag = 1
                f.write("       if(linha{j}[{i}] != 0):\n".format(j=j, i=i))
                f.write("           i = 0\n")
                f.write("           while (i < size):\n")
                f.write("               aux[i] = linha{i}[i]\n".format(i=i)) 
                f.write("               auxid[i] = id{i}[i]\n".format(i=i)) 
                """ for k in range(tamanho):
                    if(k == i):
                        continue
                    else:
                        f.write("               linha{i}[i] = linha{k}[i]\n".format(i=i, k=k))
                        f.write("               id{i}[i] = id{k}[i]\n".format(i=i, k=k)) """
               
            else:
                f.write("       elif(linha{j}[{i}] != 0):\n".format(j=j, i=i))   
                f.write("           i = 0\n")
                f.write("           while (i < size):\n")
                f.write("               aux[i] = linha{i}[i]\n".format(i=i))
                f.write("               auxid[i] = id{i}[i]\n".format(i=i))
                """ for k in range(tamanho):
                    if(k == i):
                        continue
                    else:
                        f.write("               linha{i}[i] = linha{k}[i]\n".format(i=i, k=k))
                        f.write("               id{i}[i] = id{k}[i]\n".format(i=i, k=k)) """
    #checagem dos pivos


            
 
            