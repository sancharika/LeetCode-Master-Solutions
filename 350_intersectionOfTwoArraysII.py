from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        T - O(n+m) S-O(1001) -> O(1)
 a hash table (represented by the array arr) of size 1001
 We iterate over the second array (nums2). For each element, we check if its count in the hash table (arr) is greater than zero. This indicates if the element exists in the first array as well.
If the element exists (count > 0), we add it to a result array (result) and decrement its count in the hash table. This ensures we only add duplicates once.
        """
        # T - O(n^2)
        # inter = []
        # for i in nums1:
        #     if i in nums2:
        #         inter.append(i)

        # return inter

        arr = [0] * 1001
        result = []
        for num in nums1:
            arr[num] += 1

        for num in nums2:
            if arr[num] > 0:
                result.append(num)
                arr[num] -= 1
        return result[: len(result)]
        
if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersect(nums1, nums2))