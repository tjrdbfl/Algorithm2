# {'cl':0,'bom':1,'dara':2,'minzy':3}
# 각 친구의 번호별로 먹을 수 있는 음식의 번호 리스트를 저장
# eaters={
# 0:[2,3],
# 1:[0,3],
# 2:[0,2],
# 3:[0]
# }
# eatables={
# 0: [1,2,3],
# 1: [4,5],
# 2: [0,2,4],
# 3: [0,1,5]
#}
def search(edible, chosen):
    global best
    if chosen>=best:
        return
    try: # 아직 먹을 음식이 없는 첫 번째 친구를 찾는다.
        first=edible.index(0)
    except: # 모든 친구가 먹을 음식이 있는 경우
        best=chosen
    else: # try 블록이 정상적으로 실행된 경우에만 실행된다.
        for food in eatables[first]:
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

    best=m+1
    search([0]*n,0)
    print(best)
