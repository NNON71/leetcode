class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a,2)
        d=int(b,2)
        e = c+d
        return bin(e)[2:]

        # Optimal Approach
        
        # a_size, b_size = len(a), len(b)
        # max_size = max(a_size, b_size)
        # if a_size < b_size :
        #     a = '0' * (b_size - a_size) + a
        # else :
        #     b = '0' * (a_size - b_size) + b
        # print(a, b)
        # ans = []
        # carry = 0
        # for i in range(max_size - 1, -1, -1) :
        #     val = int(a[i]) + int(b[i]) + carry 
        #     c = val % 2
        #     carry = val // 2
        #     ans.append(str(c))
        #     print(ans)
            
        # if carry == 1 :
        #     ans.append('1')
        
        # res = "".join(ans[::-1])
        # return res
    
s = Solution()
print(s.addBinary(a = "1", b = "111")) #100