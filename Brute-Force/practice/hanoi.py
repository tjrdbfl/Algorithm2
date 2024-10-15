# n: 옮기려는 원판의 개수.
# src: 원판을 옮길 출발지 막대.
# via: 중간에 사용할 보조 막대.
# dst: 원판을 옮길 목적지 막대.
def hanoi(n,src,via,dst):
    if n==1:
        print(f"Move from {src} to {dst}")
    else:
        hanoi(n-1,src,dst,via) # 1단계: n-1개의 원판을 보조막대로 옮김
        hanoi(1,src,via,dst)  # 2단계: 가장 큰 원판을 목적지로 옮김
        hanoi(n-1,via,src,dst)  # 3단계: 보조막대에 있는 n-1개의 원판을 목적지로 옮김