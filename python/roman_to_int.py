def romanToInt(s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        int_result = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                int_result += values[s[i + 1]] - values[s[i]]
                i += 2  
            else:
                int_result += values[s[i]]
                i += 1
                
        return int_result
        
string1 = 'MMIII'
string2 = 'DMVII'
print(romanToInt(string1))
print(romanToInt(string2))