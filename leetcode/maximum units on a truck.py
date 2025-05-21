class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        count = 0
        boxTypes.sort(key=lambda x: x[1],reverse= True)
        for i in boxTypes:
            if truckSize>0 and truckSize-i[0]>=0:
                count += i[0]*i[1]
                truckSize -= i[0]
            elif truckSize == 0:
                break
            else:
                count += truckSize*i[1]
                break
        return count
