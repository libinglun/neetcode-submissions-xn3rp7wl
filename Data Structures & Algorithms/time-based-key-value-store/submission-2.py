class TimeMap:

    def __init__(self):
        self.timemap = {}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        l = 0
        r = len(self.timemap[key]) - 1

        print(self.timemap)
        if timestamp < self.timemap[key][l][1]:
            return ""

        # find the largest timestamp < timestamp
        while l <= r:
            if timestamp > self.timemap[key][r][1]:
                return self.timemap[key][r][0]
            print(l, r)
            m = (l + r) // 2

            if self.timemap[key][m][1] == timestamp:
                return self.timemap[key][m][0]
            elif self.timemap[key][m][1] > timestamp:
                r = m - 1
            else:
                if self.timemap[key][m+1][1] > timestamp:
                    return self.timemap[key][m][0]
                else:
                    l = m + 1


