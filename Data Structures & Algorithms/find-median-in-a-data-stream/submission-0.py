class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        length = len(self.data)
        if length % 2 == 1:
            return self.data[length//2]
        else:
            return (self.data[length//2] + self.data[(length//2)-1])/2


        
        