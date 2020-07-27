
def Quicksort(A,l,r):
	if l>=r:
		return
	m=Partition(A,l,r)
	Quicksort(A,l,m-1)
	Quicksort(A,m+1,r)
	return A

def Partition(A,l,r):
	pivot=A[l]
	j=l
	for i in range(l+1,r+1):
		if pivot>=A[i]:
			j+=1
			A[j],A[i]=A[i],A[j]
	A[l],A[j]=A[j],A[l]
	return j

if __name__=='__main__':
	A=list(map(int,input().split()))
	print(Quicksort(A,0,len(A)-1))