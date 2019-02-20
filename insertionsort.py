#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:15:43 2019

@author: alunos-lmc04
"""
import itertools as it
import timeit
from random import randint
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')
 
swap=[]

# Function to do insertion sort 
def insertionSort(arr): 
    swaps = 0
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        swaps+=1
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        return swaps
    
x = [10000,20000,30000,40000,50000]
yMelhor = []
yPior = []
y = []




def geraLista(tam):
    lista = []
    while tam>len(lista):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

for i in range (5):
para gerar com aleatatorio utilizar geralista, geralistacres para a lista do melhor caso e geralistadecres para o pior caso
  lista=geraLista(x[i])
  yMelhor.append(timeit.timeit("insertionSort({})".format(sorted(lista)),setup="from __main__ import insertionSort",number=1))
  yPior.append(timeit.timeit("insertionSort({})".format(sorted(lista,reverse = True)),setup="from __main__ import insertionSort",number=1))
  y.append(timeit.timeit("insertionSort({})".format(lista),setup="from __main__ import insertionSort",number=1))
  swap.append(bubble_sort(lista))

para gerar o grafico do tempo de ordenacao do insertion sort
desenhaGrafico(x,y)
desenhaGrafico(x,yPior)
desenhaGrafico(x,yMelhor)
para gerar o grafico do numero de verificacoes em cada ordenacao
desenhaGrafico(x,swap)

pertmutacoes
lista = list(it.permutations([1,2,3,4,5,6],6))
ListaPermut = []

for i in lista:
    ListaPermut.append(list(i))
tempos = []
for i in ListaPermut:
    tempos.append(timeit.timeit("insertionSort({})".format(lista),setup="from __main__ import insertionSort",number=10))
    
print('Pior caso:', ListaPermut(tempos))

