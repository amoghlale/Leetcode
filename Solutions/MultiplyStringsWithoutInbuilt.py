class Solution:
    def string_to_int_conversion_without_inbuilt(self, num, ref_dict):
        ten_multiplier = len(num) - 1
        if ten_multiplier == 0:
            num_converted = ref_dict[num[0]]
        else:
            num_converted = 0
            for i in num:
                num_converted += ref_dict[i] * pow(10, ten_multiplier)
                ten_multiplier -= 1
        return num_converted

    def multiply(self, num1: str, num2: str) -> str:
        ref_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        product = self.string_to_int_conversion_without_inbuilt(num1, ref_dict) * self.string_to_int_conversion_without_inbuilt(num2, ref_dict)
        if product == 0:
            return '0'
        else:
            result = ""
            while product != 0:
                result += str(product % 10)
                product = product // 10
            return result[::-1]
