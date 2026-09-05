class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def f(nums, l, r, k):
            if l == r:
                return nums[l]
            pivot_index = where_is_pivot(nums, l, r)
            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                return f(nums, l, pivot_index - 1, k)
            else:
                return f(nums, pivot_index + 1, r, k)
        def where_is_pivot(nums, l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] >= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        return f(nums, 0, len(nums) - 1, k - 1)