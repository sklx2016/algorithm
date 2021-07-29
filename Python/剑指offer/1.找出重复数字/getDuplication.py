
# 可以修改原数组 O(n)  
def getDuplication1(array ):
	for i in range(len(array)):
		while array[i] != i:
			if array[i] == array[array[i]]:
				return array[i]
			else:
				temp = array[i]
				array[i] = array[array[i]]
				array[array[i]] = temp 
	return -1


# 不能修改原数组  O(nlogn)  二分查找
def getDuplication2(array):
	left, right = 0, len(array) - 1
	while left <= right:
		mid = left + (right - left) / 2
		cnt = cntNumber(array, left, mid)
		if right == left:
			if cnt > 1:
				return left
			else:
				break
		if cnt > mid - left + 1:
		    left = mid
		else:
			right = mid
	return -1

def cntNumber(array, start, mid):
	cnt = 0
	for i in range(len(array)):
		if array[i] >= start and array[i] <= mid:
			cnt += 1
	return cnt