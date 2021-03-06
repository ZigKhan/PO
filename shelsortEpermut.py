from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it

mpl.use('Agg')

def geraListaAleatoria(tam):
	lista = []
	while len(lista) < tam:
		n = randint(1,1*tam)
		if n not in lista: lista.append(n)
	return lista

def geraListaCresc(tam):
    lista = []
    i = 0
    while i <= tam:
        lista.append(i)
        i+=1
    return lista

def geraListaDecresc(tam):
    lista = []
    while tam >= 0:
        lista.append(tam)
        tam-=1
    return lista

def shellSort(arr): 
  
    
    n = len(arr) 
    gap = n//2
   
    while gap > 0: 
  
        for i in range(gap,n): 
  
            temp = arr[i] 
  
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
   
            arr[j] = temp 
        gap //= 2
        
        
def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'shellSort')
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(label)
    
x = [10000,20000,30000,40000,50000]

yPiorCaso = []
yMedioCaso = []
yMelhorCaso = []

lista = [1, 2, 3, 4, 5, 6]
listaPermutada = list(it.permutations(lista,6))

tempos = []

for i in x:
    lista = geraListaDecresc(i)
    yPiorCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))
    
    lista = geraListaAleatoria(i)
    yMedioCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))
    
    lista = geraListaCresc(i)
    yMelhorCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))

desenhaGrafico(x,yPiorCaso,'Quantidade','Tempo','Pior_Caso')    
desenhaGrafico(x,yMedioCaso,'Quantidade','Tempo','Medio_Caso')
desenhaGrafico(x,yMelhorCaso,'Quantidade','Tempo','Melhor_Caso')



for i in permut:
    tempos.append(timeit.timeit('shellSort({})'.format(listaPermutada),setup="from __main__ import shellSort",number=1))

maior = tempos.index(max(tempos))
menor = tempos.index(min(tempos))

print('Tempo maior:',max(tempo))
print(listaPermutada[maior])
print("\n")
print('Tempo menor:',max(tempo))
print(listaPermutada[maior])
