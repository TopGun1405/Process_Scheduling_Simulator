from collections import deque

from process import Process
from processor import Processor


class Simulator:
    def __init__(self) -> None:
        self.currentState = None
        self.timeQuantum = 0
        self.allProcess = deque([])
        self.allProcessor = deque([Processor(name="Processor 1")])

    def __str__(self) -> str:
        text = "Process: {0}\nProcessor: {1}\n".format(
            ", ".join(map(str, self.allProcess)), ", ".join(map(str, self.allProcessor))
        )
        return text

    def changeToPcoreFirst(self) -> None:
        pass

    def changeToEcoreFirst(self) -> None:
        pass

    def addProcess(self, *args) -> None:
        if not args:
            newProcess = Process(
                name=f"P{len(self.allProcess) + 1}"
            )
            self.allProcess.append(newProcess)
            self.allProcessor[0].readyQueue.append(newProcess)
        else:
            for process in args:
                self.allProcess.append(process)
                self.allProcessor[0].readyQueue.append(process)

    def removeProcess(self, process: Process) -> None:
        self.allProcess.remove(process)

    def addProcessor(self) -> None:
        newProcessor = Processor(
            name=f"Processor {len(self.allProcessor) + 1}"
        )
        self.allProcessor.append(newProcessor)

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
        self.allProcessor[0].add(copyProcess.popleft())

    def startSimulate(self):
        self.allProcessor[0].processing()
