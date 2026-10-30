class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0


    def is_empty(self):
        return self.front_node is None


    def enqueue(self, item):
        node_baru = Node(item)


        if self.is_empty():
            self.front_node = node_baru
            self.rear_node = node_baru
        else:
            self.rear_node.next = node_baru
            self.rear_node = node_baru


        self.count += 1


    def dequeue(self):
        if self.is_empty():
            return None


        item = self.front_node.data
        self.front_node = self.front_node.next
        self.count -= 1


        if self.front_node is None:
            self.rear_node = None


        return item


    def front(self):
        if self.is_empty():
            return None
        return self.front_node.data


    def rear(self):
        if self.is_empty():
            return None
        return self.rear_node.data


    def size(self):
        return self.count


    def display(self):
        current = self.front_node
        hasil = []


        while current is not None:
            hasil.append(str(current.data))
            current = current.next


        print("Front ->", " -> ".join(hasil), "<- Rear")


# Pengujian
q = LinkedQueue()
q.enqueue("Surat-001")
q.enqueue("Surat-002")
q.enqueue("Surat-003")


q.display()
print("Diproses:", q.dequeue())
q.display()
print("Front:", q.front())
print("Rear:", q.rear())
print("Jumlah:", q.size())

