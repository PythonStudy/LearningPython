#!/bin/env python
#coding:utf-8

import sys

#num = sys.argv[1]
def is_daffodil_number(num):
    if (num < 100) or (num > 999):
	print("Please give a number between 100 and 999.")
    str_num = str(num)
    if (pow(int(str_num[0]),3) + pow(int(str_num[1]),3) + pow(int(str_num[2]),3))== num:
	return True
    else :
	return False

if __name__  == "__main__":

    num = int(sys.argv[1])
    if is_daffodil_number(num):
	print("Number %d is a daffodil number." % num)
    else :
	print("Number %d is not a daffodil number." % num)
