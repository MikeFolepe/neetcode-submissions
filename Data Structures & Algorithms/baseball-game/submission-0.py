class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []
        res = 0

        for op in operations:
            if op == '+':
                first, second = record[-1],record[-2]
                sum = first + second
                record.append(sum)
            elif op == 'D':
                last = record[-1]
                double = last * 2
                record.append(double)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))

        for rec in record:
            res += rec
        return res

        
        