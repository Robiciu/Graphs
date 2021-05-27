class EdgeList:
    def __init__(self, size):
        self.list = []
        self.size = size

    def add_edge(self, v1, v2):
        self.list.append((v1, v2))

    def is_edge(self, v1, v2):
        for i in self.list:
            if i == (v1, v2):
                return True
        return False

    def get_order(self):
        return self.size

    def get_successors(self, v):
        successors = []
        for pair in self.list:
            if pair[0] == v:
                successors.append(pair[1])
        return successors

    def print(self):
        for pair in self.list:
            print(pair)
