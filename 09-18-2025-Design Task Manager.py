#https://leetcode.com/problems/design-task-manager/description/
# Time:O(1)
# 
# # Space:O(n)
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.taskPU = {}
        for u, t, p in tasks:
            self.taskPU[t] = [p, u]
            heapq.heappush(self.pq, (-p, -t, u))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskPU[taskId] = [priority, userId]
        heapq.heappush(self.pq, (-priority, -taskId, userId))
        
    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskPU[taskId][0] = newPriority
        heapq.heappush(self.pq, (-newPriority, -taskId, self.taskPU[taskId][1]))
        
    def rmv(self, taskId: int) -> None:
        self.taskPU[taskId] = [None, None]

    def execTop(self) -> int:
        while self.pq and ((self.taskPU[-self.pq[0][1]][0] != -self.pq[0][0] or self.taskPU[-self.pq[0][1]][1] != self.pq[0][2])):
            heapq.heappop(self.pq)
        if not self.pq: return -1
        self.taskPU[-self.pq[0][1]] = [None, None]
        return heapq.heappop(self.pq)[2]