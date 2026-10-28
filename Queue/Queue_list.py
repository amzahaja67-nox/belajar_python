class Queue:
    def __init__(self):
        self.data = []


    def enqueue(self, item):
        self.data.append(item)


    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.pop(0)


    def front(self):
        if self.is_empty():
            return None
        return self.data[0]


    def rear(self):
        if self.is_empty():
            return None
        return self.data[-1]


    def is_empty(self):
        return len(self.data) == 0


    def size(self):
        return len(self.data)


    def display(self):
        print("Front ->", self.data, "<- Rear")




# Pengujian
q = Queue()


q.enqueue("Tiket-001")
q.enqueue("Tiket-002")
q.enqueue("Tiket-003")


q.display()
print("Tiket terdepan:", q.front())
print("Tiket paling belakang:", q.rear())
print("Tiket dilayani:", q.dequeue())


q.display()
print("Jumlah antrean:", q.size())