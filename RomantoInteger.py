class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
        return ans+d[s[-1]]
    def faster(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        running_sum = 0
        str_to_value = {}
        str_to_value["I"] = 1
        str_to_value["V"] = 5
        str_to_value["X"] = 10
        str_to_value["L"] = 50
        str_to_value["C"] = 100
        str_to_value["D"] = 500
        str_to_value["M"] = 1000
        str_to_value["IV"] = 4
        str_to_value["IX"] = 9
        str_to_value["XL"] = 40
        str_to_value["XC"] = 90
        str_to_value["CD"] = 400
        str_to_value["CM"] = 900

        while counter < len(s) :
            if s[counter: counter + 2]  in str_to_value:
                running_sum += str_to_value[s[counter: counter + 2]]
                counter += 2
            else:
                running_sum += str_to_value[s[counter]]
                counter += 1 
        return running_sum

s=Solution()
print(s.romanToInt(s = "III"))
print(s.romanToInt(s = "LVIII"))
print(s.romanToInt(s = "MCMXCIV"))