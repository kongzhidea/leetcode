class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = []
        ln = len(nums)
        if ln == 0:
            return
        k = k - (k/ln)*ln

        for i in range(k):
            l.append(nums[ln - k + i])

        for i in range(ln - k):
            l.append(nums[i])
        nums[:] = l[:]