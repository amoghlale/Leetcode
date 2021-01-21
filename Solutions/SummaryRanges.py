class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return ["{}".format(nums[0])]
        else:
            intermediate_result = []
            output_result = []
            i = 0
            str_val = ""
            while i <= len(nums) - 1:
                if i == len(nums) -1:
                    str_val = str_val + str(nums[i])
                    intermediate_result.append(str_val)
                    break
                if nums[i+1] - nums[i] == 1:
                    str_val = str_val + str(nums[i]) + "->"
                else:
                    str_val = str_val + str(nums[i])
                    intermediate_result.append(str_val)
                    str_val = ""
                i += 1
            for i in intermediate_result:
                sublists = i.split("->")
                if len(sublists) > 1:
                    output_result.append((sublists[0] + "->" + sublists[-1]))
                else:
                    output_result.append(sublists[0])
            return output_result
