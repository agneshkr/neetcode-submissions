class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        nums = self.store[key]
        lo, hi = 0, len(nums)
        pred = lambda x: nums[x][0] > timestamp

        while lo<hi:
            mid = lo + (hi-lo)//2

            if pred(mid):
                hi=mid
            else:
                lo=mid+1
        if lo==0:
            return ""
        else:
            return nums[lo-1][1]

