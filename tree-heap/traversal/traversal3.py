# 전위, 후위 -> 중위 순회 출력
# full binary search tree 일 때만 가능
def traversal(preorder,postorder):
    assert(len(preorder)==len(postorder))
    root=preorder[0]
    if len(preorder)==1: #왼쪽 자식 노드가 없으므로
        print(root,end=" ")
    elif preorder:
        # 후위 순위에서 왼쪽 자식 노드의 위치 + 1
        pos=postorder.index(preorder[1])+1
        traversal(preorder[1:pos+1],postorder[:pos])
        print(root,end=" ")
        traversal(preorder[pos+1:],postorder[pos:-1])        

for _ in range(int(input())):
    n=int(input())
    preorder=list(map(int,input().split()))
    postorder=list(map(int,input().split()))
    traversal(preorder,postorder)