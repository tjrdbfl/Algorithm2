# 문자열 탐색
class TrieNode:
    def __init__(self):
        self.children={} # 자식 노드 딕셔너리 : key=문자, value=자식노드
        self.terminal=False

    def insert(self,string):
        if not string:
            self.terminal=True
        else:
            char=string[0] # 첫 번째 문자
            if char not in self.children:
                self.chilren[char]=TrieNode()
            self.children[char].insert(string[1:]) # 이후 문자열 추가 
    
    def find(self,string):
        if not string:
            return self
        else:
            char=string[0]
            if char not in self.children:
                return None
            return self.children[char].find(string[1:])

S=["BE","BET","BUS","TEA","TEN"]
root=TrieNode()
for s in S:
    root.insert(s)
for s in S+["BUT","TE"]:
    node=root.find(s)
    if node:
        if node.terminal:
            print(s+" exists.")
        else:
            print(s+" does not exists. But, it is a prefix")
    else:
        print(s+" does not exists.")


# {
#     "B": {  # Root node has children "B" and "T"
#         "E": {  # "BE"
#             "terminal": True,
#             "children": {
#                 "T": {  # "BET"
#                     "terminal": True,
#                     "children": {}
#                 }
#             }
#         },
#         "U": {  # "BUS"
#             "terminal": False,
#             "children": {
#                 "S": {
#                     "terminal": True,
#                     "children": {}
#                 }
#             }
#         }
#     },
#     "T": {  # "T"
#         "E": {  # "TE"
#             "terminal": False,
#             "children": {
#                 "A": {  # "TEA"
#                     "terminal": True,
#                     "children": {}
#                 },
#                 "N": {  # "TEN"
#                     "terminal": True,
#                     "children": {}
#                 }
#             }
#         }
#     }
# }
