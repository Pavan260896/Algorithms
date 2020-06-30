
def MergeSort(A):
	if len(A)<=1:
		return A
	mid=int(len(A)/2)
	B=MergeSort(A[:mid])
	C=MergeSort(A[mid:])
	S=Merge(B,C)
	return S
def Merge(B,C):
	D=[]
	i=0
	j=0
	while i<len(B) and j<len(C):
		b=B[i]
		c=C[j]
		if b<=c:
			D.append(b)
			i+=1
		else:
			D.append(c)
			j+=1
	if i<len(B):
		D.extend(B[i:])
	if j<len(C):
		D.extend(C[j:])
	return D
if __name__=='__main__':
	A=list(map(int,input().split()))
	print(MergeSort(A))