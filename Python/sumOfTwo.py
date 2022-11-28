from typing import List


class Solution:
    def twoSumNew(self, nums: List[int], target: int):
        map = dict()

        for i, n in enumerate(nums):
            diff = target - n 
            print(map, diff, i)
            if diff in map:
                return (map.get(diff), i)
            map[n] = i
        
if __name__ == "__main__":
    s = Solution()
    print(s.twoSumNew([3,3], 6))
