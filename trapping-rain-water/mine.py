#!/usr/bin/env python3

"""
https://leetcode.com/submissions/detail/110008234/
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        Local maximums is the key here.
        
        Get a list of all local maximums.
        Then, from that list, prune values that are surrounded by higher neighbors. Repeat until there's no removals.
                 o
         o       o
        oooo o   o
        oooooo o o o
        oooooooooooo
         ^ ^ ^ ^ ^ ^ maximums
         ^       ^ ^ maxs after pruning
         [4,3,3,2,5,2]
         [4,5] <-- double max
         [4,5,2] <-- actual correct answer
         14 water

               o
           o   o
         o o   o  o
         o o o o oo
         o o o o oo
        ooooooooooo
         ^ ^ ^ ^  ^ max
         ^ ^   ^  ^ pruning
         [4,5,3,6,4]
         [4,5,6,4]

         
        Then, for each pair that list, you have your water level as the min() height of the pair. Loop through the map within that pair, and get the difference between water level and the map's height at that point. If positive, there's water here, so add it to a counter.
        
        --Special cases--
        
        - Empty array
        - Flat array
        - Many >= vs > corner cases:
        
        o oo o
        oooooo Where should the maximums be? What about pruned maximums?
        """
        
        #print(height)

        maxes = self.local_maxes(height)
        #print("maxes       ", maxes)
        #print("---values of", [height[i] for i in maxes])

        pruned = self.pruned_maxes(height, maxes)
        #print("final pruned", pruned)
        #print("---values of", [height[i] for i in pruned])

        summed = self.summed_pairs(height, pruned)
        #print(summed)
        
        return summed
        
    def local_maxes(self, height):
        maxes = []
        for i in range(len(height)):
            if i == 0:
                leftVal = -1
            else:
                leftVal = height[i-1]
            if i == len(height)-1:
                rightVal = -1
            else:
                rightVal = height[i+1]
            here = height[i]
            if leftVal <= here > rightVal:
                maxes.append(i)
            
            
        return maxes
    
    def pruned_maxes(self, height, maxes):
        # keep removing values that are surrounded by larger or equal values
        pruned = maxes[:]
        while True:
            for idx in range(1, len(pruned)-1):
                leftLoc = pruned[idx-1]
                leftHeight = height[leftLoc]
                hereLoc = pruned[idx]
                hereHeight = height[hereLoc]
                rightLoc = pruned[idx+1]
                rightHeight = height[rightLoc]

                if leftHeight >= hereHeight <= rightHeight:
                    pruned[idx:idx+1] = [] # remove here
                    break
            else: # nothing was removed, must be all pruned already
                break
        return pruned
    
    def summed_pairs(self, height, pruned):
        # pruned is an array of indexes for heightmap
        water = 0
        # for each pair
        for idx in range(len(pruned)-1):
            leftLoc = pruned[idx]
            rightLoc = pruned[idx+1]
            waterLevel = min(height[leftLoc], height[rightLoc])
            #print("between {} and {}, water level is {}".format(height[leftLoc], height[rightLoc], waterLevel))
            for map_idx in range(leftLoc, rightLoc):
                mapHeightHere = height[map_idx]
                diff = waterLevel - mapHeightHere
                #print("diff at {} is {}".format(map_idx, diff))
                if diff > 0:
                    water += diff
            
        return water


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
print(Solution().trap([3,4,3,3,2,3,1,2,1,5,1,2]) == 14)
print(Solution().trap([1]) == 0)
print(Solution().trap([1,1]) == 0)
print(Solution().trap([1,2,1]) == 0)
print(Solution().trap([1,1,1]) == 0)