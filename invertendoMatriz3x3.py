linha1 = [1,3]
linha2 = [2,1]
id1 = [1, 0]
id2 = [0, 1]
size = 2
def inverte(linha1, linha2, id1, id2):
    #pivo linha 1
    pivo = linha1[0]
    i = 0
    while (i<size):
        linha1[i] = linha1[i]/pivo
        id1[i] = id1[i]/pivo
        i += 1
    #zerando a linha2
    i = 0
    cofator = linha2[0]
    while(i<size):              
        linha2[i] = linha2[i] - cofator*linha1[i]
        id2[i] = id2[i] - cofator*id1[i]
        i += 1


    pivo = linha2[1]
    i = 0
    while (i<size):
        linha2[i] = linha2[i]/pivo    
        id2[i] = id2[i]/pivo
        i +=1
        

    #zerando a linha 1
    i = 0
    cofator = linha1[1]
    while(i<size):      
        linha1[i] = linha1[i] - cofator*linha2[i]
        id1[i] = id1[i] - cofator*id2[i]
        i +=1
    
    print(linha1, id1)
    print(linha2,id2)

        

    #print(linha1, id1, '\n', linha2, id2)    

    

        

inverte(linha1, linha2, id1, id2)        
    
            
            
            
        
        
        
    
    
        
        
        
    
    
    
    