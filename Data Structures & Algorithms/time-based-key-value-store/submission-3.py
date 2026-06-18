class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map.setdefault(key,[]).append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        ls = self.map[key]

        start, end = 0, len(ls)-1
        prev_mid = None

        while start<=end:
            mid = start + (end-start)//2
            if ls[mid][0] == timestamp:
                return ls[mid][1]
            elif ls[mid][0] > timestamp:
                end = mid - 1
            else:
                prev_mid = ls[mid]
                start = mid + 1
        
        return "" if not prev_mid else prev_mid[1]