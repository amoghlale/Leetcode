class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, left, right = ([], 0, 0)
        q = [(left, right, '')]
        while q:
            left, right, s = q.pop()
            if len(s) == 2 * n:
                result.append(s)
            if left < n:
                q.append([left + 1, right, s + '('])
            if right < left:
                q.append([left, right + 1, s + ')'])
        return result

# Explanation:
# q                                 popped_value    result
# [(1, 0, '('), (1, 1, '()')]       (0, 0, '')
# [(1, 0, '('), (2, 1, '()(')]      (1, 1, '()')
# [(1, 0, '('), (2, 2, '()()')]     (2, 1, '()(')
# [(1, 0, '(')]                                     ['()()'] obtained from (2, 2, '()()')
# [(2, 0, '(('), (2, 1, '(()')]     (1, 0, '(')
# [(2, 0, '(('), (2, 2, '(()')]     (2, 1, '(()')
# [(2, 0, '((')]                    (2, 2, '(()')
# [(2, 1, '(()')]                   (2, 0, '((')
# [(2, 2, '(())')]                  (2, 1, '(()')
# []                                (2, 2, '(())')  ['()()', '(())'] obtained from (2, 2, '(())')
