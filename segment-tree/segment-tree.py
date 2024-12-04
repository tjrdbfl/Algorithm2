INF=float('inf')

def query(node,low,high,left,right):
    if right<low or high<left:
        return INF
    elif left<=low and high<=right:
        return range_min[node]
    else:
        mid=(low+high)//2
        lmin=query(2*node,low,mid,left,right)
        rmin=query(2*node+1,mid+1,high,left,right)
        return min(lmin,rmin)

def update(node,low,high,i,x):
    if i<low or high<i:
        return range_min[node]
    elif low==high:
        range_min[node]=x
        return range_min[node]
    else:
        mid=(low+high)//2
        lmin=update(2*node,low,mid,i,x)
        rmin=update(2*node+1,mid+1,high,i,x)
        range_min[node]=min(lmin,rmin)
        return range_min[node]

def init(node,low,high):
    if low==high:
        range_min[node]=arr[low]
        return range_min[node]
    else:
        mid=(low+high)//2
        lmin=init(2*node,low,mid)
        rmin=init(2*node+1,mid+1,high)
        range_min[node]=min(lmin,rmin)
        return range_min[node]

arr=[78,30,99,38,50,51,52,20,81]
n=len(arr)
range_min=[0]*(4*n) # 구간 트리 배열의 초기화
init(1,0,n-1) # 구간 트리 초기화 : 항상 1번 노드에서 찾기 
print(query(1,0,8,1,5))