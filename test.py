# import math
# import os
# import random
# import re
# import sys
# from collections import defaultdict
#
# def countPairs(arr):
#     position2 = lambda r: r > 0 and not (r & (r - 1))
#     t = defaultdict(int)
#     for x in arr:
#         t[x] += 1
#     t = list(t.items())
#     ans = 0
#     for i in range(len(t)):
#         a, a_count = t[i]
#         for j in range(i, len(t)):
#             b, b_count = t[j]
#             if position2(a & b):
#                 if a == b:
#                     ans += (a_count * (a_count - 1)) // 2
#                 else:
#                     ans += a_count * b_count
#     return ans
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(countPairs(arr))
#
# def minOperations(arr, threshold, d):
#
#     de = defaultdict(lambda: [0, 0])
#     arr.sort()
#     answer = sys.maxsize
#     for x in arr:
#         step = 0
#         while True:
#             de[x][0] += 1
#             de[x][1] += step
#             if de[x][0] >= threshold:
#                 answer = min(answer, de[x][1])
#             if x == 0:
#                 break
#             x = x//d
#             step += 1
#     return answer