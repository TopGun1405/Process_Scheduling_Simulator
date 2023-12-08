from process import Process
from processor import Processor
from simulator import Simulator


def main():
    print("=" * 100)
    print(
        "AT: Arrival Time, "
        "BT: Burst Time, "
        "WT: Waiting Time, "
        "TT: TurnAround Time, "
        "NTT: Normalized TT"
    )
    print("=" * 100)

    # processor = Processor()
    # for i in range(1, 10):
    #     p = Process(f"P{i}", i, i * 2)
    #     processor.readyQueue.append(p)
    #     print(p)

    newSimulator = Simulator()
    p1 = Process(name="P1", arrival_time=0, burst_time=3)
    p2 = Process(name="P2", arrival_time=1, burst_time=7)
    p3 = Process(name="P3", arrival_time=3, burst_time=2)
    p4 = Process(name="P4", arrival_time=5, burst_time=5)
    p5 = Process(name="P5", arrival_time=6, burst_time=3)
    newSimulator.addProcess(p1, p2, p3, p4, p5)
    newSimulator.startSimulate()


if __name__ == "__main__":
    main()
