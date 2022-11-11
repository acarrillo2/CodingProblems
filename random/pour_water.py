"""
We are given an elevation map, heights[i] representing the height of the terrain at that index. 
The width at each index is 1. 

After V units of water fall at index K, how much water is at each index?

Water first drops at index K and rests on top of the highest terrain or water at that index. 
Then, it flows according to the following rules:
1. If the droplet would eventually fall by moving left, then move left.
2. Otherwise, if the droplet would eventually fall by moving right, then move right.
3. Otherwise, rise at it's current position.

Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. 
Also, "level" means the height of the terrain plus any water in that column.
We can assume there's infinitely high terrain on the two sides out of bounds of the array. 
Also, there could not be partial water being spread out evenly on more than 1 grid block - 
each unit of water has to be in exactly one block.

https://aaronice.gitbook.io/lintcode/array/pour-water
"""

def pour_water(heights, K, V):
    for i in range(V):
        searching = True
        index = K
        while searching:
            current = heights[index]
            if index - 1 >= 0 and current > heights[index - 1]:
                index = index - 1
            elif index + 1 < len(heights) and current > heights[index + 1]:
                index = index + 1
            else:
                # Either levels are flat around it or this is lower than others
                heights[index] += 1    
                searching = False
    return heights

heights = [2,1,1,2,1,2,2]
V = 4
K = 3
print(pour_water(heights, K, V))