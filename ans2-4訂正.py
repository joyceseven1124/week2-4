# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:40:15 2022

@author: 劉佳怡
"""

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    data =[]
    for i in range(len(nums)):
        x = nums[i]
        for a in range(len(nums)):
            if(i != a) :
                result = x*nums[a]
                data.append(result)
    print(max(data))
        
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10