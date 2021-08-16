import random


class Process:

    def __init__(self, arrival_time: int, priority: int, service_time: int, size_mbytes: int, io_needed: int, pid: int):
        self.arrivalTime = arrival_time
        self.priority = priority
        self.serviceTime = service_time
        self.sizeMbytes = size_mbytes
        self.ioNeeded = io_needed

        self.processorTime = self.serviceTime
        self.previous_queue = -1
        self.quantum = -1

        self.PID = pid

    def join_cpu(self, quantum):
        self.quantum = quantum
        print("Processo", self.PID, "com quantum", self.quantum)

    def has_reached_cpu_time(self):
        self.quantum -= 1
        print("Processo", self.PID, "com quantum atualizado", self.quantum)
        return self.quantum <= 0

    def has_ended(self) -> bool:
        self.processorTime -= 1
        print("Processo", self.PID, "necessita de ", self.processorTime, "segundos de CPU")
        return self.processorTime <= 0

    def has_needed_io(self, available_disks) -> bool:
        return self.ioNeeded <= available_disks
