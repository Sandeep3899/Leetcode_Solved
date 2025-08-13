from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        def backtrack(path: str, open_cnt: int, close_cnt: int) -> None:
            # If the string is complete, add to results
            if len(path) == 2 * n:
                res.append(path)
                return

            # Try to place an opening parenthesis if we still can
            if open_cnt < n:
                backtrack(path + "(", open_cnt + 1, close_cnt)

            # Place a closing parenthesis only if it won't invalidate the string
            if close_cnt < open_cnt:
                backtrack(path + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res
