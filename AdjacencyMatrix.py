class AdjMatrix:
    def __init__(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([0]*size)
        self.size = size

    def add_edge(self, v1, v2):
        if v1 != v2 and not self.is_edge(v1, v2):
            self.matrix[v1][v2] = 1
            self.matrix[v2][v1] = -1

    def is_edge(self, v1, v2):
        if self.matrix[v1][v2] == 1:
            return True
        return False

    def get_order(self):
        return self.size

    def get_successors(self, v):
        successors = []
        for i in range(self.size):
            if self.matrix[v][i] == 1:
                successors.append(i)
        return successors

    def print(self):
        for row in self.matrix:
            for elem in row:
                print(elem, end=" ")
            print()
