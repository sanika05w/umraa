class PriorityQueue:
    def _init_(self):
        self.queue = []
        

    # Add Process
    def enqueue(self, pid, name, priority):
        self.queue.append([pid, name, priority])

    # Execute Process
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        curr = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][2] < self.queue[curr][2]:
                curr = i
        print("Executed:", self.queue.pop(curr))

    # View Next Process
    def display_next(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        curr = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][2] < self.queue[curr][2]:
                curr = i
        print("Next Process:", self.queue[curr])

    # Display All Processes
    def display_all(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return
        curr = sorted(self.queue, key=lambda x: x[2])
        for process in curr:
            print(process)

    # Count Processes
    def count(self):
        print("Total Processes:", len(self.queue))


pq = PriorityQueue()

pq.enqueue(101, "Chrome", 3)
pq.enqueue(102, "System", 1)
pq.enqueue(103, "Editor", 2)
pq.enqueue(104, "Background", 4)

pq.display_next()
pq.display_all()
pq.count()
pq.dequeue()