import heapq

def sortArray(arr):
    minHeap = []
    for num in arr:
        heapq.heappush(minHeap,num)

    res = []
    while minHeap:
        top = heapq.heappop(minHeap)
        res.insert(0,top)

    return res

arr = [4,6,3,2,9]
print(arr)
res = sortArray(arr)
print(res)