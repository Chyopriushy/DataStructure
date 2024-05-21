class QueueCircular:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_, self.rear_ = 0, 0


    def size(self):
        if self.front_ > self.rear_:
            return (self.rear_ - self.front_) + self.capacity
        return self.rear_ - self.front_


    def empty(self):
        return self.front_ == self.rear_

    def full(self):
        return self.front_ == ((self.rear_ + 1) % self.capacity)

    def enqueue(self, data):
        if not self.full():
            self.rear_ = ((self.rear_ + 1) % self.capacity)
            self.arr[self.rear_] = data

    def dequeue(self):
        if not self.empty():
            self.front_ = ((self.front_ + 1) % self.capacity)
            return self.arr[self.front_]


    def front(self):
        if self.empty():
            return
        return self.arr[(self.front_ + 1) % self.capacity]

    def rear(self):
        if self.empty():
            return
        return self.arr[self.rear_ % self.capacity]

    def __str__(self):
        ret = []
        cnt = self.size()
        curr_idx = self.front_ + 1
        while cnt:
            if curr_idx >= self.capacity:
                curr_idx %= self.capacity
            ret.append(self.arr[curr_idx])
            curr_idx += 1
            cnt -= 1
        ret = ", ".join(map(str, ret))
        return f"[{ret}]"

if __name__ == "__main__":
    SIZE = 8
    queue = QueueCircular(SIZE)
    print(f"queue = {queue}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "A"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "B"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()

    data = "C"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "D"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "E"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "F"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "G"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "H"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "I"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()

    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    print(f">> queue.deueue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()
    data = "J"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.rear_}")
    print(f">> queue.data:{queue.front(), queue.rear()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size = {queue.size()}")
    print()