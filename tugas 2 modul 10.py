def tukar(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
    
def bubblesort (A,n):
    for i in range (n-1):
        if A[i] > A[i+1]:
            tukar(A,i,i+1)
        if n-1 > 1 :
            bubblesort(A, n-1)
            
A = [4,2,5,0,6,1,-1]
bubblesort(A, len(A))
print('\nlist yang sudah disorting : ')
print(A)
