from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return []
        for i in root.children:
            res += self.postorder(i)
        res.append(root.val)
        return res