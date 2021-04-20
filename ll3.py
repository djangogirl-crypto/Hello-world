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
    def ntLastNode(self,n):
        ref_ptr=self.head
        main_ptr=self.head
        count=0
        if self.head is not None:
            while count<n:
                if ref_ptr is None:
                    print("% d is greater than the no.pf nodes in list " %(n))
                    return

                ref_ptr=ref_ptr.next
                count+=1
        if ref_ptr is None:
            self.head =self.head.next
            if self.head is not None:
                print(main_ptr.data)
        else:
            while(ref_ptr is not None):
                main_ptr =main_ptr.next
                ref_ptr = ref_ptr.next
            print(main_ptr.data)
llist=LinkedList()
llist.push(9)
llist.push(10)
llist.push(34)
llist.push(77)
llist.ntLastNode(4)