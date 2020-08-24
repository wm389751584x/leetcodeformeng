from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []
        level = [root]
        self.bfs(level, res)
        return res

    def bfs(self, level, res):
        if not level: return
        # nodes for next level
        next_lvl = []
        # int values for current level
        curr_val = []
        for node in level:
            if node.children:
                for child in node.children:
                    next_lvl.append(child)
            curr_val.append(node.val)
        # assigning values of current value or res
        # level = next_level
        res.append(curr_val)
        level = next_lvl
        self.bfs(level, res)


if __name__ == "__main__":
    pass