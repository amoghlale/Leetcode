class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output_list = []
        for i in nums1:
            if i in nums2:
                index_in_2 = nums2.index(i)
                if index_in_2 == len(nums2) - 1:
                    output_list.append(-1)
                elif index_in_2 == len(nums2) - 2:
                    if i <= nums2[-1]:
                        output_list.append(nums2[-1])
                    else:
                        output_list.append(-1)
                else:
                    sliced_array = nums2[index_in_2 + 1: ]
                    flag = 0
                    for j in sliced_array:
                        if i <= j:
                            output_list.append(j)
                            flag = 1
                            break
                    if flag == 0:
                        output_list.append(-1)
        return output_list
