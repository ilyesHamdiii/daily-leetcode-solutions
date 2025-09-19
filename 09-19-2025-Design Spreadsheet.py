#https://leetcode.com/problems/design-spreadsheet/?envType=daily-question&envId=2025-09-19
# Time:O(1)
# 
# # Space:O(n)
class Spreadsheet:
    def __init__(self, rows: int):
        self.data = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value
        
    def resetCell(self, cell: str) -> None:
        self.data[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")
        x = int(x) if x.isdigit() else self.data[x]
        y = int(y) if y.isdigit() else self.data[y]
        return x + y
        