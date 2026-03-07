class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        x = int(s, 2)

        p1 = int('01' * ((n + 1) // 2), 2) & ((1 << n) - 1)
        p2 = int('10' * ((n + 1) // 2), 2) & ((1 << n) - 1)
        
        msb_mask = 1 << (n - 1)
        _min = float('inf')
        for i in range(n):
            _min = min(_min, (x ^ p1).bit_count(), (x ^ p2).bit_count())

            msb = 1 if (x & msb_mask) else 0
            x = ((x & ~msb_mask) << 1) | msb
        return _min
        
    def minFlips1(self, s: str) -> int:
        n = len(s)
        s2 = s + s
        
        diff1 = diff2 = 0
        min_flips = float('inf')

        for i in range(len(s2)):
            ch1 = '0' if i % 2 == 0 else '1'
            ch2 = '1' if i % 2 == 0 else '0'

            if s2[i] != ch1: diff1 += 1
            if s2[i] != ch2: diff2 += 1

            if i >= n:
                left_char1 = '0' if (i - n) % 2 == 0 else '1'
                left_char2 = '1' if (i - n) % 2 == 0 else '0'
                
                if s2[i - n] != left_char1: diff1 -= 1
                if s2[i - n] != left_char2: diff2 -= 1

            if i >= n - 1:
                min_flips = min(min_flips, diff1, diff2)
        return min_flips
    
    