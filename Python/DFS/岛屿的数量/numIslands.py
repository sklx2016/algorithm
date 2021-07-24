# -*- coding: utf-8 -*-
# @Author: skkkkkk
# @Date:   2021-07-24 15:42:31
# @Last Modified by:   skkkkkk
# @Last Modified time: 2021-07-24 16:21:32

'''
leetcode 200
给定2d网格图(其中，1代表陆地  0代表水)，计算岛屿数量。 岛被水包围，通过水平或垂直连接相邻的土地而形成。
您可以假设网格的所有四个边缘都被水包围
'''
def numIslands(grid):
	if len(grid) == 0:
		retrun 0
	cnt = 0
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == 1:
				cnt += 1


def DFS(grid, row, col):
	if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
		retrun
	grid[row][col] = 0
	DFS(grid, row - 1, col)
	DFS(grid, row + 1, col)
	DFS(grid, row, col - 1)
	DFS(grid, row, col + 1)