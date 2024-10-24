# 먹을 수 있는 음식의 종류가 적은 친구 먼저 찾기
# {'cl':0,'bom':1,'dara':2,'minzy':3}
# eaters={
# 0:[2,3],
# 1:[0,3],
# 2:[0,2],
# 3:[0]
# }

# eatables={
# (1, [4,5]),
# (0, [1,2,3]),
# (2, [0,2,4]),
# (3, [0,1,5])
#}

def search(edible,chosen):
    global best
    if chosen >= best:
        return
    for friend,foods in eatables:
        if edible[friend]==0:
            break
    else: # for 루프가 끝가지 실행되었을 때 
        best=chosen
        return
    for food in foods: # 이 친구가 먹을 수 있는 음식을 하나 남긴다
        for j in eaters[food]:
            edible[j]+=1
        search(edible,chosen+1)
        for j in eaters[food]:
            edible[j]-=1
            
for _ in range(int(input())):
    n,m=map(int,input().split())
    friends={k:i for i,k in enumerate(input().split())}
    eaters={i:[friends[name] for name in input().split()[1:]] for i in range(m)}
    eatables={i:[] for i in range(n)}
    for i in eaters:
        for j in eaters[i]:
            eatables[j].append(i)

    eatables=sorted(eatables.items(), key=lambda x: len(x[1]))
    best=m+1
    search([0]*n,0)
    print(best)


            