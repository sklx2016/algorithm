# -*- coding:utf-8 -*-
#堆排序（大根堆）

import random

def MAX_heapify(heap, HeapSize, root):
    left = root * 2
    right = left + 1
    large = root
    if left < HeapSize and heap[large] < heap[left]:
        large = left
    if right < HeapSize and heap[large] < heap[right]:
        large = right
    if root != large:
        heap[root], heap[large] = heap[large], heap[root]
        MAX_heapify(heap, HeapSize, large)

def Build_heap(heap):
    HeapSize = len(heap)
    for i in range((HeapSize - 2)// 2, -1, -1):
        MAX_heapify(heap, HeapSize, i)

def heapSort(heap):
    Build_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        MAX_heapify(heap, i, 0)
    return heap

b = [random.randint(1, 10) for i in range(10)]
print(heapSort(b))