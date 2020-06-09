"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
    def __repr__(self):
        return f"\n value: {self.value} \n prev: {self.prev} \n next: {self.next}"


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
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
        return current_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # define new node
        new_node = ListNode(value, None, None)
        self.length += 1
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

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass

    def traverse(self):
        # grabs first node
        curr_node = self.head
        # keep going until you reach end of the list
        while curr_node != None:
            print(curr_node.value)
            # grab the node after the old current one
            curr_node = curr_node.next


node = ListNode(2,3,5)
print(node)


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

print('-'*50)
print('After Remove from head')
print('-'*50)
double_list.remove_from_head()
double_list.remove_from_head()

double_list.traverse()

# Add to tail
double_list.add_to_tail(77)
double_list.add_to_tail(22)


# traverse list
print('-'*50)
print('After insertion - Tail')
print('-'*50)
double_list.traverse()

# Remove from tail
double_list.remove_from_tail()


# traverse list
print('-'*50)
print('After Removal - Tail')
print('-'*50)
double_list.traverse()
