#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 10:29:08 2022

@author: ashleylarweck
"""
# -*- coding: utf-8 -*-
"""
HW1 Code 
"""
import random

import matplotlib.pyplot as plt
from IPython import get_ipython


#%% Q1 Selection Sort; although not required, it should be in-place sorting (sort the original list)

def selectionSort(numList):
    """Given a list of numbers, return a list in sorted order (least to largest)
        Note that the function may change the original list (in-place sorting)
    """
    for i in range(len(numList)):
        min_idx = i

        for j in range(i + 1, len(numList)):
         

            if numList[j] < numList[min_idx]:
                min_idx = j
         
        (numList[i], numList[min_idx]) = (numList[min_idx], numList[i])
        
    return numList
    

#%% Testing selection sort

a = [random.randint(0, 20) for _ in range(10)]
print('\n\n********* Q1 *********')
print('random array is: ', a)
    
b = selectionSort(a)
print('selection sorted array is: ', b)

if b == sorted(a):
    print('selectionSort is correct') 

    print('Profiling running time of python sorted function on a:')
    get_ipython().run_line_magic('timeit', 'sorted(a)')

    print('Profiling running time of my merge sort function on a:')
    get_ipython().run_line_magic('timeit', 'selectionSort(a)')

else:
# replace the following statement with a print statement if your selection sort is incorrect 
# but you want to continue with the rest of the code
    print("Selection Sort is Incorrect.")


#%% Q2a. Merge function

def merge(sortListA, sortListB):
    """Given two non-decreasingly sorted list of numbers, 
       return a single merged list in non-decreasing order
    """
    list_final = sortListA + sortListB
    
    list_final = selectionSort(list_final)
    
    return list_final


#%% Testing merge function

a = sorted([random.randint(0, 10) for _ in range(5)]) # a is sorted 
b = sorted([random.randint(0, 10) for _ in range(4)]) # b is sorted

print('\n\n********* Q2a *********')
print('a is: ', a)
print('b is: ', b)

c = merge(a, b) # c should be sorted(a+b)
print('merged result: ', c)

if (c == sorted(a + b)):
    print('merge is correct')
else:
# replace the following statement with a print statement if your merge function is incorrect 
# but you want to continue with the rest of the code
    print("Merge is Incorrect.")  


#%% Q2b merge sort; not an in-place sorting (returns a new sorted list)

def mergeSort(numList):
    """
    Given a list of numbers in random order, 
    return a new list sorted in non-decreasing order, 
    and leave the original list unchanged.
    """
    sortedList = numList
    
    if len(sortedList) > 1:
  
        mid = len(sortedList)//2
        L = sortedList[:mid]
        R = sortedList[mid:]
  
        mergeSort(L)
  
        mergeSort(R)
  
        i = j = k = 0
  
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sortedList[k] = L[i]
                i += 1
            else:
                sortedList[k] = R[j]
                j += 1
            k += 1
  
        while i < len(L):
            sortedList[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            sortedList[k] = R[j]
            j += 1
            k += 1
        
    return sortedList


#%% Test mergeSort function
    
    
a = [random.randint(0, 20) for _ in range(10)]
    

print('\n\n********* Q2b *********')
print('random array is: ', a)


b = mergeSort(a)
print('merge sorted array is: ', b)


if b == sorted(a):
    print('mergeSort is correct') 
    print('profiling running time of python sorted function on a:')
    get_ipython().run_line_magic('timeit', 'sorted(a)')

    print('profiling running time of my merge sort function on a:')
    get_ipython().run_line_magic('timeit', 'mergeSort(a)')

else:
# replace the following statement with a print statement if your merge sort is incorrect 
# but you want to continue with the rest of the code
    raise SystemExit('mergeSort is incorrect')




#%% Q3 run the three sorting algorithms on different input sizes and collect running time

import time

# input size is 500 * (1, 2, 4, ..., 32)
sizes = [500 * 2**i for i in range(6)]


merge_sort_time = [0] * len(sizes)
selection_sort_time = [0] * len(sizes)
quick_sort_time = [0] * len(sizes)

print('\n\n********* Q3 *********')
print('Collecting running time (in milliseconds)')

for i in range(len(sizes)):
    print('iteration %d, size = %d' %(i, sizes[i]))
    # random array of size sizes[i]
    a = [random.random() for _ in range(sizes[i])]
    start_time = time.perf_counter()
    sorted(a)
    quick_sort_time[i] = 1000*(time.perf_counter() - start_time) 
    start_time = time.perf_counter()
    mergeSort(a)
    merge_sort_time[i] = 1000*(time.perf_counter() - start_time) 
    start_time = time.perf_counter()
    selectionSort(a)
    selection_sort_time[i] = 1000*(time.perf_counter() - start_time)  


# complete the following code to plot the running time; use the style show in the homework 
# document as template, reproduce as much detail as possible.

#%% Q3a. plot running time (Fig 1)

fig, ax = plt.subplots()

ax.set_title('Fig 1')
plt.xlabel('Input Size')
plt.ylabel('Time (ms)')

plt.plot(sizes, quick_sort_time, 'r', label = "Quick Sort", linestyle=":", marker="x")
plt.plot(sizes, merge_sort_time, 'g', label = "Merge Sort", linestyle="-.", marker="*")
plt.plot(sizes, selection_sort_time, 'b', label = "Selection Sort", linestyle="dashdot", marker="*")
plt.legend()
plt.xlim([-500, 17000])
plt.ylim([-500,10000])
plt.show()

#%% Q3b. plot running time (Fig 2)

fig, ax = plt.subplots()
ax.set_title('Fig 2')
plt.xlabel('Input Size')
plt.ylabel('Time (ms)')

plt.plot(sizes, quick_sort_time, 'r', label = "Quick Sort", linestyle=":", marker="x")
plt.plot(sizes, merge_sort_time, 'g', label = "Merge Sort", linestyle="-.", marker="*")
plt.plot(sizes, selection_sort_time, 'b', label = "Selection Sort", linestyle="dashdot", marker="*")
plt.legend()
plt.xlim([-500, 17000])
plt.yscale("log")
plt.show()

#%% Q3c. plot running time per input element (Fig 3)

qsL = [i / j for i, j in zip(quick_sort_time, sizes)]
msL = [i / j for i, j in zip(merge_sort_time, sizes)]
ssL = [i / j for i, j in zip(selection_sort_time, sizes)]

fig, ax = plt.subplots()
ax.set_title('Fig 3')
plt.xlabel('Input Size')
plt.ylabel('Time (ms) per input element')

plt.plot(sizes, qsL, 'r', label = "Quick Sort", linestyle=":", marker="x")
plt.plot(sizes, msL, 'g', label = "Merge Sort", marker="*")
plt.plot(sizes, ssL, 'b', label = "Selection Sort", linestyle="dashdot", marker="*")
plt.legend()
plt.xlim([-500, 17000])
plt.ylim([-0.05,0.7])

plt.show()

#%% Q3d. plot running time per input element (Fig 4)

fig, ax = plt.subplots()
ax.set_title('Fig 4')
plt.xlabel('Input Size')
plt.ylabel('Time (ms) per input element')

plt.plot(sizes, qsL, 'r', label = "Quick Sort", linestyle=":", marker="x")
plt.plot(sizes, msL, 'g', label = "Merge Sort", marker="*")
plt.plot(sizes, ssL, 'b', label = "Selection Sort", linestyle="dashdot", marker="*")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.ylim([-0.00001, 1])


plt.show()