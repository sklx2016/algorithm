#在数组中输出最大的K个数
import random
#方法一：  快排+类似二分查找

def find_topK(array, K):
    if len(array) < K:
        return array
    a = array[-1]
    right = [a] + [x for x in array[:-1] if x >= a]
    lens = len(right)
    if lens == K:
        return right
    if lens > K:
        return find_topK(right, K)
    else:
        left = [x for x in array[:-1] if x < a]
        return find_topK(left, K - lens) + right

A = [i for i in range(50)]
print(A)
print(find_topK(A, 10))



#方法二： 小根堆

def heapify(heap, HeapSize, root):
    left = root * 2
    right = left + 1
    large = root
    if left < HeapSize and heap[left] < heap[large]:
        large = left
    if right < HeapSize and heap[right] < heap[large]:
        large = right
    if root != large:
        heap[root], heap[large] = heap[large], heap[root]
        heapify(heap, HeapSize, large)

def Bulid_Heap(heap):
    HeapSize = len(heap)
    for i in range((HeapSize - 2) // 2, -1, -1):
        heapify(heap, HeapSize, i)
    print(heap)

def find_topK2(array, K):
    heap = array[:K]
    Bulid_Heap(heap)
    for i in range(K, len(array)):
        if array[i] > heap[0]:
            heap[0], array[i] = array[i], heap[0]
            heapify(heap, K, 0)
    return heap

print(find_topK2(A, 10))







