class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class Graph:
    def __init__(self: str, sequence: list):
        self._matrix = sequence[:]
        self.nodes = []

    def _construct(self, sequence):
        pass

class DiagnosticsReport(object):
    def __init__(self, raw):
        self._raw = raw
        self.cols = None
        self.rows = None
        self.deserialize()

    def deserialize(self):
        self.rows = [list(row) for row in self._raw.splitlines()]
        self.cols = list(zip(*self.rows))

    def kiss(self):
        return f"Rows: {self.rows[0]}\nCols: {self.cols[0]}"




def main():
    with open('./input.txt', 'r') as fio:
        raw = fio.read()
    report = DiagnosticsReport(raw)
    print(report.kiss())

if __name__ == "__main__":
    main()

