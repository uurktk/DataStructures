# O(n^2)
class Solution(object):
    def findDuplicate(self, nums):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return nums[i]

# Better way (floyd algorithm)
class SolutionTwo(object):
    def findDuplicate(self, nums):
        slowPointer = 0
        fastPointer = 0
        thirdPointer = 0
        while True:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
            if slowPointer == fastPointer:
                break
        while True:
            slowPointer = nums[slowPointer]
            thirdPointer = nums[thirdPointer]
            if slowPointer == thirdPointer:
                break
        return thirdPointer