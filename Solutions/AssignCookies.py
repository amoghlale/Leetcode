class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0:
            return 0
        else:
            # for cases like g=[10,9,8,7] and s=[5,6,7,8]
            g.sort(reverse=True)
            # for cases like g=[10,9,8,7] and s=[10,9,8,7]
            s.sort()
            content_count = 0
            for i in g:
                if not s:
                    return content_count
                elif i <= s[-1]:
                    content_count += 1
                    s.pop()
            return content_count
