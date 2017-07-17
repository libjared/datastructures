#!/usr/bin/env python3

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        start, end = 0, len(height) - 1
        liter = 0
        left_bound, right_bound = 0, 0
        left_bound_loc, right_bound_loc = -1, -1
        
        print('=================================')
        print('Initial state')
        self.printBoard(height, start, end, left_bound_loc, right_bound_loc)
        self.printStats(liter, left_bound, right_bound)

        while start < end:
            print('=================================')
            if height[start] < height[end]:
                if height[start] >= left_bound:
                    left_bound = height[start]
                    left_bound_loc = start
                    print("Set left bound to", left_bound)
                else:
                    liter += left_bound - height[start]
                    print("Added liters from left bound", left_bound-height[start])
                start += 1
            else:
                if height[end] >= right_bound:
                    right_bound = height[end]
                    right_bound_loc = end
                    print("Set right bound to", right_bound)
                else:
                    liter += right_bound - height[end]
                    print("Added liters from right bound", right_bound-height[end])
                end -= 1
            self.printBoard(height, start, end, left_bound_loc, right_bound_loc)
            self.printStats(liter, left_bound, right_bound)
        return liter
    
    def printBoard(self, height, start, end, left_bound_loc, right_bound_loc):
        # graph
        for top in range(5,0,-1):
            print("".join(['#' if x >= top else ' ' for x in height]))
        # markers
        marks = [' '] * len(height)
        marks[start] = '\\'
        marks[end] = '/'
        print("".join(marks))
        # bounds too
        bnd = [' '] * len(height)
        if left_bound_loc != -1:
            bnd[left_bound_loc] = '^'
        if right_bound_loc != -1:
            bnd[right_bound_loc] = '^'
        print("".join(bnd))
            
    
    def printStats(self, liter, left_bound, right_bound):
        print("Left  bound:", left_bound)
        print("Right bound:", right_bound)
        print("Liters:", liter)


a = [3,4,3,3,2,3,1,2,1,5,1,2]
print(Solution().trap(a))