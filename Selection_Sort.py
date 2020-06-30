def SelectionSort(A):
	for i in range(len(A)):
		min_index=i
		for j in range(i+1,len(A)):
			if A[j]<A[min_index]:
				min_index=j
		if i!=min_index:
			A[min_index],A[i]=A[i],A[min_index]
	return A

if __name__=='__main__':
	A=list(map(int,input().split()))
	print(SelectionSort(A))