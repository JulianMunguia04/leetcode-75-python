# 238 Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        zero_count = nums.count(0)

        product = 1
        answer = []

        for i in range(len(nums)):
          if nums[i] != 0:
            product *= nums[i]
            print(product)

        for num in nums:
          if zero_count > 1:
            answer.append(0)
          elif zero_count == 1:
            if num == 0:
              answer.append(product)
            else:
              answer.append(0)
          else:
            answer.append(int(product / num))

        return answer