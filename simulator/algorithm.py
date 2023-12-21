from collections import deque

from process import Process


def FCFS(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    timeStamps: dict[Process, dict[str, int]] = {
        process: {'START': 0, 'END': 0} for process in readyQueue
    }
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = BT + (0 if not endList else Pn['WT'])
        Pn['NTT'] = Pn['TT'] / BT

        timeStamps[Pn]['START'] = runtime
        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamps[Pn]['END'] = runtime
        endList.append(Pn)

    return endList


def first_come_first_served(readyQueue: deque[Process]) -> list[Process]:
    endList: list[Process] = FCFS(readyQueue)
    return endList


def RR(readyQueue: deque[Process], timeQuantum: int) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    copiedBT = {pn: pn['BT'] for pn in readyQueue}
    timeStamps: dict[Process, list[dict[str, int]]] = {
        process: [] for process in readyQueue
    }
    rotateQueue = deque()
    while readyQueue:
        while readyQueue:
            Pn = readyQueue.popleft()
            if Pn['AT'] <= runtime:
                rotateQueue.append(Pn)
            else:
                readyQueue.appendleft(Pn)
                break

        Pn = rotateQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

        timeStamp = {'START': 0, 'END': 0}

        if BT > timeQuantum:
            Pn['BT'] -= timeQuantum

            timeStamp['START'] = runtime
            timeStamp['END'] = timeStamp['START'] + timeQuantum

            rotateQueue.append(Pn)
            timeStamps[Pn].append(timeStamp)
        else:
            timeStamp['START'] = runtime
            timeStamp['END'] = runtime + BT
            timeStamps[Pn].append(timeStamp)

            wt = sum(map(lambda t: t['END'] - t['START'], timeStamps[Pn]))
            print(Pn, wt)

            Pn['BT'] = copiedBT[Pn]
            Pn['WT'] = wt + ((runtime - AT) if runtime >= AT else 0)
            Pn['TT'] = Pn['BT'] + (0 if not endList else Pn['WT'])
            Pn['NTT'] = Pn['TT'] / Pn['BT']

            endList.append(Pn)

        runtime += timeQuantum if BT > timeQuantum else BT

    endList.sort(key=lambda k: k['AT'])
    print(timeStamps)

    return endList


def round_robin(readyQueue: deque[Process], timeQuantum: int) -> list[Process]:
    endList: list[Process] = RR(readyQueue, timeQuantum)
    return endList


def SJF(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    shortestJob = []
    timeStamps: dict[Process, dict[str, int]] = {
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

        timeStamps[Pn]['START'] = runtime
        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamps[Pn]['END'] = runtime
        endList.append(Pn)

    while shortestJob:
        Pn = shortestJob.pop()
        AT, BT = Pn['AT'], Pn['BT']

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = Pn['WT'] + BT
        Pn['NTT'] = Pn['TT'] / BT

        timeStamps[Pn]['START'] = runtime
        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamps[Pn]['END'] = runtime
        endList.append(Pn)

    endList.sort(key=lambda k: k['AT'])

    return endList


def shortest_job_first(readyQueue: deque[Process]) -> list[Process]:
    endList: list[Process] = SJF(readyQueue)
    return endList


def SRTN(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

    return endList


def shortest_remaining_time_next(readyQueue: deque[Process]) -> list[Process]:
    endList: list[Process] = SRTN(readyQueue)
    return endList


def HRRN(readyQueue: deque[Process]) -> list[Process]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']

        responseRatio = (Pn['WT'] + BT) / BT

    return endList


def high_response_ratio_next(readyQueue: deque[Process]) -> list[Process]:
    endList: list[Process] = HRRN(readyQueue)
    return endList


if __name__ == "__main__":
    pass
