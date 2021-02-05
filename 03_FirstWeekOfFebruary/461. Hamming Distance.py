class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        result = bin(result)
        print(result)
        count = 0
        for x in result:
            if x == '1':
                count += 1
        return count
        '''
            return bin(x ^ y).count(1) 
        '''