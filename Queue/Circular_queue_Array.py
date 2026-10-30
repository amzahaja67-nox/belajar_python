
class CircularQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Kapasitas harus lebih dari 0")


        self.data = [None] * capacity
        self.capacity = capacity
        self.front_index = 0
        self.rear_index = -1
        self.count = 0


    def is_empty(self):
        return self.count == 0


    def is_full(self):
        return self.count == self.capacity


    def enqueue(self, item):
        if self.is_full():
            print("Queue penuh!")
            return False


        self.rear_index = (
            self.rear_index + 1
        ) % self.capacity


        self.data[self.rear_index] = item
        self.count += 1
        return True


    def dequeue(self):
        if self.is_empty():
            print("Queue kosong!")
            return None


        item = self.data[self.front_index]
        self.data[self.front_index] = None


        self.front_index = (
            self.front_index + 1
        ) % self.capacity


        self.count -= 1
        return item


    def front(self):
        if self.is_empty():
            return None
        return self.data[self.front_index]


    def rear(self):
        if self.is_empty():
            return None
        return self.data[self.rear_index]


    def size(self):
        return self.count


    def display(self):
        print("Isi array:", self.data)
        print("Front:", self.front())
        print("Rear:", self.rear())
        print("Jumlah:", self.size())




# Pengujian Circular Queue
cq = CircularQueue(5)


cq.enqueue("A")
cq.enqueue("B")
cq.enqueue("C")
cq.enqueue("D")
cq.enqueue("E")
cq.display()


print("Dikeluarkan:", cq.dequeue())
print("Dikeluarkan:", cq.dequeue())


cq.enqueue("F")
cq.enqueue("G")
cq.display()

