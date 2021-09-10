#This is the selection sort Algorithms

def ssort(aList):
    for i in range(len(aList)):
        least=i
        for j in range(i+1,len(aList)):
            if aList[j]<aList[least]:
                least=j
        swap(aList,least,i)


def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp


a=[]

n=int(input('Enter the upper limit:'))

for i in range(n):
    a.append(int(input()))


ssort(a)

print('After sorting:',a)