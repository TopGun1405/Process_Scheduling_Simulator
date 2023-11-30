from process import Process
from processor import Processor


class Simulator:
    def __init__(self) -> None:
        self.currentState = None
        self.timeQuantum = 0
        self.allProcess = []
        self.allProcessor = [Processor(name="Processor 1")]

    def __str__(self) -> str:
        text = "Process: {0}\nProcessor: {1}\n".format(
            ", ".join(map(str, self.allProcess)), ", ".join(map(str, self.allProcessor))
        )
        return text

    def changeToPcoreFirst(self) -> None:
        pass

    def changeToEcoreFirst(self) -> None:
        pass

    def addProcess(self) -> None:
        newProcess = Process(
            name=f"P{len(self.allProcess) + 1}"
        )
        self.allProcess.append(newProcess)

    def addProcessor(self) -> None:
        newProcessor = Processor(
            name=f"Processor {len(self.allProcessor) + 1}"
        )
        self.allProcessor.append(newProcessor)
