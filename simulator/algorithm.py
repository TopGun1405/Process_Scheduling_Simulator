from collections import deque

from process import Process


def first_come_first_served(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

        if not endList:
            Pn['TT'] = BT
        else:
            latest_TT = endList[-1]['TT']
            if latest_TT > AT:
                Pn['WT'] = latest_TT - AT
            else:
                runtime += AT - latest_TT
            Pn['TT'] = runtime + BT

        Pn['NTT'] = Pn['TT'] / BT
        runtime += BT
        endList.append(Pn)

    print("\n".join(map(str, endList)))
    return endList


def FCFS(readyQueue: deque[Process]) -> list[Process]:
    runtime = 0
    endList: list[Process] = first_come_first_served(readyQueue)
    return endList


def round_robin(readyQueue: deque[Process], timeQuantum: int) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

    return endList


def RR(readyQueue: deque[Process], timeQuantum: int) -> list[Process]:
    runtime = 0
    endList: list[Process] = round_robin(readyQueue, timeQuantum)
    return endList


def shortest_job_first(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

    return endList


def SJF(readyQueue: deque[Process]) -> list[Process]:
    runtime = 0
    endList: list[Process] = shortest_job_first(readyQueue)
    return endList


def shortest_remaining_time_next(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

    return endList


def SRTN(readyQueue: deque[Process]) -> list[Process]:
    runtime = 0
    endList: list[Process] = shortest_remaining_time_next(readyQueue)
    return endList


def high_response_ratio_next(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

    return endList


def HRRN(readyQueue: deque[Process]) -> list[Process]:
    runtime = 0
    endList: list[Process] = high_response_ratio_next(readyQueue)
    return endList


if __name__ == "__main__":
    pass
