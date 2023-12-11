from uuid import uuid4
from collections import deque

from process import Process
from algorithm import *
from algorithm import FCFS, RR, SJF, SRTN, HRRN


velocity = {
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
        self.timeQuantum = timeQuantum
        self.velocity = velocity[self.core]
        self.runtime = 0

        self.readyQueue: deque[Process] = deque([])
        self.endProcessList: dict[str, list[Process]] = {
            'FCFS': [],
            'RR': [],
            'SJF': [],
            'SRTN': [],
            'HRRN': []
        }

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

    def __getitem__(self, key: str | int) -> str | int:
        info = {
            'name': self.name,
            'core': self.core,
            'runtime': self.runtime,
            'timeQuantum': self.timeQuantum,

            0: self.name,
            1: self.core,
            2: self.runtime,
            3: self.timeQuantum
        }
        try:
            return info[key]
        except KeyError:
            pass

    def isProcessing(self) -> bool:
        pass

    def processing(self) -> None:
        print()
        self.endProcessList['FCFS'] = FCFS(self.readyQueue)
        self.endProcessList['RR'] = RR(self.readyQueue, self.timeQuantum)
        self.endProcessList['SJF'] = SJF(self.readyQueue)
        self.endProcessList['SRTN'] = SRTN(self.readyQueue)
        self.endProcessList['HRRN'] = HRRN(self.readyQueue)

    def addProcess(self, process: Process) -> None:
        self.readyQueue.append(process)
