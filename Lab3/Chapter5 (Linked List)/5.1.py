class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def traversal_odd(self):
        odd = []
        current_node = self.head
        while current_node is not None:
            if current_node.value % 2 != 0:
                odd.append(current_node.value)
            current_node = current_node.next    
        return odd

    def traversal_even(self):
        even = []
        current_node = self.head
        while current_node is not None:
            if current_node.value % 2 == 0:
                even.append(current_node.value)
            current_node = current_node.next
        return even

    def __str__(self):
        if self.head is None:
            return "List is empty"
        
        current_node = self.head
        result = ""
        while current_node is not None:
            result += str(current_node.value)
            if current_node.next is not None:
                result += " -> "
            current_node = current_node.next
        return result

new_linked_list = SinglyLinkedList()
re_arrange = []

input_list = list(map(int, input("Enter the numbers list: ").split()))

for i in input_list:
    new_linked_list.append(i)

odd = new_linked_list.traversal_odd()
even = new_linked_list.traversal_even()

for i in even:
    re_arrange.append(i)

for i in odd:
    re_arrange.append(i)

print("Rearranged list:", re_arrange)
