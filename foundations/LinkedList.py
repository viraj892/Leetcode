class Node:
    data = None
    next = None

    def __init__(self, data: int):
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        cur = self.head
        while i < index:
            if not cur.next:
                return None
            cur = cur.next
            i += 1

        return cur.next.val

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        i = 0
        cur = self.head
        while cur.next:
            cur = cur.next
            