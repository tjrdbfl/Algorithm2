def insertion(n,shifted):
    A=list(range(1,n+1)) # 1부터 n 까지 수열 만들기
    B=[]
    for i in range(n-1,-1,-1):
        move=shifted[i] # 이동한 칸
        item=A[i-move]
        A.pop(i-move)
        B.append(item)
    return B[::-1] # 추가한 순서를 뒤집으면 원래의 수열 

for _ in range(int(input())):
    n=int(input())
    shifted=list(map(int,input().split()))
    print(*insertion(n,shifted))