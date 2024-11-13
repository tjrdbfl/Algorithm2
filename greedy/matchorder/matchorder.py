from bisect import bisect_left,bisect_right
# pop()은 리스트의 마지막 요소를 제거
# pop(0)은 리스트의 첫 번째 요소를 제거

def matchorder(n,russian,korean):
    korean.sort()
    wins=0
    for i in range(n):
        if korean[-1] < russian[i]: # 가장 레이팅이 높은 한국 선수가 이길 수 없는 경우
            korean.pop(0) # 가장 레이팅이 낮은 선수를 출전시킨다. 
        else:
            wins+=1 # 이길 수 있는 선수 중 가장 레이팅이 낮은 선수 출전시키기
            korean.pop(bisect_left(korean,russian[i])) # russian[i] 보다는 크지만 가장 레이팅이 낮은 인덱스 반환
    return wins

for _  in range(int(input())):
    n=int(input())
    russian=list(map(int,input().split()))
    korean=list(map(int,input().split()))
    print(matchorder(n,russian,korean))

