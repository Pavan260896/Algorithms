import random
def QuickSort(A,l,r):
	if l>=r:
		return
	k=random.randint(l,r)
	A[k],A[l]=A[l],A[k]
	m=Partition(A,l,r)
	QuickSort(A,l,m-1)
	QuickSort(A,m+1,r)
	return A

def Partition(A,l,r):
	x=A[l]
	j=l
	for i in range(l+1,r+1):
		if A[i]<=x:
			j+=1
			A[i],A[j]=A[j],A[i]
	A[l],A[j]=A[j],A[l]
	return j

if __name__=='__main__':
	A=list(map(int,input().split()))
	print(*QuickSort(A,0,len(A)-1))