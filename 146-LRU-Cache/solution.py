class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        del node
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.capacity = capacity
        self.list = List()
        self.dict = {}

    def _insert(self, key, value):
        node = Node(key, value)
        self.list.insert(node)
        self.dict[key] = node

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self._insert(key, val)
            return val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            self.list.delete(self.dict[key])
        elif self.capacity == len(self.dict):
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)
        self._insert(key, value)