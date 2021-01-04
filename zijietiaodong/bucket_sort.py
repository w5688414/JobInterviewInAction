class Solution():
    def __init__(self):
        super().__init__()

    def bucketSort(self,nums,bucketSize=5):
        maxValue=max(nums)
        minValue=min(nums)
        n=len(nums)
        bucketCount = (maxValue - minValue) // bucketSize + 1
        buckets=[[] for i in range(bucketCount)]
        for i in range(n):
            j=(nums[i]-minValue)//bucketSize
            buckets[j].append(nums[i])
        # print(buckets)
        # print(bucketCount)
        for i in range(bucketCount):
            buckets[i].sort()
        res=[]
        for i in range(bucketCount):
            res+=buckets[i]
        return res


if __name__ == "__main__":
    arr=[2,7,3,4,7,12,3,2,1]
    solution=Solution()
    res=solution.bucketSort(arr)
    print(res)