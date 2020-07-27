
def insertionSort(A):
	n=len(A)
	for i in range(1,n):
		key=A[i]
		place=i
		while place>0:
			if A[place-1]>key:
				A[place]=A[place-1]
				place-=1
			else:
				break
		A[place]=key
	return A

if __name__=='__main__':
	A=list(map(int,input().split()))
	print(insertionSort(A))
