class Process:

    def __init__(self, arrival_time: int, priority: int, service_time: int, size_mbytes: int, io_needed: int):
        self.arrivalTime = arrival_time
        self.priority = priority
        self.serviceTime = service_time
        self.sizeMbytes = size_mbytes
        self.ioNeeded = io_needed
