def fw_add(pos,x):
    global tree
    while pos<len(tree):
        tree[pos]+=x
        pos+=(pos&-pos)

def fw_sum(pos):
    global tree
    ret=0
    while pos>0:
        ret+=tree[pos]
        pos&=(pos-1)
    return ret


arr=[0]+[7,3,9,8,5,1,2,6,4]
n=len(arr)
tree=[0]*(n+1)
for i in range(1,n+1):
    fw_add(i,arr[i])
    print("add",i,arr[i],tree)

print(fw_sum(n))
print(fw_sum(7)-fw_sum(5))    