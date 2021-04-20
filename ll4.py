class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def nthnode(self,n):
        ref_ptr=self.head
        main_ptr=self.head
        count=0
        if self.head is not None:
            while(count<n):
                if ref_ptr is not None:
                    print("%d is greater than no. of nodes in list"%(n))
                    return
                ref_ptr=ref_ptr.next
                count+=1
        if ref_ptr is None :
            self.head=self.head.next
            print("Node no. % d from last is % d "% (n, main_ptr.data))
            if (self.head is not None):
                print("Node no. % d from last is % d "% (n, main_ptr.data))
                

