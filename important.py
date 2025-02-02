    
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
            50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
            900: "CM", 1000: "M"
        }

        result = ""
        
        for value in sorted(roman_map.keys(), reverse=True):  # Sort keys in descending order
            result += (num // value) * roman_map[value]  # Add corresponding Roman symbols
            num %= value  # Reduce `num`
        
        return result

# Example usage
sol = Solution()
print(sol.intToRoman(989643791))  # Output: "MCMXCIV"













def sub_findSumZero(l):
    m={}
    s=0
    for i in range(len(l)):
        s+=l[i]
        if s==0:
            return l[:i+1]
        if s in m:
            si=m[s]+1
            return l[si:i+1]
        m[s]=i
        print(m)
l=[4,2,-3,1,6]
print(sub_findSumZero(l))

    
