    
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

    
