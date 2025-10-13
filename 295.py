import heapq

class MedianFinder:

    def __init__(self):
        self.qmin = []
        self.qmax = []

    def addNum(self, num: int) -> None:
        if len(self.qmin) == 0 or num < -self.qmin[0]:
            heapq.heappush(self.qmin, -num)
            if len(self.qmin) > len(self.qmax) + 1:
                heapq.heappush(self.qmax, -heapq.heappop(self.qmin))
        else:
            heapq.heappush(self.qmax, num)
            if len(self.qmax) > len(self.qmin):
                heapq.heappush(self.qmin, -heapq.heappop(self.qmax))

    def findMedian(self) -> float:
        return -self.qmin[0] if len(self.qmin) > len(self.qmax) \
            else (self.qmax[0] - self.qmin[0]) / 2
            
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()