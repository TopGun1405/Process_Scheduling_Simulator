from collections import deque

from algorithm import FCFS, RR, SJF, SRTN, HRRN


priority = {
    0: "Ecore",
    1: "Pcore"
}


class Processor:
    def __init__(self, name="Processor N") -> None:
        self.name = name
        self.priority = priority[0]

        self.readyQueue = deque([])
        self.endProcessList = []

    def __len__(self) -> int:
        return len(self.readyQueue)

    def __str__(self) -> str:
        text = (
            "[Processor Name: {0}] | "
            "Priority: {1}"
        ).format(
            self.name,
            self.priority
        )
        return text

    def __getitem__(self, item) -> None:
        pass

    def isProcessing(self) -> bool:
        pass

    def processing(self) -> None:
        self.endProcessList.append(FCFS(self.readyQueue))

    def add(self, process) -> None:
        self.readyQueue.append(process)
