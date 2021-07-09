class Memory:

    def __init__(self, max_memory: int):
        self.maxMemory = max_memory
        self.loadedProcess = []

    def add_image(self, process) -> bool:
        if self.calculateOccupiedMemory() < self.maxMemory:
            self.loadedProcess.append(process)
            return True
        return False

    def remove_image(self, process):
        self.loadedProcess.remove(process)

    def is_in_memory(self, process) -> bool:
        return process in self.loadedProcess

    def calculate_occupied_memory(self):
        sumTotal = 0
        for process in self.loadedProcess:
            sumTotal += process.sizeMbytes
        return sumTotal
