from itertools import chain, product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        look_up_dict = {
            2: ('a', 'b', 'c'),
            3: ('d', 'e', 'f'),
            4: ('g', 'h', 'i'),
            5: ('j', 'k', 'l'),
            6: ('m', 'n', 'o'),
            7: ('p', 'q', 'r', 's'),
            8: ('t', 'u', 'v'),
            9: ('w', 'x', 'y', 'z'),
        }
        if len(digits) == 0:
            return []
        combo_alphabets = [look_up_dict[int(i)] for i in digits]
        tuple_combos = list(chain(product(*combo_alphabets)))
        return list(map(lambda x: ''.join(x), tuple_combos))
