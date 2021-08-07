import sys


class Heap:
    def __init__(self, maxsize, comparator=lambda more_priority, less_priority: more_priority > less_priority):
        self.nodes = [None] * (maxsize + 1)
        self.nodes[0] = 0
        self.comparator = comparator
        self.size = 0
        self.maxsize = maxsize

        if not callable(self.comparator):
            raise ValueError('Comparator is not a function!')

    def left_child(self, index):
        child_index = index * 2
        return self.__child(child_index)

    def right_child(self, index):
        child_index = index * 2 + 1
        return self.__child(child_index)

    def is_node_exist(self, index):
        return index < self.maxsize and self.nodes[index] is not None

    def pop(self):
        if self.size < 1:
            return None
        root = self.nodes[1]
        self.nodes[1] = self.nodes[self.size]
        self.nodes[self.size] = None
        self.size -= 1
        self.sift_down(1)
        return root

    def push(self, item):
        if self.size >= self.maxsize:
            return False
        self.size += 1
        self.nodes[self.size] = item
        self.sift_up(self.size)
        return self.size

    def sift_up(self, index):
        while index // 2 > 0:
            parent_index = index // 2
            if self.__is_first_node_priority_higher(index, parent_index):
                self.__swap(index, parent_index)
            index = parent_index

    def sift_down(self, index):
        while index * 2 <= self.size:
            child, child_index = self.__most_priority_child(index)
            if self.__is_first_node_priority_higher(child_index, index):
                self.__swap(index, child_index)
            index = child_index

    def __swap(self, index_from, index_to):
        self.nodes[index_from], self.nodes[index_to] = self.nodes[index_to], self.nodes[index_from]

    def __child(self, index):
        if self.is_node_exist(index):
            return self.nodes[index], index
        return None, index

    def __most_priority_child(self, index):
        left_child, left_child_index = self.left_child(index)
        right_child, right_child_index = self.right_child(index)

        if right_child is None:
            return left_child, left_child_index

        if self.__is_first_node_priority_higher(left_child_index, right_child_index):
            return left_child, left_child_index
        else:
            return right_child, right_child_index

    def __is_first_node_priority_higher(self, first_node_index, second_node_index):
        return self.comparator(self.nodes[first_node_index], self.nodes[second_node_index])


def is_first_student_better(student1, student2, name_key=0, tasks_key=1, penalty_key=2):
    if student1[tasks_key] == student2[tasks_key]:
        if student1[penalty_key] == student2[penalty_key]:
            return student1[name_key] < student2[name_key]
        return student1[penalty_key] < student2[penalty_key]
    return student1[tasks_key] > student2[tasks_key]


def print_score(name_key=0, tasks_key=1, penalty_key=2):
    students_number = int(sys.stdin.readline().strip())
    heap = Heap(students_number, comparator=is_first_student_better)

    for i in range(students_number):
        student_score = sys.stdin.readline().strip().split(' ')
        student_score[tasks_key] = int(student_score[tasks_key])
        student_score[penalty_key] = int(student_score[penalty_key])
        heap.push(student_score)

    for i in range(students_number):
        student_score = heap.pop()
        print(student_score[name_key])


def profile():
    import cProfile, pstats, io
    from pstats import SortKey
    pr = cProfile.Profile()
    pr.enable()
    print_score()
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CALLS
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


if __name__ == '__main__':
    # print_score()
    # cProfile.run('print_score()')
    profile()
