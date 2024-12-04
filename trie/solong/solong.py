class TrieNode:
    def __init__(self):
        self.children={}
        self.terminal=-1 # 이 노드에서 종료하는 문자열의 인덱스, 없으면 -1
        self.first=-1 # 이 노드를 루트로 하는 트라이에 가장 먼저 추가된 단어의 인덱스

    # 인덱스가 id인 문자열 key를 추가한다.
    def insert(self,key,id):
        if self.first==-1:
            self.first=id
        if not key: # 문자열 종료 시 
            self.terminal=id
        else:
            char=key[0]
            if char not in self.children:
                self.children[char]=TrieNode()
            self.children[char].insert(key[1:],id)

    # 문자열 key 가 사전에 있는지 찾는다.
    def find(self,key):
        if not key:  # 문자열 종료 시
            return self # self : Trie의 입력 문자열의 마지막 문자에 해당하는 현재 노드() 를 반환
        else:
            char=key[0]
            if char not in self.children:
                return None
            return self.children[char].find(key[1:])

    # 여기까지 타이핑했을 때, 인덱스가 id인 key를 타이핑하기 위해 몇 번의 키를 더 눌러야 할까?
    def type(self,key,id):
        if not key: # 문자열 종료 시
            return 0
        else:
            if self.first==id: # 이 노드에서 추천되는 문자열이 이 문자열이면
                return 1 # 탭 키를 누르고 종료
            return 1+self.children[key[0]].type(key[1:],id)


# 사전을 나타내는 trie 가 주어질 때,
# 단어 word를 타이핑하는 데 몇 번이나 키를 눌러야 하는지 계산
def count_keys(trie,word):
    node=trie.find(word)
    if not node or node.terminal==-1:
        return len(word)
    else:
        return trie.type(word,node.terminal)
        
# SOLONG 문제를 트라이를 이용하여 해결
def solong(dicwords, keywords):
    # 사전의 단어들을 출현 빈도의 내림차순, 단어의 오름차순으로 정렬
    # 정렬된 순서로 추가하면 사전의 인덱스 번호를 각 노드의 추천 단어 번호로 쓸 수 있다.
    dicwords.sort(key=lambda x : (-int(x[1]),x[0]))
    trie=TrieNode()
    for i,x in enumerate(dicwords):
        trie.insert(x[0],i)  # x[0]: 'ALL'
    trie.first=-1 # 아무 글자도 입력하지 않으면 자동완성을 하지 않는다.
    cnt=sum(count_keys(trie,s) for s in keywords)
    return cnt + len(keywords) - 1 # cnt : 문자열 타자 수, len(keywords)-1 : 공백 수 

for _ in range(int(input())):
    n,m=map(int,input().split())
    dicwords=[input().split() for _ in range(n)]
    keywords=input().split() 
    print(solong(dicwords,keywords))

# dicwords = [['ALL', '4'], ['AND', '3'], ['FISH', '8'], ['FOR', '6'], ['SO', '4'], ['THANKS', '9'], ['THE', '9']]
# keywords = ['SO', 'LONG', 'AND', 'THANKS', 'FOR', 'ALL', 'THE', 'FISH']
