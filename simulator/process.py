from uuid import uuid4


class Process:
    def __init__(self,
                 name=f"P{uuid4()}",
                 arrival_time=0,
                 burst_time=0) -> None:
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnAround_time = 0
        self.normalized_turnAround_time = 0

    def __str__(self) -> str:
        text = (
            "[Process Name: {0}] | "
            "AT: {1}, "
            "BT: {2}, "
            "WT: {3}, "
            "TT: {4}, "
            "NTT: {5}"
        ).format(
            self.name,
            self.arrival_time,
            self.burst_time,
            self.waiting_time,
            self.turnAround_time,
            self.normalized_turnAround_time
        )
        return text

    def __getitem__(self, key: str | int) -> str | int:
        info = {
            'name': self.name,
            'AT': self.arrival_time,
            'BT': self.burst_time,
            'WT': self.waiting_time,
            'TT': self.turnAround_time,
            'NTT': self.normalized_turnAround_time,

            0: self.name,
            1: self.arrival_time,
            2: self.burst_time,
            3: self.waiting_time,
            4: self.turnAround_time,
            5: self.normalized_turnAround_time
        }
        try:
            return info[key]
        except KeyError:
            message = (
                "[KeyError]\n"
                "Process Name   : (name or 0)\n"
                "Arrival Time   : (AT or 1)\n"
                "Burst Time     : (BT or 2)\n"
                "Waiting Time   : (WT or 3)\n"
                "TurnAround Time: (TT or 4)\n"
                "Normalized TT  : (NTT or 5)"
            )
            return message
