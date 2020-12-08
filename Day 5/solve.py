class Solve():
    def __init__(self, file):
        self.file = file
        self.codes = self.parse()
        self.highestID = 0
        self.rows = []
        self.columns = []
        self.allID = []
    def parse(self):
        codes = []
        with open(self.file, "r") as f:
            codes = f.readlines()
        return codes
    def initRow_Col(self):
        self.rows.clear()
        self.columns.clear()
        for x in range(0, 128):
            self.rows.append(x)
        for x in range(0, 8):
            self.columns.append(x)
    def findHighestID(self):
        for j in self.codes:
            self.initRow_Col()
            for i in j:
                if i == "F":
                    end = len(self.rows) / 2
                    self.rows = self.rows[0:int(end)]
                else:
                    start = int(len(self.rows) / 2)
                    self.rows = self.rows[start:int(len(self.rows))]
                if i == "R":
                    start = int(len(self.columns) / 2)
                    self.columns = self.columns[start:int(len(self.columns))]
                else:
                    end = len(self.columns) / 2
                    self.columns = self.columns[0:int(end)]
            thisID = (self.rows[0] * 8) + self.columns[0]
            self.allID.append(thisID)
            self.highestID = max(self.highestID, thisID)
    def findMySeat(self):
        self.allID.sort()
        for i in self.allID:
            if self.allID[self.allID.index(i)+1] != i+1:
                print(i+1)
solve = Solve("input.txt")
solve.findHighestID()
solve.findMySeat()
