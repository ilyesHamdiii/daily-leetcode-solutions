#https://leetcode.com/problems/design-movie-rental-system/
# Time:O(Mlogm+Qlogm)

# 
# # Space:O(n)
import bisect
from collections import deque, defaultdict
class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.seen:
            return False


        if len(self.queue) == self.limit:
            olds, oldd, oldt = self.queue.popleft()
            self.seen.remove((olds, oldd, oldt))
            self.dest_map[oldd].pop(0)

        self.queue.append((source,destination,timestamp))
        self.seen.add((source,destination,timestamp))
        self.dest_map[destination].append(timestamp)


        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        s,d,t = self.queue.popleft()
        self.seen.remove((s,d,t))
        self.dest_map[d].pop(0)
        return [s,d,t]

        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # count = 0

        # for (s,d,t) in self.queue:
        #     if d == destination and startTime <= t <= endTime:
        #         count += 1

        # return count 

        timestamp_list = self.dest_map[destination]                  #[90, 95, 105, 110]

        left = bisect.bisect_left(timestamp_list, startTime)
        right = bisect.bisect_right(timestamp_list, endTime)

        return right - left
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)