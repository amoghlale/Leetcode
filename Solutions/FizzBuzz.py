class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output_list = []
        for num in range(1, n + 1):
            str_num = ""
            if num % 3 != 0 and num % 5 != 0:
                output_list.append(str(num))
            else:
                if num % 3 == 0:
                    str_num += "Fizz"
                if num % 5 == 0:
                    str_num += "Buzz"
                output_list.append(str_num)
        return output_list
