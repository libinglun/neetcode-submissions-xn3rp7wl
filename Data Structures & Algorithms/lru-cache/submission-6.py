class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # map key to node
        self.cache = {}
        self.capacity = capacity
        # dummy nodes to reduce margin logics
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # remove node
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

            # move node to the end
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node

            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache:
            node = Node(key, value)
            print("cache size: ", len(self.cache), self.capacity)
            if len(self.cache) >= self.capacity:
                # out of capacity, remove least used node
                next = self.head.next
                print("key value pair to pop: ", next.key, next.val)
                self.cache.pop(next.key)
                self.head.next = next.next
                next.next.prev = self.head

            # move node to the end
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node
            self.cache[key] = node
        else:
            node = self.cache[key]
            # remove node
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

            # move node to the end
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node

            node.val = value




            



        
