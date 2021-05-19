tamanho = 3

f = open("Codigo_10x10.py", "w")
f.write("def inverte(): \n")
for i in range(tamanho):   
    f.write("   ###########################         pivolinha{i}      #############################\n".format(i=i))
    #checagem dos pivos
    for j in range(tamanho):        
        if (j<=i):
            f.write("   if((linha{j}[{i}] == 0)):\n". format(i=i, j=j))
            linha0 = 0
            f.write("       aux   = [0,0,0]\n       auxid = [0,0,0]\n") ## pensar num jeito de otimizar isso aqui
        

                                
            continue
        else:
            f.write("       if((linha{j}[{i}] != 0)):\n".format(i=i, j=j))
            f.write("           i = 0\n")
            f.write("           while (i < tamanho):\n")           
              
            f.write("               aux[i] = linha{linha0}[i]\n".format(linha0=linha0))
            f.write("               linha{linha0}[i] = linha{j}[i]\n".format(linha0 =linha0, j=j))
            f.write("               linha{j}[i] = linha{j}[i]\n".format(linha0 =linha0, j=j))
            

            