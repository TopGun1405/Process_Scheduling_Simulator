class Processor:
    def __init__(self, name="Processor N"):
        self.readyQueue = []
        self.name = name

    def __len__(self):
        pass

    def __str__(self) -> str:
        text = (
            "[Processor Name: {0}]"
        ).format(
            self.name
        )
        return text

    def __getitem__(self, item):
        pass

    def processing(self):
        pass

    def add(self, process):
        self.readyQueue.append(process)
