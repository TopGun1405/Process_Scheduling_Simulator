from collections import deque

from process import Process


def first_come_first_served(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    timeStamp: dict[Process, dict[str, int]] = {
        process: {'START': 0, 'END': 0} for process in readyQueue
    }
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = BT + (0 if not endList else Pn['WT'])
        Pn['NTT'] = Pn['TT'] / BT

        timeStamp[Pn]['START'] = runtime
        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamp[Pn]['END'] = runtime
        endList.append(Pn)

    return endList


def FCFS(readyQueue: deque[Process]) -> list[Process]:
    endList: list[Process] = first_come_first_served(readyQueue)
    return endList


def round_robin(readyQueue: deque[Process], timeQuantum: int) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    copiedBT = {pn: pn['BT'] for pn in readyQueue}
    timeStamp: dict[Process, list[dict[str, int]]] = {
        process: [] for process in readyQueue
    }
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

        if BT > timeQuantum:
            Pn['BT'] -= timeQuantum
            readyQueue.append(Pn)
        else:
            Pn['BT'] = copiedBT[Pn]
            Pn['WT'] = (runtime - AT) if runtime >= AT else 0
            Pn['TT'] = Pn['BT'] + (0 if not endList else Pn['WT'])
            Pn['NTT'] = Pn['TT'] / Pn['BT']
            endList.append(Pn)

        runtime += timeQuantum if BT > timeQuantum else BT

    endList.sort(key=lambda k: k['AT'])

    return endList


def RR(readyQueue: deque[Process], timeQuantum: int) -> list[Process]:
    endList: list[Process] = round_robin(readyQueue, timeQuantum)
    return endList


def shortest_job_first(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    shortestJob = []
    timeStamp: dict[Process, dict[str, int]] = {
        process: {'START': 0, 'END': 0} for process in readyQueue
    }
    while readyQueue:

        while readyQueue:
            Pn = readyQueue.popleft()
            if Pn['AT'] <= runtime:
                shortestJob.append(Pn)
            else:
                readyQueue.appendleft(Pn)
                break

        shortestJob.sort(key=lambda k: k['BT'], reverse=True)
        Pn = shortestJob.pop()
        AT, BT = Pn['AT'], Pn['BT']

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = BT + (0 if not endList else Pn['WT'])
        Pn['NTT'] = Pn['TT'] / BT

        timeStamp[Pn]['START'] = runtime
        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamp[Pn]['END'] = runtime
        endList.append(Pn)

    while shortestJob:
        Pn = shortestJob.pop()
        AT, BT = Pn['AT'], Pn['BT']

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = Pn['WT'] + BT
        Pn['NTT'] = Pn['TT'] / BT

        timeStamp[Pn]['START'] = runtime
        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamp[Pn]['END'] = runtime
        endList.append(Pn)

    endList.sort(key=lambda k: k['AT'])

    return endList


def SJF(readyQueue: deque[Process]) -> list[Process]:
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
    endList: list[Process] = high_response_ratio_next(readyQueue)
    return endList


if __name__ == "__main__":
    pass
