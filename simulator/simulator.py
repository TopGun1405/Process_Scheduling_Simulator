from collections import deque

from process import Process
from processor import Processor


config = {
    'MAX_PROCESS': 15,
    'MAX_PROCESSOR': 4
}


class Simulator:
    def __init__(self) -> None:
        self.currentState = None
        self.timeQuantum = 2
        self.allProcess = deque([])
        self.allProcessor = deque([Processor(name="Processor 1")])

    def __str__(self) -> str:
        text = (
            "Process: {0}\n"
            "{1}\n"
            "Processor: {2}\n"
            "{3}\n"
            "timeQuantum: {4}\n"
            "maximum Process, Processor: {5}, {6}"
        ).format(
            len(self.allProcess),
            ", ".join(map(lambda process: "\t" + str(process), self.allProcess)),
            len(self.allProcessor),
            ", ".join(map(lambda processor: "\t" + str(processor), self.allProcessor)),
            self.timeQuantum,
            config['MAX_PROCESS'], config['MAX_PROCESSOR']
        )
        return text

    def changeToPcoreFirst(self) -> None:
        pass

    def changeToEcoreFirst(self) -> None:
        pass

    def addProcess(self, *args: Process) -> None:
        if not args:
            newProcess = Process(
                name=f"P{len(self.allProcess) + 1}"
            )
            self.allProcess.append(newProcess)

            self.allProcessor[0].readyQueue.append(newProcess)
        else:
            for process in args:
                self.allProcess.append(process)
                ####
                self.allProcessor[0].readyQueue.append(process)

    def removeProcess(self, process: Process) -> None:
        self.allProcess.remove(process)

    def addProcessor(self, *args: Processor) -> None:
        if not args:
            newProcessor = Processor(
                name=f"Processor {len(self.allProcessor) + 1}"
            )
            self.allProcessor.append(newProcessor)
        else:
            for processor in args:
                self.allProcessor.append(processor)

    def addProcessToProcessor(self) -> None:
        copyProcess = self.allProcess[:]
        i = 0
        # while not copyProcess:
        #     for processor in self.allProcessor:
        #         if not processor.finishedProcessList:
        #             processor.readyQueue.append(copyProcess.popleft())
        #             break
        #         else:
        #             pass
        #         pass
        #     if not self.allProcessor[i].finishedProcessList:
        #         pass
        self.allProcessor[0].addProcess(copyProcess.popleft())

    def startSimulate(self) -> None:
        self.allProcessor[0].processing()
