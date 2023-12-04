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


if __name__ == "__main__":
    main()
