class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curr = 0
        step = 1  # direction: +1 down, -1 up

        for ch in s:
            rows[curr] += ch
            # Bounce at top or bottom row
            if curr == 0:
                step = 1
            elif curr == numRows - 1:
                step = -1
            curr += step

        return ''.join(rows)