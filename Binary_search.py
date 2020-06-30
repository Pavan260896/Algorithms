def BinarySearch(A,l,h,k):
	while l<=h:
		mid=int(l + (h-l)/2)
		if A[mid]==k:
			return mid
		elif A[mid]<k:
			l=mid+1
		else:
			h=mid-1
	return -1
if __name__=='__main__':
	A=list(map(int,input().split()))
	k=int(input())
	print(BinarySearch(A,0,len(A)-1,k))