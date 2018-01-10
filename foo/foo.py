#!/usr/local/bin/python3
#coding=utf-8
__version__ = "0.1"
__author__ = "brant"

Pi = 3.1415926

def sum(lst):
    col = lst[0]
    for v in lst[1:]:
        col = col+v
    return col

w = [10,28,39,27]
print(sum(w),Pi)
