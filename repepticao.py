############ formato de código para zerar clinhas abaixo e acima dos pivos  
""" for i in range(10):   
    print("__________________________")
    for j in range(10):        
        if (j==i):
            continue
        else:
            print("lucca{i}".format(i = j))  """

############ formato de código para gerar checagem dos pivos           
for i in range(10):
    print("__________________________")
    for j in range(10):
        if(j<=i):
            continue
        else:
            print("lucca{i}".format(i=j)) 

                   
########

tamanho = 10
print("aux = [", end = '')
for i in range(tamanho):
  print("0", end = '')
  if(i != tamanho-1):
    print(",", end = '')
print("]", end = '')  

