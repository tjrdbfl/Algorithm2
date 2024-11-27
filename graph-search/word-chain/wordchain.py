from collections import defaultdict

# 단어를 그래프의 두 인덱스로 변환
def to_index(word):
    return ord(word[0]) - ord('a'), ord(word[-1]) - ord('a')

# 그래프 생성
def make_graph(words):
    adj = [[0] * 26 for _ in range(26)]
    graph = defaultdict(list)
    indeg = [0] * 26
    outdeg = [0] * 26
    
    for word in words:
        a, b = to_index(word)
        graph[(a, b)].append(word)  # 단어 저장
        adj[a][b] += 1  # 간선 추가
        outdeg[a] += 1  # 진출 차수 증가
        indeg[b] += 1  # 진입 차수 증가
    
    return adj, graph, indeg, outdeg

# 오일러 경로 조건 확인
def check_euler(indeg, outdeg):
    start, end = 0, 0
    for i in range(26):
        delta = outdeg[i] - indeg[i]
        if delta < -1 or delta > 1:
            return False
        if delta == 1:
            start += 1
        if delta == -1:
            end += 1
    return (start == 1 and end == 1) or (start == 0 and end == 0)

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

# 단어 체인 생성
def wordchain(words):
    adj, graph, indeg, outdeg = make_graph(words)
    if not check_euler(indeg, outdeg):  # 오일러 조건 확인
        return "IMPOSSIBLE"
    
    circuit = get_euler_trail_or_circuit(adj, indeg, outdeg)
    if len(circuit) != len(words) + 1:  # 모든 단어를 사용했는지 확인
        return "IMPOSSIBLE"
    
    circuit.reverse()  # 경로 뒤집기
    ret = []
    for i in range(1, len(circuit)):
        a, b = circuit[i - 1], circuit[i]
        ret.append(graph[(a, b)].pop())
    return " ".join(ret)

# 입력 처리
for _ in range(int(input())):
    n = int(input())
    words = [input() for _ in range(n)]
    print(wordchain(words))
