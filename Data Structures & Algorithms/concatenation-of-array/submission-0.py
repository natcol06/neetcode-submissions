class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        second_list = []


        for num in nums:
            second_list.append(num)

        final_list = second_list + nums

        return final_list