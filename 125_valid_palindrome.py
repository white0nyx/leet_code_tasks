class Solution:
    def isPalindrome(self, string: str) -> bool:
        # Оставляем только буквы и цифры, игнорируя регистр
        filtered = ''.join(char.lower() for char in string if char.isalnum())
        return filtered == filtered[::-1]

