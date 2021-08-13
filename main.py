from classes.hardware import Hardware
from classes.inputReader import InputReader
import time

inputReader = InputReader("./input.txt")
hardware = Hardware(2)                  #Criação do objeto para representar o despachante com quantum 2

while True:
    processes = inputReader.get_process_by_time(hardware.time)
    for process in processes:
        if not hardware.add_process(process):
            process.arrivalTime += 1

    hardware.update_cpu()

    hardware.print_state()
    hardware.clock()
    time.sleep(1)

