
def selectionSort(A):
	n=len(A)
	for i in range(n-1):
		min_index=i
		for j in range(i+1,n):
			if A[j]<A[min_index]:
				min_index=j
		if min_index!=i:
			A[min_index],A[i]=A[i],A[min_index]
	return A

if __name__=='__main__':
	A=list(map(int,input().split()))
	print(selectionSort(A))