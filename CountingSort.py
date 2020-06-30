
def CountingSort(A,M):
	Count=[0 for i in range(M+1)]
	for k in A:
		Count[k]+=1
	Pos=[0 for i in range(M+1)]
	Pos[0]=0
	for j in range(1,M+1):
		Pos[j]=Pos[j-1] + Count[j-1]
	S=[0 for i in range(len(A))]
	for k in A:
		S[Pos[k]]=k
		Pos[k]+=1
	return S

if __name__=='__main__':
	A=list(map(int,input().split()))
	M=int(input())
	print(*CountingSort(A,M))