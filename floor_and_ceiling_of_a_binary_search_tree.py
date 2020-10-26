"""
Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    if root_node.left:
        left_floor, left_ceil = findCeilingFloor(root_node.left, k, floor, ceil)
    else:
        left_floor, left_ceil = root_node.value, root_node.value
    if root_node.right:
        right_floor, right_ceil = findCeilingFloor(root_node.right, k, floor, ceil)
    else:
        right_floor, right_ceil = root_node.value, root_node.value
    if floor:
        if left_floor > floor and left_floor <= k:
            floor = left_floor
        if right_floor and right_floor > floor and right_floor <= k:
            floor = right_floor
    else:
        floor = max([left_floor, right_floor])
    if ceil:
        if left_ceil and left_ceil > floor and left_ceil <= k:
            ceil = left_ceil
        if right_ceil and right_ceil > floor and right_ceil <= k:
            ceil = right_ceil
    else:
        ceil = min([left_ceil, right_ceil])
    return floor, ceil



root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)



