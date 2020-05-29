class node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None
class Double_Linked_list:
    def __init__(self):
        self.nil = node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil
    def insert(self,key):
        new = node(key)
        new.next = self.nil.next
        self.nil.next.prev = new
        self.nil.next = new
        new.prev = self.nil
    def search(self,key):
        cur = self.nil.next
        while cur.key != key and cur != self.nil:
            cur = cur.next
        return cur
    def deletenode(self,Node):
        if Node == self.nil:
            return
        Node.prev.next = Node.next
        Node.next.prev = Node.prev
    def deleteFirst(self):
        self.deletenode(self.nil.next)
    def deleteLast(self):
        self.deletenode(self.nil.prev)
N = int(input())
d = Double_Linked_list()
for _ in range(N):
    s,n = input().split()
    n = int(n)
    if s == "insert":
        d.insert(n)
    elif s == "deleteFirst":
        d.deleteFirst()
    elif s == "deleteLast":
        d.deleteLast()
    else:
        cur = d.search(n)
        d.deletenode(cur)
ans = []
cur = d.nil.next
while cur != d.nil:
    ans.append(str(cur.key))
    cur = cur.next
print(" ".join(ans))