"""
Created on Fri Feb 22 16:13:39 2019

@author: alunos-lmc04
"""
import timeit
from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randrange
import sys
import itertools as it


mpl.use('Agg')

     
def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def sort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst  

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
    while tam > 0:
        lista.append(tam)
        tam-=1
    return lista   
        

def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'quickSort')
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(label)
    
x = [10000,20000,30000,40000,50000]

yPiorCaso = []
yMedioCaso = []
yMelhorCaso = []

#print(geraLista(100))
for i in x:
    lista = geraListaDecresc(i)
    yPiorCaso.append(timeit.timeit('sort({})'.format(lista),setup="from __main__ import sort",number=1))
    
    lista = geraListaAleatoria(i)
    yMedioCaso.append(timeit.timeit('sort({})'.format(lista),setup="from __main__ import sort",number=1))
    
    lista = geraListaCresc(i)
    yMelhorCaso.append(timeit.timeit('sort({})'.format(lista),setup="from __main__ import sort",number=1))

desenhaGrafico(x,yPiorCaso,'Quantidade','Tempo','Pior_Caso')    
desenhaGrafico(x,yMedioCaso,'Quantidade','Tempo','Medio_Caso')
desenhaGrafico(x,yMelhorCaso,'Quantidade','Tempo','Melhor_Caso')
       
