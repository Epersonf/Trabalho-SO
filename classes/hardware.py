from classes.memory import Memory
from classes.process import Process

class Hardware:

    def __init__(self, quantum: int):
        self.time = -1
        self.cpus = [None] * 4
        self.disks: int = 4
        self.memory = Memory(16000)
        self.quantum = quantum
        self.realtimeQueue = []
        self.feedbackQueue = [[], [], []]

    def add_process(self, process: Process):
        if not self.memory.add_image(process):
            return
        if process.priority == 0:
            self.realtimeQueue.append(process)
        else:
            self.feedbackQueue[0].append(process)

    def clock(self):
        self.time += 1

    def print_state(self):
        print("--------------------")

        print("CPU STATE")
        print(self.cpus)

        print("\nREALTIME QUEUE")
        print(self.realtimeQueue)

        print("\nFEEDBACK QUEUE")
        for i in self.feedbackQueue:
            print(self.feedbackQueue)

        print("--------------------")

