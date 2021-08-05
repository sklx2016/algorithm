# coding=utf-8
'''=================================================
@Author ：songkai
@Date   ：2021/8/5 10:08
=================================================='''

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
'''

def maxProfit(prices):
    n = len(prices)
    if n == 0 : return 0
    min_buy, res = prices[0], 0
    for i in range(1, n):
        res = max(res, prices[i] - min_buy)
        min_buy = min(min_buy, prices[i])
    return res



