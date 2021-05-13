class Solution:
    def calculateDistance(self , point , triangle ):
        # write code here
        triangle = sorted(triangle,key = lambda x:x[0])
        if point[0]<triangle[0]