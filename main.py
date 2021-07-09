from classes.hardware import Hardware
from classes.inputReader import InputReader

inputReader = InputReader("./input.txt")
hardware = Hardware(2)

while True:
    processes = inputReader.get_process_by_time(hardware.time)
    for process in processes:
        hardware.add_process(process)
    hardware.clock()

