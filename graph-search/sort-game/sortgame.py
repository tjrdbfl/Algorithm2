from collections import deque

# deque: bfs 를 위한 큐

def sortgame(n,perm):
    target="01234567"[:n] # n = 4문자열 target은 "0123"
    queue=deque([(0,perm)]) # 초기 상태는 튜플로 (0, perm)
    visited=set(perm) # 방문한 순열을 추적하기 위한 세트 만들기 
    while queue:
        dist,here=queue.popleft()
        if here==target: # queue 에서 꺼낸 노드가 도착점이면 
            return dist
        for i in range(n-1):
            for j in range(i+2,n+1):
                there=here[:i]+here[i:j][::-1]+here[j:] # i 에서 j 까지 뒤집기 
                if there not in visited: # 아직 방문하지 않은 정점이면
                    queue.append((dist+1,there)) # 거리를 증가하고 큐에 추가
                    visited.add(there) # 방문 집합에 추가 
    return -1 # bfs 가 끝나기 전에 target을 만나지 못한 경우 

for _ in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split())) # nums = [3, 1, 4, 2]
    sort=sorted(nums) # sort = [1, 2, 3, 4]
    perm=[sort.index(x) for x in nums] # perm = [2, 0, 3, 1]
    print(sortgame(n,"".join(map(str,perm)))) # 각 정수를 perm문자열로 변환