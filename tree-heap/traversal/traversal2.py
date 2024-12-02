# postorder, inorder -> 이진트리 구성 -> preorder로 출력
def traversal(postorder,inorder):
    assert(len(postorder) == len(inorder))
    if postorder: 
        root=postorder[-1]
        pos=inorder.index(root)
        print(root,end=" ")
        traversal(postorder[:pos],inorder[:pos])
        traversal(postorder[pos:-1],inorder[pos+1:]) # 마지막 원소를 제외하고 앞의 부분만 남기기


for _ in range(int(input())):
    n=int(input())
    postorder=list(map(int,input().split()))
    inorder=list(map(int,input().split()))
    traversal(postorder,inorder)
    print()