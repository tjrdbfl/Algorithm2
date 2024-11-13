def traversal(preorder,inorder):
    assert(len(preorder)==len(inorder))
    if preorder:
        root=preorder[0]
        pos=inorder.index(root)
        traversal(preorder[1:pos+1],inorder[:pos])
        traversal(preorder[pos+1:],inorder[pos+1:])
        print(root,end=" ") 

for _ in range(int(input())):
    n=int(input())
    preorder=list(map(int,input().split()))
    inorder=list(map(int,input().split()))
    traversal(preorder,inorder)
    print()
