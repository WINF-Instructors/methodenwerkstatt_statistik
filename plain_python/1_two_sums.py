# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution1:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i,elem1 in enumerate(nums):
            for j, elem2 in enumerate(nums):
                if i!=j and elem1+elem2 == target:
                    return [i,j]

class Solution2:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i,elem in enumerate(nums):
            try:
                j=nums.index(target-elem)
                if i != j:
                    return [i,j]
            except:
                continue

class Solution3:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i,elem in enumerate(nums):
            check = [
                j for (j,other_elem) in enumerate(nums) 
                if (other_elem + elem == target) and (i!=j)
            ]
            if len(check)>0:
                return [i,check[0]]

import unittest
class SolutionTest(unittest.TestCase):
    
    def test_solution(self):
        test_cases = [
            ([2,7,11,15],9,[0,1]),
            ([3,2,4],6,[1,2]),
        ]
        algorithms = [Solution1.twoSum, Solution2.twoSum, Solution3.twoSum]

        for solution in algorithms:
            for num_list, target, expected_result in test_cases:
                self.assertEqual(solution(nums=num_list, target=target), expected_result)

    

if __name__ == '__main__':
    unittest.main()
