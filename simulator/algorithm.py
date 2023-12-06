from process import Process
from processor import Processor


def first_come_first_served(process: Process) -> Process:
    AT = process.arrival_time
    BT = process.burst_time
    WT = process.waiting_time
    turnAround_time = 0

    return process


def FCFS(process: Process):
    first_come_first_served(process)


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
