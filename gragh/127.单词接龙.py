"""127.单词接龙
字典wordList 中从单词 beginWord和 endWord 的 转换序列 是一个按下述规格形成的序列：
序列中第一个单词是 beginWord 。序列中最后一个单词是 endWord 。每次转换只能改变一个字母。转换过程中的中间单词必须是字典wordList 中的单词。
给你两个单词 beginWord和 endWord 和一个字典 wordList ，找到从beginWord 到endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换
序列，返回 0。
"""
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet,visited,q,step = set(),set(),[],1
        for c in wordList:
            wordSet.add(c)
        q.append(beginWord)
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur == endWord:
                    return step
                c = list(cur)
                for j in range(len(c)):
                    t = c[j]
                    for x in range(ord('a'), ord('z') + 1):
                        a = chr(x)
                        c[j] = a
                        c = "".join(c)
                        if c in wordSet and c not in visited:
                            q.append(c)
                            visited.add(c)
                        #  道理是一样的，访问过的节点在字典中去掉，那么下次再访问时就不会把这个节点加到队列里。
                        # if c in wordSet:
                        #     q.append(c)
                        #     wordSet.remove(c)
                        c=list(c)
                    c = list(c)
                    c[j] = t
            step += 1
        return 0
s = Solution()
print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
