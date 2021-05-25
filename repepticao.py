############ formato de código para zerar clinhas abaixo e acima dos pivos  
""" for i in range(10):   
    print("__________________________")
    for j in range(10):        
        if (j==i):
            continue
        else:
            print("lucca{i}".format(i = j))  """

############ formato de código para gerar checagem dos pivos           
""" for i in range(10):
    print("__________________________")
    for j in range(10):
        if(j<=i):
            continue
        else:
            print("lucca{i}".format(i=j))  """

                   
########

""" tamanho = 10
print("aux = [", end = '')
for i in range(tamanho):
  print("0", end = '')
  if(i != tamanho-1):
    print(",", end = '')
print("]", end = '')  

for i in range(tamanho):
  print("id{i} = [".format(i=i), end = '')
  for j in range(tamanho):   
    if (j==i):
      print("1", end = '')
    else:
      print("0", end = '') 
    if (j != tamanho-1):
      print(",", end = '')
  print("]\n", end = '')    """
tamanho = 5
print("aux = ", end = '')
for i in range(tamanho):
  print("linha{i}".format(i=i), end = '')
  if(i != tamanho-1):
    print(" + ", end = '')

