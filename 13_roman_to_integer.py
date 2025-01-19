class Solution:
    def romanToInt(self, string: str) -> int:
        values_map = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        result = 0
        for i in range(len(string) - 1):
            if values_map[string[i]] < values_map[string[i + 1]]:
                result -= values_map[string[i]]
            else:
                result += values_map[string[i]]
        return result + values_map[string[-1]]

