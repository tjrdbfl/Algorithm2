# {'cl':0,'bom':1,'dara':2,'minzy':3}
# eaters={
# 0:[2,3],
# 1:[0,3],
# 2:[0,2],
# 3:[0]
# }

# chosen: 지금까지 고른 음식 수
# food : 이번에 고려해야할 음식 번호
# edible[i] : 지금까지 고른 음식 중 i번 친구가 먹을 수 있는 음식의 수
def search(food,edible,chosen):
    global best
    if chosen>=best:
        return 
    if food==m: # 모든 음식에 대해 만들지 여부를 결정했으면 
        if all(edible): # 모든 친구가 1 이상의 값을 가지고 있는지
            best=chosen # 모든 친구가 음식을 먹을 수 있으면, 최적해 갱신
    else:
        search(food+1,edible,chosen) # food를 만들지 않는 경우

        for j in eaters[food]:  # food를 만드는 경우
            edible[j]+=1
        search(food+1,edible,chosen+1)

        for j in eaters[food]: # 탐색이 끝나면 다시 이 값을 원래대로 돌려놓고, 다른 경로를 탐색하기 위해 상태 복구
            edible[j]-=1

for _ in range(int(input())):
    n,m=map(int,input().split())
    friends={k:i for i,k in enumerate(input().split())}
    eaters={i:[friends[name] for name in input().split()[1:]] for i in range(m)}
    best=m+1
    search(0,[0]*n,0)
    print(best)

