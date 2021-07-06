class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            segments = [i for i in s.split(' ') if i != '']
            return len(segments)
