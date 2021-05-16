size = 2
def check_pivo(linha0, linha1, id0, id1, size):
    # se o pivo da linha0 for 0, trocar com a linha1 se a linha 1 for dif  de 0
    if ((linha0[0] == 0)):
        if(linha1[0] != 0):
            aux = [0,0]
            auxid = [0,0]
            i = 0
            while (i < size): #loop pra passar a linha
                aux[i] = linha0[i]
                linha0[i] = linha1[i]
                linha1[i] = aux[i]
            
                auxid[i] = id0[i]
                id0[i] = id1[i]
                id1[i] =auxid[i]
                i += 1  
            print(a0)
            print(a1)      

a0 = [0,2]
a1 = [1,0]
ida0 = [1, 0]
ida1 = [0, 1]    

check_pivo(a0, a1, ida0, ida1, size)

def inverte(linha0, linha1, id0, id1, size):
    #pivo linha 0
    pivo = linha0[0]
    i = 0
    while (i<size):
        linha0[i] = linha0[i]/pivo
        id0[i] = id0[i]/pivo
        i += 1
    #zerando a linha1
    i = 0
    cofator = linha1[0]
    while(i<size):              
        linha1[i] = linha1[i] - cofator*linha0[i]
        id1[i] = id1[i] - cofator*id0[i]
        i += 1

    # segundo pivo
    pivo = linha1[1]
    i = 0
    while (i<size):
        linha1[i] = linha1[i]/pivo    
        id1[i] = id1[i]/pivo
        i +=1     
    #zerando a linha 1
    i = 0
    cofator = linha0[1]
    while(i<size):      
        linha0[i] = linha0[i] - cofator*linha1[i]
        id0[i] = id0[i] - cofator*id1[i]
        i +=1
    
    print(linha0, id0)
    print(linha1,id1)

        

    #print(linha0, id0, '\n', linha1, id1)    

    

        

inverte(a0, a1, ida0, ida1, size)        
    
            
            
            
        
        
        
    
    
        
        
        
    
    
    
    