from uuid import uuid4
from collections import deque

from process import Process
from algorithm import *
from algorithm import FCFS, RR, SJF, SRTN, HRRN


priority = {
    'Ecore': 1,
    'Pcore': 2
}


class Processor:
    def __init__(self,
                 name=f"Processor {uuid4()}",
                 core="Ecore",
                 timeQuantum=2) -> None:
        self.name = name
        self.core = core
        self.priority = priority['Ecore']
        self.runtime = 0
        self.timeQuantum = timeQuantum

        self.readyQueue: deque[Process] = deque([])
        self.endProcessList: list[list[Process]] = []

    def __len__(self) -> int:
        return len(self.readyQueue)

    def __str__(self) -> str:
        text = (
            "[Processor Name: {0}]\n"
            "Core: {1}\n"
            "RunTime: {2}\n"
            "Process: {3}\n"
            "{4}"
        ).format(
            self.name,
            self.core,
            self.runtime,
            len(self.readyQueue),
            "\n".join(map(lambda process: "\t" + str(process), self.readyQueue))
        )
        return text

    def __getitem__(self, item: str | int) -> str | int:
        pass

    def isProcessing(self) -> bool:
        pass

    def processing(self) -> None:
        self.endProcessList.append(FCFS(self.readyQueue))
        self.endProcessList.append(RR(self.readyQueue, timeQuantum=self.timeQuantum))

    def add(self, process: Process) -> None:
        self.readyQueue.append(process)
