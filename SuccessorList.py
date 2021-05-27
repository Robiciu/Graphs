class SucList:
    def __init__(self, size):
        self.list = []
        self.size = size
        for i in range(size):
            self.list.append([])

    def add_edge(self, v1, v2):
        self.list[v1].append(v2)

    def is_edge(self, v1, v2):
        for suc in self.list[v1]:
            if suc == v2:
                return True
        return False

    def get_order(self):
        return self.size

    def get_successors(self, v):
        successors = []
        for suc in self.list[v]:
            successors.append(suc)
        return successors

    def print(self):
        for v in range(self.size):
            print(v, end=" -> ")
            for suc in self.list[v]:
                print(suc, end=" ")
            print()
