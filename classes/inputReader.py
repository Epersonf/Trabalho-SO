from classes.process import Process


class InputReader:

    def __init__(self, path):
        inputs = open(path, "r")
        self.processes = []
        for line in inputs.read().split("\n"):
            params = line.split(", ")
            params = list(map(int, list(params)))
            self.processes.append(Process(params[0], params[1], params[2], params[3], params[4]))

    def get_process_by_time(self, t: int):
        processes = []
        for process in self.processes:
            if process.arrivalTime == t:
                processes.append(process)
        return processes
