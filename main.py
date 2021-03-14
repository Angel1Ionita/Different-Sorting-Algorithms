import math
import random
import time

with open('teste.in') as f:
    T=int(f.readline())
    N_Max_List = [tuple(int(num) for num in line.split()) for line in f]
#N_Max_List retine valorile pentru N , respectiv max intr-o lista de tupluri sub forma (N,Max)

def BubbleSort(L):
    if len(L)>25000:
        return
    while (1):
        ok = 1
        k = 1
        for i in range(len(L) - k):
            if L[i] > L[i + 1]:
                ok = 0
                L[i], L[i + 1] = L[i + 1], L[i]
        if ok == 1:
            break
        k += 1
def CountingSort(L):
    try:
        Lk=[0] * (max(L)+1)
        for i in L:
            Lk[i]+=1
        L.clear()
        for i in range(len(Lk)):
            if Lk[i]!=0:
                for j in range(Lk[i]):
                    L.append(i)
    except:
        pass
def RadixSort_10(L):
    if len(L)>10000000 and max(L)>10000000:
        return
    d=math.floor(math.log(max(L),10))+1
    b_10=[]
    for counter in range(d):
        for key in range(10):
            b_10.append([])
        for nr in L:
            b_10[nr//(10**counter)%10].append(nr)
        L.clear()
        for i in b_10:
            L.extend(i)
        b_10.clear()
def RadixSort_2(L):
    d=math.floor(math.log(max(L),2))+1
    b_2=[]
    for counter in range(d):
        for key in range(2):
            b_2.append([])
        for nr in L:
            b_2[(nr>>counter)&1].append(nr)
        L.clear()
        for i in b_2:
            L.extend(i)
        b_2.clear()
def MergeSort(L):
    if len(L)>9000000:
        return
    if len(L)>1 :
        m = len(L)//2
        Ls = L[:m]
        Lr = L[m:]
        MergeSort(Ls)
        MergeSort(Lr)
        #------------------Interclasarea sublistelor---------------------------------------
        i = 0
        j = 0
        k = 0
        while i < len(Ls) and j < len(Lr):
            if Ls[i] <= Lr[j]:
                L[k] = Ls[i]
                i += 1
            elif Ls[i] > Lr[j]:
                L[k] = Lr[j]
                j += 1
            k+=1
        while i < len(Ls):
            L[k] = Ls[i]
            i += 1
            k += 1
        while j < len(Lr):
            L[k] = Lr[j]
            j += 1
            k += 1
        #--------------------------------------------------------------
def Medianof3(L,st,dr): #Calculeaza pozitia pivotului ca fiind Mediana din 3
    mij = (st+dr)// 2
    if L[st] > L[dr]:
        L[st],L[dr] = L[dr],L[st]
    if L[0] > L[mij]:
        L[st],L[mij] = L[mij],L[st]
    if L[mij] > L[-1]:
        L[mij],L[dr] = L[dr],L[mij]
    return mij
def partition(L,st,dr): #Creeaza partiliile in functie de pozitia pivotului
    pivot=L[Medianof3(L,st,dr)]
    L[Medianof3(L,st,dr)],L[dr] = L[dr],L[Medianof3(L,st,dr)]
    i=st
    for j in range(st,dr):
        if L[j] < pivot:
            L[i],L[j] = L[j],L[i]
            i += 1
    L[i],L[dr] = L[dr],L[i]
    return i
def QuickSort(L,st,dr):
    try:
        if len(L) > 11000000:
            return
        if st < dr :
            pivot=partition(L,st,dr)
            QuickSort(L,st,pivot-1)
            QuickSort(L,pivot+1,dr)
    except:
        pass
def TimSort(L):      #Algoritmul de sortare folosit in Python
    if len(L)>10000000:
        return
    L.sort()
#----------------------------------------------
def Test_BubbleSort(L):
    t0 = time.time()
    BubbleSort(L)
    t1 = time.time()
    print("BubbleSort", end=" ")
    print(t1 - t0, end=" ")
    if returnSortCheck(L) == 0:
        print("Too slow to sort the list",end=" ")
    SortCheck(L)
def Test_CountingSort(L):
    t0 = time.time()
    CountingSort(L)
    t1 = time.time()
    print("CountingSort", end=" ")
    print(t1 - t0, end=" ")
    SortCheck(L)
def Test_RadixSort_2(L):
    t0 = time.time()
    RadixSort_2(L)
    t1 = time.time()
    print("RadixSort LSD Base 2", end=" ")
    print(t1 - t0, end=" ")
    if returnSortCheck(L) == 0:
        print("Too slow to sort the list",end=" ")
    SortCheck(L)
def Test_RadixSort_10(L):
    t0 = time.time()
    RadixSort_10(L)
    t1 = time.time()
    print("RadixSort LSD Base 10", end=" ")
    print(t1 - t0, end=" ")
    SortCheck(L)
def Test_MergeSort(L):
    t0 = time.time()
    MergeSort(L)
    t1 = time.time()
    print("MergeSort", end=" ")
    print(t1 - t0, end=" ")
    if returnSortCheck(L) == 0:
        print("Too slow to sort the list",end=" ")
    SortCheck(L)
def Test_QuickSort(L,st,dr):
    t0 = time.time()
    QuickSort(L,st,dr)
    t1 = time.time()
    print("QuickSort", end=" ")
    print(t1 - t0, end=" ")
    if returnSortCheck(L) == 0:
        print("Too slow to sort the list",end=" ")
    SortCheck(L)
def Test_TimSort(L):
    t0 = time.time()
    TimSort(L)
    t1 = time.time()
    print("TimSort", end=" ")
    print(t1 - t0, end=" ")
    if returnSortCheck(L) == 0:
        print("Too slow to sort the list",end=" ")
    SortCheck(L)
def returnSortCheck(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return 0
    return 1
def SortCheck(L): #Verifica daca lista a fost sortata cu success , caz in care afiseaza PASS , altfel FAIL
    if returnSortCheck(L)==0:
        print("FAIL")
    else:
        print("PASS")
    

print("\n")
for nr_test in range(T):
    Laux = [random.randint(0, N_Max_List[nr_test][1]) for i in range(N_Max_List[nr_test][0])]
    L = Laux.copy()
    print("Test",nr_test+1,": N =",N_Max_List[nr_test][0],", Max =",N_Max_List[nr_test][1])
    Test_BubbleSort(L)
    L = Laux.copy()
    Test_CountingSort(L)
    L = Laux.copy()
    Test_RadixSort_2(L)
    L = Laux.copy()
    Test_RadixSort_10(L)
    L = Laux.copy()
    Test_MergeSort(L)
    L = Laux.copy()
    Test_QuickSort(L,0,len(L)-1)
    L = Laux.copy()
    Test_TimSort(L)
    print("\n",end="")


