from collections import defaultdict

to_index=lambda word: (ord(word[0])-ord('a'),ord(word[-1])-ord('a'))

# 오일러 경로 또는 오일러 회로가 존재하는지 확인
def check_euler(indeg, outdeg):
    start, end = 0, 0
    for i in range(26):
        delta = outdeg[i] - indeg[i] # 모든 정점에 대해 delta 값은 -1,0,1 만 존재 가능
        if delta < -1 or delta > 1:
            return False
        if delta == 1:
            start += 1
        if delta == -1:
            end += 1
    return (start == 1 and end == 1) or (start == 0 and end == 0)
    # 두 조건을 만족하지 않으면 오일러 경로는 존재하지 x
    # start==1 and end==1 : 오일러 경로
    # start==0 and end==0 : 오일러 회로  

# DFS로 오일러 경로 생성
def get_euler_circuit(here, adj, circuit):
    for there in range(26):
        while adj[here][there] > 0:
            adj[here][there] -= 1
            get_euler_circuit(there, adj, circuit)
    circuit.append(here)

# 오일러 경로 혹은 회로 생성
def get_euler_trail_or_circuit(adj, indeg, outdeg):
    circuit = []
    for i in range(26):
        if outdeg[i] == indeg[i] + 1:  # 시작점
            get_euler_circuit(i, adj, circuit)
            return circuit
    for i in range(26):
        if outdeg[i] > 0:  # 회로일 경우
            get_euler_circuit(i, adj, circuit)
            return circuit
    return circuit


# 그래프 생성
def make_graph(words):
    adj = [[0] * 26 for _ in range(26)]
    graph = defaultdict(list) # 키가 (a, b)인 딕셔너리로 사용, 키가 없을 때 자동으로 빈 리스트 []를 기본값으로 할당
    indeg = [0] * 26 # i 로 시작하는 단어 수
    outdeg = [0] * 26 # i 로 끝나는 단어 수
    
    for word in words:
        a, b = to_index(word)
        graph[(a, b)].append(word)  # 단어 저장
        adj[a][b] += 1  # 간선 추가
        outdeg[a] += 1  # 진출 차수 증가
        indeg[b] += 1  # 진입 차수 증가
    
    return adj, graph, indeg, outdeg

# 단어 체인 생성
def wordchain(words):
    adj, graph, indeg, outdeg = make_graph(words)
    if not check_euler(indeg, outdeg):  # 오일러 조건 확인
        return "IMPOSSIBLE"
    
    circuit = get_euler_trail_or_circuit(adj, indeg, outdeg)
    if len(circuit) != len(words) + 1:  # 모든 단어를 사용했는지 확인
        return "IMPOSSIBLE"
    
    circuit.reverse()  # 경로 뒤집기
    ret=""
    for i in range(1,len(circuit)):
        a,b=circuit[i-1],circuit[i]
        if len(ret)!=0:
            ret+=" "
        ret+=graph[(a,b)][-1]
        graph[(a,b)].pop()
    return ret


# 입력 처리
for _ in range(int(input())):
    n = int(input())
    words = [input() for _ in range(n)]
    print(wordchain(words))
