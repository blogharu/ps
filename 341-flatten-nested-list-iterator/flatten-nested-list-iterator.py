# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.deque = deque(nestedList)
        self.generator = self.get_generator()

    def get_generator(self):
        while self.deque:
            ele = self.deque.popleft()
            if ele.isInteger():
                yield ele
            else:
                self.deque.extendleft(ele.getList()[::-1])

    def next(self) -> int:
        return next(self.generator).getInteger()
        
    def hasNext(self) -> bool:
        ele = next(self.generator, None)
        if hasNext := ele is not None:
            self.deque.appendleft(ele)            
        return hasNext
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())