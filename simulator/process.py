from uuid import uuid1


class Process:
    def __init__(self,
                 name=f"P{uuid1()}",
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
        }
        try:
            return info[key]

        except KeyError:
            message = (
                "[KeyError]\n"
                "Process Name   : name\n"
                "Arrival Time   : AT\n"
                "Burst Time     : BT\n"
                "Waiting Time   : WT\n"
                "TurnAround Time: TT\n"
                "Normalized TT  : NTT"
            )
            return message

    def __setitem__(self,
                    key: str | int,
                    value: str | int | float) -> None:
        names = {
            'name': 'name',
            'AT': 'arrival_time',
            'BT': 'burst_time',
            'WT': 'waiting_time',
            'TT': 'turnAround_time',
            'NTT': 'normalized_turnAround_time',
        }
        try:
            self.__setattr__(names[key], value)

        except KeyError:
            message = (
                "[KeyError]\n"
                "Process Name   : name\n"
                "Arrival Time   : AT\n"
                "Burst Time     : BT\n"
                "Waiting Time   : WT\n"
                "TurnAround Time: TT\n"
                "Normalized TT  : NTT"
            )
            print(message)
