class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = list(x)
        val = 0
        minus = False
        if x[0] == '-':
            minus = True
            rev = reversed(x[1:])
            val = int(''.join(rev))
            rev = '-' + str(val)
        else:
            rev = reversed(x)
            val = int(''.join(rev))
            rev = str(val)
        if val >= pow(2, 31):
            if not minus:
                return '0'
            elif val > pow(2, 31):
                return '0'
        return rev
