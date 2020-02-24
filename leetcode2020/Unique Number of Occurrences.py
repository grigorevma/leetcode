'''
Given an array of integers arr,
write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

'''


class Solution:
    #Runtime 76ms 94%
    #memory 12.7 MB 100%
    def uniqueOccurrences(self, arr):
        self.state = True
        arr.sort()
        g = self.loop_coorutine(arr[0])
        next(g)
        for i in arr:
            g.send(i)
        g.send(arr[0])
        g.close()
        return self.state
    
    def loop_coorutine(self, first):
        count = 0
        sm = set()
        while True:
            value = yield
            if first == value:
                count +=1
            else:
                if count in sm:
                    self.state = False
                sm.add(count)
                count = 1
                first = value