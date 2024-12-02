# preorder, inorder 출력 결과로 -> postorder 출력 
def traversal(preorder,inorder):
    assert(len(preorder)==len(inorder))
    if preorder: # 텅 빈 트리면 곧장 종료
        root=preorder[0] # 전위 순회의 첫 원소는 루트 노드
        pos=inorder.index(root) # 중위 순회에서 루트 노드의 위치
        # 후위 순회 출력
        traversal(preorder[1:pos+1],inorder[:pos]) # 왼쪽 서브트리 재귀호출
        traversal(preorder[pos+1:],inorder[pos+1:]) # 오른쪽 서브트리 재귀호출
        print(root,end=" ") # 후위 순회이므로 마지막에 루트 노드 출력

for _ in range(int(input())):
    n=int(input()) # 트리에 포함된 노드의 수
    preorder=list(map(int,input().split()))
    inorder=list(map(int,input().split()))
    traversal(preorder,inorder)
    print()