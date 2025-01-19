class Solution:
    def reverseWords(self, s: str) -> str:
        # split по умолчанию разбивает по пробелам, даже если их несколько
        return ' '.join(s.split()[::-1])

