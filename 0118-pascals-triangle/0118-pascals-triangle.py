class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []  # Store Pascal's Triangle rows
        for i in range(numRows):
            row = [1] * (i + 1)  # Initialize row with 1s
            for j in range(1, i):  # Compute middle values
                row[j] = result[i-1][j-1] + result[i-1][j]
            result.append(row)
        return result
