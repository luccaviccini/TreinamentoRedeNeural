aux = [0,0,0]
auxid = [0,0,0]
def check_pivo_linha0():
    aux = [0,0,0]
    auxid = [0,0,0]
    id0 = [1, 0, 0]
    id1 = [0, 1, 0]    
    id2 = [0, 0, 1]
    size = 3
    # se o pivo da linha0 for 0, trocar com a linha1 se a linha 1 for dif  de 0
    if ((linha0[0] == 0)):
        #aux = [0,0,0]
        #auxid = [0,0,0]
        # se o pivo da linha1 nao for 0
        if(linha1[0] != 0):          
            i = 0
            while (i < size): #loop pra passar a linha
                aux[i] = linha0[i]
                auxid[i] = id0[i]

                linha0[i] = linha1[i]
                id0[i] = id1[i]

                linha1[i] = aux[i]    
                id1[i] =auxid[i]
                i += 1  
        #se a linha1 for zero substituir pela 2       
        elif(linha2[0] != 0):
            i=0
            while (i < size): #loop pra passar a linha
                aux[i] = linha0[i]
                auxid[i] = id0[i]

                linha0[i] = linha2[i]
                id0[i] = id2[i]

                linha2[i] = aux[i]                       
                id2[i] =auxid[i]
                i += 1 

def check_pivo_linha1():
    # se o pivo da linha1 for 0, trocar com a linha2 
    if ((linha1[1] == 0)):
        #aux = [0,0,0]
        #auxid = [0,0,0]
        
       #se o pivo da linha1 for zero substituir pela 2       
        if(linha2[1] != 0):
            i=0
            while (i < size): #loop pra passar a linha
                aux[i] = linha1[i]
                linha1[i] = linha2[i]
                linha2[i] = aux[i]
            
                auxid[i] = id1[i]
                id1[i] = id2[i]
                id2[i] =auxid[i]
                i += 1 

def inverte():
    ###########################  pivo linha0 #############################
    check_pivo_linha0()
    pivo = linha0[0]
    
    #dividindo tudo pelo pivo -> colocando o pivo =1 
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

    #zerando a linha2
    i = 0
    cofator = linha2[0]
    while(i<size):              
        linha2[i] = linha2[i] - cofator*linha0[i]
        id2[i] = id2[i] - cofator*id0[i]
        i += 1

    ###########################  pivo linha1 #############################
    check_pivo_linha1()
    pivo = linha1[1] # ainda tem que checar se ele ?? diferente de 0
    i = 0
    # #dividindo a linha1 pelo pivo -> colocando o pivo =1
    while (i<size):
        linha1[i] = linha1[i]/pivo    
        id1[i] = id1[i]/pivo
        i +=1     
    ##zerando a linha 0 na coluna do pivo da linha1
    i = 0
    cofator = linha0[1]
    while(i<size):      
        linha0[i] = linha0[i] - cofator*linha1[i]
        id0[i] = id0[i] - cofator*id1[i]
        i +=1
    i = 0
    #zerando a linha 2 na coluna do pivo da linha1 
    cofator = linha2[1]
    while(i<size):      
        linha2[i] = linha2[i] - cofator*linha1[i]
        id2[i] = id2[i] - cofator*id1[i]
        i +=1        
    
    ###########################  pivo linha2 #############################
    pivo = linha2[2]
    #dividindo tudo pelo pivo -> colocando o pivo =1 
    i = 0    
    while (i<size):
        linha2[i] = linha2[i]/pivo
        id2[i] = id2[i]/pivo
        i += 1
    #zerando a linha1
    i = 0
    cofator = linha1[2]
    while(i<size):              
        linha1[i] = linha1[i] - cofator*linha2[i]
        id1[i] = id1[i] - cofator*id2[i]
        i += 1

    #zerando a linha0    
    i = 0
    cofator = linha0[2]
    while(i<size):      
        linha0[i] = linha0[i] - cofator*linha2[i]
        id0[i] = id0[i] - cofator*id2[i]
        i +=1  
   
   
    print(linha0, id0)
    print(linha1, id1)
    print(linha2, id2) 



global linha0, linha1, linha2, id0, id1, id2, size
linha0 = [0,2,2]
linha1 = [0,6,4]
linha2 = [0,9,4]

id0 = [1, 0, 0]
id1 = [0, 1, 0]    
id2 = [0, 0, 1]
size = 3
print(linha0, id0)
print(linha1, id1)
print(linha2, id2) 
inverte()        
    
            
            
            
        
        
        
    
    
        
        
        
    
    
    
    