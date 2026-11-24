# Q. 1 CPU Process Scheduling Using Priority Queue
# An operating system manages multiple processes waiting for CPU execution. Each process is assigned a priority. The CPU executes the process with the highest priority first.
# Develop a Python program to implement a Priority Queue for CPU Process Scheduling.

# Priority Levels
    # • Priority 1 – System Process (Highest Priority)
    # • Priority 2 – Interactive Process
    # • Priority 3 – Background Process
    # • Priority 4 – Low-Priority Process

# Implement the following functions:
    # 1. Add Process: Insert a process with Process ID, Process Name and Priority (enqueue)
    # 2. Execute Process: Remove the process with the highest priority (dequeue)
    # 3. View Next Process: Display the next process to be executed (display_next)
    # 4. Display Processes: Display all pending processes in priority order (display_all)
    # 5. Count Processes: Display the total number of pending processes (count)


class PriorityQueue:
    def __init__(self):
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