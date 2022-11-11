"""
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region x contains another region y then x is bigger than y. Also, by definition, a region x contains itself.

Given two regions: region1 and region2, return the smallest region that contains both of them.

If you are given regions r1, r2, and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It is guaranteed the smallest region exists.
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
    
    def __str__(self):
        return "Node {name: " + self.name + ", parent: " + str(self.parent) + ", children: " + str(self.children) + "}"


def smallest_common_region(regions, r1, r2):
    region_map = build_data_structures(regions)
    region1_node = region_map[r1]
    region2_node = region_map[r2]
    region1_parents = []
    while region1_node.parent is not None:
        region1_parents.append(region1_node.parent)
        region1_node = region1_node.parent
    while region2_node.parent not in region1_parents:
        region2_node = region2_node.parent
    return region2_node.parent.name

def build_data_structures(list_of_lists):
    region_map = {}
    for list in list_of_lists:
        node = None
        if list[0] in region_map:
            node = region_map[list[0]]
        else:
            node = Node(list[0])
            region_map[list[0]] = node
        for i in range(len(list) - 1):
            child = None
            if list[i+1] in region_map:
                child = region_map[list[i+1]] 
            else:
                child = Node(list[i+1])
                region_map[list[i+1]] = child
            child.parent = node
            node.children.append(child)
    return region_map

def smallest_common_region_no_node(regions, r1, r2):
    parent_map = {}
    for list in regions:
        for i in range(len(list) - 1):
            parent_map[list[i+1]] = list[0]
    
    r1_ancestors = [r1]
    while r1 in parent_map:
        r1 = parent_map[r1]
        r1_ancestors.append(r1)
    
    while parent_map[r2] not in r1_ancestors:
        r2 = parent_map[r2]
    return parent_map[r2]
        

regions = [
    ["Earth","North America","South America"],
    ["North America","United States","Canada"],
    ["United States","New York","Boston"],
    ["Canada","Ontario","Quebec"],
    ["South America","Brazil"]
]
r1 = "Quebec"
r2 = "New York"

print(smallest_common_region_no_node(regions, r1, r2))

