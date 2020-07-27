
def bubbleSort(A):
	lastsorted=len(A)-1
	not_sorted=True
	while not_sorted:
		not_sorted=False
		for i in range(lastsorted):
			if A[i]>A[i+1]:
				A[i],A[i+1]=A[i+1],A[i]
				not_sorted=True
		lastsorted-=1
	return A

if __name__=='__main__':
	A=list(map(int,input().split()))
	print(bubbleSort(A))