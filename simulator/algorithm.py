from collections import deque

from process import Process


def FCFS(readyQueue: deque[Process]) -> tuple[list, dict]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    timeStamps: dict[Process, dict[str, int]] = {
        process: {'START': 0, 'END': 0} for process in readyQueue
    }
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']
        timeStamps[Pn]['START'] = runtime

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = BT + (0 if not endList else Pn['WT'])
        Pn['NTT'] = Pn['TT'] / BT

        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamps[Pn]['END'] = runtime
        endList.append(Pn)

    return endList, timeStamps


def RR(readyQueue: deque[Process], timeQuantum: int) -> tuple[list, dict]:

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
        timeStamp = {'START': runtime, 'END': 0}

        if BT > timeQuantum:
            Pn['BT'] -= timeQuantum

            timeStamp['END'] = timeStamp['START'] + timeQuantum
            rotateQueue.append(Pn)
            timeStamps[Pn].append(timeStamp)
        else:
            wt = sum(map(lambda t: t['END'] - t['START'], timeStamps[Pn]))
            print(Pn, wt)

            Pn['BT'] = copiedBT[Pn]
            Pn['WT'] = wt + ((runtime - AT) if runtime >= AT else 0)
            Pn['TT'] = Pn['BT'] + (0 if not endList else Pn['WT'])
            Pn['NTT'] = Pn['TT'] / Pn['BT']

            timeStamp['END'] = runtime + BT
            endList.append(Pn)
            timeStamps[Pn].append(timeStamp)

        runtime += timeQuantum if BT > timeQuantum else BT

    endList.sort(key=lambda k: k['AT'])
    print(timeStamps)

    return endList, timeStamps


def SJF(readyQueue: deque[Process]) -> tuple[list, dict]:

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
        timeStamps[Pn]['START'] = runtime

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = BT + (0 if not endList else Pn['WT'])
        Pn['NTT'] = Pn['TT'] / BT

        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamps[Pn]['END'] = runtime
        endList.append(Pn)

    while shortestJob:
        Pn = shortestJob.pop()
        AT, BT = Pn['AT'], Pn['BT']
        timeStamps[Pn]['START'] = runtime

        Pn['WT'] = (runtime - AT) if runtime >= AT else 0
        Pn['TT'] = Pn['WT'] + BT
        Pn['NTT'] = Pn['TT'] / BT

        runtime += BT + (0 if runtime >= AT else AT - runtime)
        timeStamps[Pn]['END'] = runtime
        endList.append(Pn)

    endList.sort(key=lambda k: k['AT'])

    return endList, timeStamps


def SRTN(readyQueue: deque[Process]) -> tuple[list, dict]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    timeStamps: dict[Process, list[dict[str, int]]] = {
        process: [] for process in readyQueue
    }
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']
        timeStamp = {'START': runtime, 'END': 0}

    return endList, timeStamps


def HRRN(readyQueue: deque[Process]) -> tuple[list, dict]:

    runtime = 0
    endList: list[Process] = []

    readyQueue = deque(sorted(readyQueue, key=lambda k: k['AT']))
    timeStamps: dict[Process, list[dict[str, int]]] = {
        process: [] for process in readyQueue
    }
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn['AT'], Pn['BT']
        timeStamp = {'START': runtime, 'END': 0}

        responseRatio = (Pn['WT'] + BT) / BT

    return endList, timeStamps


if __name__ == "__main__":
    pass
