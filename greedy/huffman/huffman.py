from heapq import heapify,heappop,heappush
# 허프만 트리
class Node:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None

def print_preorder(node):
    if node:
        print(f"({node.char},{node.freq})",end=" ")
        print_preorder(node.left)
        print_preorder(node.right)

def print_inorder(node):
    if node:
        print(node.left)
        print(f"{node.char}, {node.freq}",end=" ")
        print_inorder(node.right)

def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(f"{node.char}, {node.freq}",end=" ")

def huffman(pairs):
    pq=[(int(f),Node(c,int(f))) for c,f in pairs]
    heapify(pq)
    while len(pq)>1:
        freq1,node1=heappop(pq)
        freq2,node2=heappop(pq)
        node=Node("+",freq1+freq2)
        node.left=node1
        node.right=node2
        heappush(pq,(freq1+freq2,node))
    return pq[0][1] # 허프만 트리의 root node 

# 허프만 트리를 순회하면서, 각 문자에 대해 이진 인코딩을 생성하고 이를 encoder 딕셔너리에 저장
def make_encoder(node,code,encoder):
    if node.char!='+':
        encoder[node.char]=code
    else:
        make_encoder(node.left,code+"0",encoder)
        make_encoder(node.right,code+"1",encoder)

# 인코딩된 문자열을 생성
def encode(s,encoder):
    encoded=""
    for char in s:
        encoded+=encoder[char]
    return encoded

# 각 문자는 루트에서 리프 노드까지 경로를 따라가며 디코딩
# 한 문자가 완전히 디코딩된 후, 다음 문자를 디코딩할 때는 다시 루트에서 시작해야 하므로, node가 아닌 root를 사용해 재귀 호출
def decode(node,encoded,i,decoded):
    global root
    if node.char!="+": # 리프노드인지 확인
        decoded+=[node.char]
        if i<len(encoded): # 디코딩할 부분이 존재할 경우
            decode(root,encoded,i,decoded)
    elif encoded[i]=="0":
        decode(node.left,encoded,i+1,decoded)
    else:
        decode(node.right,encoded,i+1,decoded)


n=int(input())
pairs=[input().split() for _ in range(n)]
root=huffman(pairs)
print_preorder(root)
print()
print_inorder(root)
print()
encoder={}
make_encoder(root,"",encoder)
encoded=encode("abcdef",encoder)
print(encoded)
decoded=[]
decode(root,encoded,0,decoded)
print(*decoded)
