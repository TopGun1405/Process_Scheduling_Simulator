from uuid import uuid4
from collections import deque

from process import Process
from algorithm import *
from algorithm import FCFS, RR, SJF, SRTN, HRRN


velocity = {
    'Ecore': 1,
    'Pcore': 2
}

attr_names = {
    'name': "name",
    'core': "core",
    'timeQuantum': "timeQuantum",
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
            'FCFS': [], 'RR': [], 'SJF': [], 'SRTN': [], 'HRRN': []
        }
        self.timeStamps: dict[str, list[dict | list]] = {
            'FCFS': [], 'RR': [], 'SJF': [], 'SRTN': [], 'HRRN': []
        }

    def __len__(self) -> int:
        return len(self.readyQueue)

    def __str__(self) -> str:
        text = (
            "[Processor Name: {0}]\n"
            "Core: {1}, RunTime: {2}\n"
            "Process: {3}\n"
            "{4}"
        ).format(
            self.name,
            self.core, self.runtime,
            len(self.readyQueue),
            ", ".join(map(lambda process: "\t" + str(process), self.readyQueue))
        )
        return text

    def __getitem__(self, key: str) -> str | int:
        try:
            return self.__getattribute__(attr_names[key])
        except KeyError:
            message = (
                "[KeyError]\n"
                "key list: [name, core, timeQuantum]"
            )
            return message

    def __setitem__(self,
                    key: str,
                    value: str | int) -> None:
        try:
            self.__setattr__(attr_names[key], value)
        except KeyError:
            message = (
                "[KeyError]\n"
                "key list: [name, core, timeQuantum]"
            )
            print(message)

    def processing(self) -> None:
        print("=" * 100)
        print("FCFS")
        self.endProcessList['FCFS'], self.timeStamps['FCFS'] = FCFS(self.readyQueue)
        print("\n".join(map(lambda p: "\t" + str(p), self.endProcessList['FCFS'])))

        print("=" * 100)
        print("RR")
        self.endProcessList['RR'], self.timeStamps['RR'] = RR(self.readyQueue, self.timeQuantum)
        print("\n".join(map(lambda p: "\t" + str(p), self.endProcessList['RR'])))

        print("=" * 100)
        print("SJF")
        self.endProcessList['SJF'], self.timeStamps['SJF'] = SJF(self.readyQueue)
        print("\n".join(map(lambda p: "\t" + str(p), self.endProcessList['SJF'])))

        # print("=" * 100)
        # print("SRTN")
        # self.endProcessList['SRTN'], self.timeStamps['SRTN'] = SRTN(self.readyQueue)

        # print("=" * 100)
        # print("HRRN")
        # self.endProcessList['HRRN'], self.timeStamps['HRRN'] = HRRN(self.readyQueue)

    def addProcess(self, process: Process) -> None:
        self.readyQueue.append(process)
