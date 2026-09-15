class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Find the peak of the array
        maximum_id = 0
        for i in range(len(height)):
            if height[i] > height[maximum_id]:
                maximum_id = i
        water = 0

        l = 0

        # Left-to-peak
        for r in range(1, maximum_id):
            if height[r] > height[l]:
                l = r
            else:
                water += height[l] - height[r]
        

        r = len(height)-1
        for l in range(len(height)-2, maximum_id, -1):
            if height[l] > height[r]:
                r = l
            else:
                water += height[r] - height[l]
        
        return water