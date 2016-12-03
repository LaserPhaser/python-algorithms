# python3
# import pygraphviz as PG
import random


class Heap(object):
    def __init__(self):
        self.size = 0
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def right_child(self, i):
        return i * 2 + 2

    def left_child(self, i):
        return i * 2 + 1

    def build_heap(self):
        for i in reversed(range(0, self.size // 2 + 1)):
            self.sift_down(i)

    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l <= self.size - 1 and (self.heap[l][1] < self.heap[min_index][1] or (
                        self.heap[l][1] == self.heap[min_index][1] and self.heap[l][0] < \
                        self.heap[min_index][0])):
            min_index = l

        r = self.right_child(i)
        if r <= self.size - 1 and (self.heap[r][1] < self.heap[min_index][1] or (
                        self.heap[r][1] == self.heap[min_index][1] and self.heap[r][0] < \
                        self.heap[min_index][0])):
            min_index = r

        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.sift_down(min_index)

    def sift_up(self, i):
        while i > 0 and (
                        self.heap[self.parent(i)][1] > self.heap[i][1] or (
                                self.heap[self.parent(i)][1] == self.heap[i][1] and
                                self.heap[self.parent(i)][0] >
                                self.heap[i][0])):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, cpu, element):
        self.heap.append((cpu, element))
        self.size += 1
        self.sift_up(self.size - 1)

    def extract_min(self):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.size -= 1
        del self.heap[-1]
        self.sift_down(0)
        return result

    def change_priotiy(self, i, p):
        oldp = self.heap[i]
        self.heap[i] = p
        if p < oldp:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def draw_tree(self):
        A = PG.AGraph(directed=True, strict=True)

        size = len(self.heap)
        for i in range(size):
            if self.left_child(i) < size:
                A.add_edge(str(i) + ":" + str(self.heap[i]),
                           str(self.left_child(i)) + ":" + str(self.heap[self.left_child(i)]))
            if self.right_child(i) < size:
                A.add_edge(str(i) + ":" + str(self.heap[i]),
                           str(self.right_child(i)) + ":" + str(self.heap[self.right_child(i)]))

        A.write('ademo.dot')

        A.layout(prog='dot')


class JobQueue:
    def readjobs(self):

        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        # self.num_workers, m = (2, 5)
        # self.jobs = [1, 2,3 ,4 ,5]
        # self.num_workers, m = (4, 20)
        # self.jobs = [1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        # assert m == len(self.jobs)

    def stress_readjobs(self):
        self.num_workers, m = (random.randint(1, 1000), random.randint(10, 1000))
        self.jobs = [random.randint(0, 1000) for x in range(m)]

        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        workers_heap = Heap()
        self.assigned_workers = [0] * len(self.jobs)
        for i in range(self.num_workers):
            workers_heap.insert(i, 0)
        self.start_times = [None] * len(self.jobs)
        for i in range(len(self.jobs)):
            cpu, spent_time = workers_heap.extract_min()
            self.assigned_workers[i] = cpu
            self.start_times[i] = spent_time
            workers_heap.insert(cpu, spent_time + self.jobs[i])

    def assign_jobs_bruteforce(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.readjobs()
        self.assign_jobs()
        self.write_response()

    def stress(self, repeats):
        for i in range(repeats):
            self.stress_readjobs()
            self.assign_jobs()
            res1_w = self.assigned_workers
            res1_t = self.start_times
            self.assign_jobs_bruteforce()
            assert res1_w == self.assigned_workers
            assert res1_t == self.start_times


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
    # job_queue.stress(10)
