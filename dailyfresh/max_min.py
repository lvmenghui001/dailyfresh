L = [5,40,9,20,3]
def myMaxMin(L,start,end):
    if end-start <=1:
        return (max(L[start],L[end]),min(L[start],L[end]))
    else:
        max1,min1 = myMaxMin(L,start,(start+end)//2)
        max2,min2 = myMaxMin(L,(start+end)//2+1,end)
    return max(max1,max2),min(min1,min2)

def maxMin(L):
    assert(type(L)==type([]) and len(L) >0)
    return myMaxMin(L,0,len(L)-1)

print(maxMin(L))