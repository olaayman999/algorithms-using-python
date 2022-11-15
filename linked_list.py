from locale import currency


class node:
    data=None
    next=None
    def __init__(self, data):
        self.data=data
        self.next=None
        
    def __repr__(self) :
        return(f"<Node data: {self.data} Next: {self.next} >")
        
        
class linked_list:

    
    def __init__(self):
        self.head=None

        
    def size(self):
        counter=0
        current=self.head
        while current:
            counter +=1
            current=current.next
        return counter
    
    def prepend(self, data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def __repr__(self):
        nodes =[]
        current=self.head
        while current:
            if current is self.head:
                nodes.append(" Head: %s " %current.data )
            elif current.next is None:
                nodes.append(" Tail: %s " %current.data )
            else:
                nodes.append(" %s " %current.data )
            current=current.next
        return '->'.join(nodes)
    
    
    def search(self,data):
        current=self.head
        while current:
            if current.data == data:
                return current
            else:
                current=current.next
        return(None)
            
    #1 2 3 4 8
    #0 1 2 3 4 
    def insert(self, data, index):
        if index ==0:
            self.prepend(data)
        elif index > 0 and index < self.size():
            n=node(data)
            current=self.head
            for i in range(index): #4
                if i ==index-1:
                    n.next=current.next
                    current.next=n
                else:
                    current=current.next
        else:
            print("out of range index")
    
    def pop(self):
        current=self.head
        next_node=current.next
        while current:
            if self.size() ==1:
                self.head=None
            elif next_node.next is None:
                current.next=None
            current=current.next
            next_node=next_node.next
        
    #0 1 2 3 4
    def delete(self, index):
        current=self.head
        next_node=current.next
        if index ==0 or index ==self.size()-1:
            self.pop()
        elif index <self.size():
            for i in range(index-1):
                current=current.next
                next_node=next_node.next 
            current.next=next_node.next 
            next_node.next=None
            next_node.data=None
            
    def append(self, data):
        current=self.head
        n=node(data)
        #3 4 20 5
        while current.next is not None:
            current=current.next
        current.next=n
        
