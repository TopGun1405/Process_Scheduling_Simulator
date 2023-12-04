priority = {
    0: "Ecore",
    1: "Pcore"
}


class Processor:
    def __init__(self, name="Processor N"):
        self.readyQueue = []
        self.name = name
        self.priority = priority[0]

    def __len__(self) -> int:
        return len(self.readyQueue)

    def __str__(self) -> str:
        text = (
            "[Processor Name: {0}] | "
            "Priority: {1}"
        ).format(
            self.name,
            self.priority
        )
        return text

    def __getitem__(self, item):
        pass

    def processing(self):
        pass

    def add(self, process):
        self.readyQueue.append(process)