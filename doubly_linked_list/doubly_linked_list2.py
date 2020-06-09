
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def __repr__(self):
        return f"value: {self.value} prev: {self.prev} {self.next}"


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def traverse(self):
        # grabs first node
        curr_node = self.head
        # keep going until you reach end of the list
        while curr_node != None:
            print(curr_node.value)
            # grab the node after the old current one
            curr_node = curr_node.next_node

    def get_size_list(self):
        # define incrementer
        count = 0
        # grabs first node
        curr_node = self.head
        # keep going until you reach end of the list
        while curr_node != None:
            count = count + 1
            # grab the node after the old current one. prevents inf loop.
            curr_node = curr_node.next_node
        return count
            

    
    def add_to_head(self, value):
        # define new node
        new_node = ListNode(value)
        # set next node equal to old head
        new_node.next_node = self.head
        # because its the head the prev point will point to nothing
        new_node.prev = None

        if self.head != None:
            self.head.prev = new_node
        # update head
        self.head = new_node
        
   
    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        self.length -= 1
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            return current_head.value
        current_head = self.head
        self.head = self.head.next
        self.head.prev = None
        return current_head.value
    def add_to_tail(self, value):
        # define new node
        new_node = Node(value)
        # point to nothing at the end of the list
        new_node.next = None
        # insert at head of list if empty list
        if self.head == None:
            new_node.prev = None
            self.head = new_node
            return
        # grab first node
        first_node = self.head

        #go to end of list
        while first_node.next:
            first_node = first_node.next
        # when at end, set next node equal to new node
        first_node.next = new_node
        new_node.prev = first_node
            
    def remove_from_tail(self):
        pass

   
    def move_to_front(self, ref_node, value):
        if self.head is None:
            print('this list is empty')
            return
        new_node = ListNode(value)

        new_node.prev = ref_node.prev
        ref_node.prev = new_node
        new_node.next = ref_node

        if new_node.prev != None:
            new_node.prev.next = new_node
        

   
    def move_to_end(self, ref_node, value):
        if self.head is None:
            print('the list is empty')
            return
        # define new node
        new_node = ListNode(value)
        new_node.next = ref_node
        ref_node.next = new_node
        new_node.prev = ref_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def delete(self, node):
        pass
        
    
    def get_max(self):
        pass
##
##    def __repr__(self):
##        return f"{self.head} {self.tail}"
    
node = ListNode(2,3)

double_list = DoublyLinkedList()
double_list.add_to_head(90)
double_list.add_to_head(90)
double_list.add_to_head(80)
double_list.add_to_head(70)

# traverse list
print('-'*50)
print('After insertion')
print('-'*50)
double_list.traverse()
double_list.get_size_list()

# define reference node
first_node = double_list.head

# insert before that node
double_list.move_to_end(first_node, 50)

# traverse list
print('-'*50)
print('After insertion Before')
print('-'*50)
double_list.traverse()

print(node)

print(double_list)
