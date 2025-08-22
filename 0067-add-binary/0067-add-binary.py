class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        out = []

        while i >= 0 or j >= 0 or carry:
            bit_a = ord(a[i]) - 48 if i >= 0 else 0   # '0' -> 48
            bit_b = ord(b[j]) - 48 if j >= 0 else 0

            s = bit_a + bit_b + carry
            out.append(str(s & 1))   # s % 2
            carry = s >> 1           # s // 2

            i -= 1
            j -= 1

        return "".join(reversed(out))