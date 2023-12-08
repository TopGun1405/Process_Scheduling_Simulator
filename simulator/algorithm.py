from collections import deque

from process import Process


def first_come_first_served(readyQueue: deque[Process], endList: list[Process]) -> None:

    runtime = 0
    while readyQueue:
        Pn = readyQueue.popleft()
        AT, BT = Pn.arrival_time, Pn.burst_time

        if not endList:
            Pn.turnAround_time = BT
        else:
            latest_TT = endList[-1].turnAround_time
            if latest_TT > AT:
                Pn.waiting_time = latest_TT - AT
            Pn.turnAround_time = runtime + BT

        Pn.normalized_turnAround_time = Pn.turnAround_time / BT
        runtime += BT
        endList.append(Pn)

    print("\n".join(map(str, endList)))
    return None


def FCFS(readyQueue: deque[Process], endList: list[Process]):
    first_come_first_served(readyQueue, endList)


def round_robin():
    pass


# def RR():
#     round_robin()


def shortest_job_first():
    pass


# def SJF():
#     shortest_job_first()


def shortest_remaining_time_next():
    pass


# def SRTN():
#     shortest_remaining_time_next()


def high_response_ratio_next():
    pass


# def HRRN():
#     high_response_ratio_next()


if __name__ == "__main__":
    pass
